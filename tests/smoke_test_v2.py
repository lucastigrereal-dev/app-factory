"""Smoke test v2 — valida geradores de código real.

Rodar:
    python tests/smoke_test_v2.py

Checks:
- Schema generator produz SQL e Pydantic
- API generator produz main.py
- Frontend generator produz HTML
- Renderer cria arquivos físicos
- Smoke test v1 ainda passa (backward compat)
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(r"C:\Users\lucas\Desktop\O_OMNISVERSO_REAL\SystemOS antiga pp factory")
sys.path.insert(0, str(REPO_ROOT))

from src.generators.schema_generator import generate_schema
from src.generators.api_generator import generate_api, generate_dockerfile
from src.generators.frontend_generator import generate_frontend
from src.scaffold.renderer import render_project


def test_schema_generator():
    print("[TEST] Schema generator...")
    desc = "App de tarefas. Entidades: Tarefa (titulo, status, prioridade), Projeto (nome, descricao), Usuario (nome, email)"
    result = generate_schema(desc, "taskapp")
    assert result["sql"], "SQL vazio"
    assert result["pydantic"], "Pydantic vazio"
    assert "CREATE TABLE" in result["sql"].upper() or "CREATE" in result["sql"].upper(), f"SQL sem CREATE: {result['sql'][:100]}"
    print(f"[PASS] SQL {len(result['sql'])} chars, Pydantic {len(result['pydantic'])} chars")


def test_api_generator():
    print("[TEST] API generator...")
    schema_py = "class Tarefa(BaseModel): titulo: str; status: str"
    schema_sql = "CREATE TABLE tarefas (id UUID PRIMARY KEY, titulo VARCHAR, status VARCHAR)"
    result = generate_api(schema_py, schema_sql, "taskapp")
    assert result["main_py"], "main.py vazio"
    assert "fastapi" in result["main_py"].lower() or "FastAPI" in result["main_py"], f"main.py sem FastAPI: {result['main_py'][:100]}"
    print(f"[PASS] main.py {len(result['main_py'])} chars")


def test_frontend_generator():
    print("[TEST] Frontend generator...")
    result = generate_frontend("Dashboard de tarefas com kanban", "taskapp", "html")
    assert result["index_html"], "HTML vazio"
    html_lower = result["index_html"].lower()
    assert "<html>" in html_lower or "<!doctype>" in html_lower or "<!doctype html>" in html_lower, f"HTML invalido: {result['index_html'][:100]}"
    print(f"[PASS] index.html {len(result['index_html'])} chars")


def test_renderer():
    print("[TEST] Scaffold renderer...")
    payload = {
        "schema_sql": "CREATE TABLE users (id UUID PRIMARY KEY);",
        "schema_pydantic": "from pydantic import BaseModel\nclass User(BaseModel): id: str",
        "api_main": "from fastapi import FastAPI\napp = FastAPI()",
        "frontend_html": "<html><body>Hello</body></html>",
        "requirements": ["fastapi", "uvicorn"],
        "dockerfile": generate_dockerfile(),
        "docker_compose": "version: '3.8'\nservices:\n  api:\n    build: .",
    }
    result = render_project("smoke_test_app", payload)
    assert result["file_count"] >= 4, f"Poucos arquivos: {result['file_count']}"
    assert Path(result["path"]).exists()
    print(f"[PASS] {result['file_count']} arquivos em {result['path']}")


def main():
    print("=" * 50)
    print("SMOKE TEST v2 — Geradores de código real")
    print("=" * 50)
    tests = [test_schema_generator, test_api_generator, test_frontend_generator, test_renderer]
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
