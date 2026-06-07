"""Orchestrator v2 — Pipeline E2E completo com geração de código real via templates.

Uso:
    python src/orchestrator_v2.py --idea "Sistema de reservas para hotel" --app-name "hotel-app"
"""
import argparse
import json
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.generators.schema_generator import generate_schema, generate_seed_data
from src.generators.api_generator import generate_api, generate_dockerfile, generate_docker_compose
from src.generators.frontend_generator import generate_frontend
from src.generators.test_generator import generate_tests
from src.scaffold.renderer import render_project, generate_readme
from src.llm.gateway import call_llm


def log(step: str, status: str, detail: str = ""):
    entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "step": step, "status": status, "detail": detail}
    log_path = Path("logs/orchestrator.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"  [{step}] {status} — {detail}")


def run_intake(idea: str) -> dict:
    log("intake", "start", idea[:60])
    prompt = f"""Classifique em JSON: {{"tipo":"saas|dashboard|crm|landing","descricao":"...","entidades":["..."]}}
Ideia: {idea}
Responda apenas JSON."""
    raw = call_llm(prompt, task_type="classify", timeout=20.0)
    try:
        data = json.loads(raw.strip())
    except Exception:
        data = {"tipo": "saas", "descricao": idea, "entidades": ["Item"]}
    log("intake", "ok", data.get("tipo", ""))
    return data


def run_schema(description: str, app_name: str, entities: list) -> dict:
    log("schema", "start", f"{len(entities)} entidades")
    result = generate_schema(description, app_name)
    log("schema", "ok", f"SQL {len(result['sql'])} chars")
    return result


def run_api(schema_result: dict, app_name: str) -> dict:
    log("api", "start")
    result = generate_api(schema_result["pydantic"], schema_result["sql"], app_name, schema_result.get("entities", []))
    log("api", "ok", f"main.py {len(result['main_py'])} chars")
    return result


def run_frontend(description: str, app_name: str, entities: list) -> dict:
    log("frontend", "start")
    result = generate_frontend(description, app_name, "html", entities)
    log("frontend", "ok", f"index.html {len(result['index_html'])} chars")
    return result


def run_tests(schema_result: dict, api_result: dict, app_name: str) -> dict:
    log("tests", "start")
    result = generate_tests(schema_result["pydantic"], api_result["main_py"], app_name, schema_result.get("entities", []))
    log("tests", "ok", f"test_api.py {len(result['test_api_py'])} chars")
    return result


def run_scaffold(payload: dict, app_name: str) -> dict:
    log("scaffold", "start")
    result = render_project(app_name, payload)
    log("scaffold", "ok", f"{result['file_count']} arquivos")
    return result


def run_e2e(idea: str, app_name: str, app_type: str = "saas") -> dict:
    print(f"\n[ORCHESTRATOR v2] App: {app_name}")
    print(f"[ORCHESTRATOR v2] Ideia: {idea}")
    t0 = time.time()

    intake = run_intake(idea)
    description = intake.get("descricao", idea)
    entities = intake.get("entidades", [])

    schema_result = run_schema(description, app_name, entities)
    api_result = run_api(schema_result, app_name)
    frontend_result = run_frontend(description, app_name, schema_result.get("entities", []))
    tests_result = run_tests(schema_result, api_result, app_name)

    payload = {
        "schema_sql": schema_result["sql"],
        "schema_pydantic": schema_result["pydantic"],
        "api_main": api_result["main_py"],
        "api_routers": api_result["router_py"],
        "frontend_html": frontend_result["index_html"],
        "test_api": tests_result["test_api_py"],
        "test_models": tests_result["test_models_py"],
        "conftest": tests_result["conftest_py"],
        "requirements": api_result["requirements"],
        "dockerfile": generate_dockerfile(),
        "docker_compose": generate_docker_compose(app_name),
        "readme": generate_readme(app_name, {"backend": "FastAPI", "database": "PostgreSQL", "frontend": "HTML + Tailwind"}),
        "seed_sql": generate_seed_data(schema_result, app_name),
    }
    scaffold_result = run_scaffold(payload, app_name)

    snap = {
        "app_name": app_name,
        "idea": idea,
        "type": app_type,
        "intake": intake,
        "path": scaffold_result["path"],
        "files": scaffold_result["files"],
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "duration_sec": round(time.time() - t0, 1),
    }
    snap_path = Path("checkpoints") / f"snapshot_{app_name}_{time.strftime('%Y%m%d_%H%M%S')}.json"
    snap_path.parent.mkdir(parents=True, exist_ok=True)
    snap_path.write_text(json.dumps(snap, indent=2, ensure_ascii=False), encoding="utf-8")
    log("snapshot", "ok", str(snap_path))

    print(f"\n[RESUMO] Pipeline em {snap['duration_sec']}s")
    print(f"  Pasta: {scaffold_result['path']}")
    print(f"  Arquivos: {scaffold_result['file_count']}")
    print(f"  Inclui: backend/, frontend/, db/, tests/, docker-compose.yml")
    print(f"  Proxima acao: cd {scaffold_result['path']}")
    return snap


def main():
    parser = argparse.ArgumentParser(description="App Factory Orchestrator v2 — E2E código real")
    parser.add_argument("--idea", required=True)
    parser.add_argument("--app-name", required=True)
    parser.add_argument("--type", default="saas", choices=["saas", "dashboard", "landing", "crm", "api"])
    args = parser.parse_args()
    run_e2e(args.idea, args.app_name, args.type)


if __name__ == "__main__":
    main()
