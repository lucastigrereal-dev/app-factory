"""Gateway LLM com Router Ollama.

Suporta:
- Ollama direto (porta 11434) — primary, sempre disponível
- OpenRouter (externo) — fallback de último recurso

ZERO dependências externas — usa apenas stdlib.
"""
import os
import json
import time
import hashlib
import urllib.request
import urllib.error
from typing import Optional
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────
LITELLM_URL = os.getenv("LITELLM_URL", "http://localhost:4001")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OPENROUTER_URL = "https://openrouter.ai/api/v1"
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "")

LOG_PATH = Path("logs/llm_calls.jsonl")
CACHE_PATH = Path("logs/llm_cache.jsonl")

# ── Task Router Map ────────────────────────────────────────────────
TASK_MODEL_MAP = {
    "code-gen":        "qwen2.5-coder:7b",        # reasoning, código
    "landing-page":    "qwen2.5-coder:7b",        # creative (usar qwen por enquanto)
    "prd-write":       "qwen2.5-coder:7b",        # summarization
    "classify":        "qwen2.5-coder:7b",        # classification
    "quick":           "llama3.2:3b",             # light, rápido
    "default":         "qwen2.5-coder:7b",
}

FALLBACK_CHAIN = [
    "qwen2.5-coder:7b",
    "llama3.1:8b",
    "llama3.2:3b",
]

# ── Core ───────────────────────────────────────────────────────────
def _log_call(model: str, prompt_hash: str, latency: float, tokens: int, status: str):
    """Persiste chamada em JSONL."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "model": model,
        "prompt_hash": prompt_hash,
        "latency_ms": round(latency * 1000),
        "tokens": tokens,
        "status": status,
    }
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _cache_key(prompt: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()[:16]


def _check_cache(prompt: str, model: str) -> Optional[str]:
    if not CACHE_PATH.exists():
        return None
    key = _cache_key(prompt, model)
    with CACHE_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                if entry.get("key") == key:
                    return entry.get("response")
            except json.JSONDecodeError:
                continue
    return None


def _save_cache(prompt: str, model: str, response: str):
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    key = _cache_key(prompt, model)
    entry = {"key": key, "response": response, "ts": time.time()}
    with CACHE_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _call_ollama(prompt: str, model: str, timeout: float = 60.0) -> str:
    """Chama Ollama API diretamente via urllib."""
    url = f"{OLLAMA_URL}/api/generate"
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.7},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("response", "")


def _call_openrouter(prompt: str, model: str = "google/gemini-2.5-flash", timeout: float = 30.0) -> str:
    """Fallback via OpenRouter."""
    if not OPENROUTER_KEY:
        raise RuntimeError("OPENROUTER_API_KEY não configurada")
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{OPENROUTER_URL}/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]


# ── Public API ───────────────────────────────────────────────────
def call_llm(prompt: str, task_type: str = "default", timeout: float = 60.0) -> str:
    """Chama LLM via Router Ollama.

    Args:
        prompt: Texto do prompt.
        task_type: Tipo de tarefa (code-gen, landing-page, classify, quick, default).
        timeout: Timeout em segundos.

    Returns:
        Resposta do modelo como string.
    """
    model = TASK_MODEL_MAP.get(task_type, TASK_MODEL_MAP["default"])
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()[:16]

    # 1. Cache
    cached = _check_cache(prompt, model)
    if cached:
        _log_call(model, prompt_hash, 0.0, 0, "cache_hit")
        return cached

    # 2. Primary: Ollama direto
    t0 = time.time()
    try:
        response = _call_ollama(prompt, model, timeout)
        latency = time.time() - t0
        _save_cache(prompt, model, response)
        _log_call(model, prompt_hash, latency, len(response.split()), "success")
        return response
    except Exception as e:
        latency = time.time() - t0
        _log_call(model, prompt_hash, latency, 0, f"ollama_error: {type(e).__name__}")

    # 3. Fallback chain: outros modelos Ollama
    for fallback_model in FALLBACK_CHAIN:
        if fallback_model == model:
            continue
        try:
            t0 = time.time()
            response = _call_ollama(prompt, fallback_model, timeout)
            latency = time.time() - t0
            _save_cache(prompt, fallback_model, response)
            _log_call(fallback_model, prompt_hash, latency, len(response.split()), "fallback_success")
            return response
        except Exception:
            continue

    # 4. Last resort: OpenRouter
    try:
        t0 = time.time()
        response = _call_openrouter(prompt)
        latency = time.time() - t0
        _log_call("openrouter/gemini-flash", prompt_hash, latency, len(response.split()), "openrouter_success")
        return response
    except Exception as e:
        raise RuntimeError(f"Todos os modelos falharam. Último erro: {e}")


def get_task_model(task_type: str) -> str:
    """Retorna o modelo mapeado para um task_type."""
    return TASK_MODEL_MAP.get(task_type, TASK_MODEL_MAP["default"])


if __name__ == "__main__":
    # Teste rápido
    print("[TEST] Gateway LLM")
    print("Modelo para code-gen:", get_task_model("code-gen"))
    print("Modelo para quick:", get_task_model("quick"))

    # Testar chamada real (se Ollama estiver online)
    try:
        resp = call_llm("Responda em uma palavra: qual a cor do céu?", task_type="quick", timeout=15.0)
        print("[OK] Resposta:", resp.strip())
    except Exception as e:
        print("[ERRO]", e)
        print("   Dica: verifique se Ollama esta rodando na porta 11434")
