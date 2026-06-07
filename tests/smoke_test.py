"""Smoke test App Factory v3.1 — valida pipeline basico.

Rodar:
    python tests/smoke_test.py

Checks:
- Gateway LLM responde
- Skill create-landing-page gera HTML
- HTML tem tags essenciais
- Snapshot e logs sao escritos
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(r"C:\Users\lucas\Desktop\O_OMNISVERSO_REAL\SystemOS antiga pp factory")
src_path = REPO_ROOT / "src"
sys.path.insert(0, str(src_path))

from llm.gateway import call_llm


def test_gateway():
    print("[TEST] Gateway LLM...")
    resp = call_llm("Responda com uma palavra: qual a capital do Brasil?", task_type="quick", timeout=20.0)
    assert len(resp.strip()) > 3, f"Resposta vazia ou muito curta: {resp}"
    print("[PASS] Gateway OK")


def test_landing_page_skill():
    print("[TEST] Skill create-landing-page...")
    import subprocess
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".claude/skills/create-landing-page/run.py"),
         "--nome", "Hotel Teste", "--oferta", "Pacote Teste", "--preco", "R$ 1"],
        capture_output=True, text=True, cwd=str(REPO_ROOT),
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    data = json.loads(result.stdout)
    assert data["status"] == "ok"
    artifact = Path(data["artefato"])
    assert artifact.exists()
    html = artifact.read_text(encoding="utf-8")
    assert "<title>" in html
    assert "</section>" in html
    print(f"[PASS] Landing page gerada: {artifact} ({len(html)} chars)")


def test_logs():
    print("[TEST] Logs escritos...")
    log = REPO_ROOT / "logs" / "llm_calls.jsonl"
    assert log.exists(), "Log de LLM nao encontrado"
    lines = log.read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) >= 1
    print(f"[PASS] Logs OK ({len(lines)} entradas)")


def main():
    print("=" * 50)
    print("SMOKE TEST — App Factory v3.1")
    print("=" * 50)
    tests = [test_gateway, test_landing_page_skill, test_logs]
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"[FAIL] {t.__name__}: {e}")
    print("=" * 50)
    print(f"RESULTADO: {passed}/{len(tests)} PASS")
    return 0 if passed == len(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
