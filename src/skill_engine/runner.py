"""Skill Engine — executa skills a partir de SKILL.md.

Regras:
1. Le SKILL.md (frontmatter YAML + body)
2. Detecta action (code-gen, write-file, jinja-render)
3. Chama LLM via gateway
4. Persiste artefato em artifacts/
5. Escreve checkpoint em logs/
"""
import os
import json
import re
import time
from pathlib import Path
from typing import Dict, Any, Optional
import yaml

try:
    from llm.gateway import call_llm, get_task_model
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from llm.gateway import call_llm, get_task_model

ARTIFACTS_DIR = Path("artifacts")
LOGS_DIR = Path("logs")
SKILLS_DIR = Path(".claude/skills")


def _parse_skill_md(path: Path) -> dict:
    """Extrai frontmatter YAML + body de um SKILL.md."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return {"frontmatter": frontmatter or {}, "body": body}
    return {"frontmatter": {}, "body": text}


def _write_artifact(name: str, content: str, subdir: str = "") -> Path:
    """Salva artefato em artifacts/."""
    base = ARTIFACTS_DIR / subdir
    base.mkdir(parents=True, exist_ok=True)
    path = base / name
    path.write_text(content, encoding="utf-8")
    return path


def _log_step(skill_name: str, step: str, status: str, detail: str = ""):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "skill": skill_name,
        "step": step,
        "status": status,
        "detail": detail,
    }
    log_path = LOGS_DIR / "skill_runs.jsonl"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def run_skill(skill_name: str, context: Dict[str, Any]) -> dict:
    """Executa uma skill completa.

    Args:
        skill_name: Nome da skill (ex: create-landing-page).
        context: Variáveis para renderização (ex: hotel_nome, oferta).

    Returns:
        dict com status, artefatos gerados, proxima_acao.
    """
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_path.exists():
        return {"status": "erro", "erro": f"Skill {skill_name} nao encontrada em {skill_path}"}

    skill = _parse_skill_md(skill_path)
    fm = skill["frontmatter"]
    body = skill["body"]
    action = fm.get("action", "code-gen")
    task_type = fm.get("task_type", "default")

    _log_step(skill_name, "start", "ok", f"action={action} task_type={task_type}")

    # Monta prompt substituindo {{variavel}} do contexto
    prompt = body
    for key, val in context.items():
        prompt = prompt.replace(f"{{{key}}}", str(val))
    prompt = prompt.replace("{{", "{")  # Escapa restantes

    # Chama LLM
    try:
        raw_response = call_llm(prompt, task_type=task_type, timeout=120.0)
        _log_step(skill_name, "llm", "ok", f"modelo={get_task_model(task_type)}")
    except Exception as e:
        _log_step(skill_name, "llm", "erro", str(e))
        return {"status": "erro", "erro": str(e)}

    # Parseia resposta conforme action
    if action == "jinja-render":
        from string import Template as StringTemplate
        template_source = fm.get("template", "")
        template_path = Path(template_source)
        if template_path.exists():
            template_str = template_path.read_text(encoding="utf-8")
        else:
            template_str = template_source
        t = StringTemplate(template_str)
        # Prepara dict de substituicao (jinja usa {{}} mas string.Template usa {})
        mapping = {k: str(v) for k, v in context.items()}
        rendered = t.safe_substitute(**mapping)
        out_name = fm.get("output", f"{skill_name}_output.html")
        artifact = _write_artifact(out_name, rendered, subdir=skill_name)
        _log_step(skill_name, "render", "ok", str(artifact))
        return {
            "status": "ok",
            "artefatos": [str(artifact)],
            "proxima_acao": fm.get("next_action", "validar e entregar"),
        }

    elif action == "write-file":
        out_name = fm.get("output", f"{skill_name}_output.md")
        artifact = _write_artifact(out_name, raw_response, subdir=skill_name)
        _log_step(skill_name, "write", "ok", str(artifact))
        return {
            "status": "ok",
            "artefatos": [str(artifact)],
            "proxima_acao": fm.get("next_action", "revisar e commit"),
        }

    else:  # code-gen default
        # Tenta extrair bloco de código da resposta
        code = raw_response
        if "```" in raw_response:
            # Pega o primeiro bloco de código
            match = re.search(r"```(?:\w+)?\n(.*?)\n```", raw_response, re.DOTALL)
            if match:
                code = match.group(1)
        out_name = fm.get("output", f"{skill_name}_output.py")
        artifact = _write_artifact(out_name, code, subdir=skill_name)
        _log_step(skill_name, "code", "ok", str(artifact))
        return {
            "status": "ok",
            "artefatos": [str(artifact)],
            "proxima_acao": fm.get("next_action", "testar e integrar"),
        }


def list_skills() -> list:
    """Lista todas as skills disponíveis."""
    if not SKILLS_DIR.exists():
        return []
    return [p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()]


if __name__ == "__main__":
    print("[SKILL ENGINE] Skills disponiveis:", list_skills())
