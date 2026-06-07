"""Smoke Test v3 — Valida que apps gerados tem DB real, auth JWT, frontend fetch.

Roda: python tests/smoke_test_v3.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.generators.schema_generator import generate_schema, generate_orm_models
from src.generators.api_generator import generate_api, generate_dockerfile, generate_docker_compose
from src.generators.frontend_generator import generate_frontend
from src.generators.test_generator import generate_tests
from src.scaffold.renderer import render_project


def test_orm_models_generated():
    print("[TEST] ORM models gerados...")
    entities = [{"name": "Lead", "fields": [{"name": "nome", "type": "str", "required": True}, {"name": "email", "type": "str", "required": True}]}]
    orm = generate_orm_models(entities, "crm-test")
    assert "class Lead(Base):" in orm, "ORM class Lead nao encontrada"
    assert "__tablename__ = 'leads'" in orm, "tablename nao definido"
    assert "Column" in orm, "SQLAlchemy Column nao encontrado"
    print("[PASS] ORM models OK")


def test_api_uses_sqlalchemy():
    print("[TEST] API usa SQLAlchemy...")
    entities = [{"name": "Lead", "fields": [{"name": "nome", "type": "str", "required": True}]}]
    result = generate_api("", "", "crm-test", entities)
    main = result["main_py"]
    assert "from database import get_db" in main, "get_db nao importado"
    assert "Session = Depends(get_db)" in main, "Session nao usado"
    assert "db = {}" not in main, "ERRO: ainda usa db = {} (fake DB)"
    assert "db.query(Lead)" in main, "db.query nao encontrado"
    assert "get_current_user" in main, "auth nao protege endpoints"
    print("[PASS] API SQLAlchemy OK")


def test_frontend_has_fetch():
    print("[TEST] Frontend tem fetch...")
    # Le template diretamente (nao depende do LLM estar online)
    tpl_path = Path(__file__).resolve().parent.parent / "src" / "generators" / "templates" / "frontend.html.template"
    html = tpl_path.read_text(encoding="utf-8")
    assert "fetch(" in html, "fetch nao encontrado no template frontend"
    assert "/api/" in html, "URL de API nao encontrada"
    assert "localStorage.getItem('token')" in html, "token JWT nao armazenado"
    print("[PASS] Frontend fetch OK")


def test_tests_cover_auth_and_db():
    print("[TEST] Testes cobrem auth + DB...")
    entities = [{"name": "Lead", "fields": [{"name": "nome", "type": "str", "required": True}]}]
    result = generate_tests("", "", "crm-test", entities)
    test_api = result["test_api_py"]
    assert "test_register_login_crud" in test_api, "teste de auth+crud nao encontrado"
    assert "/auth/register" in test_api, "register nao testado"
    assert "/auth/login" in test_api, "login nao testado"
    assert "sqlite" in test_api.lower() or "DATABASE_URL" in test_api, "DB de teste nao configurado"
    print("[PASS] Testes auth+DB OK")


def test_scaffold_creates_database_and_auth():
    print("[TEST] Scaffold cria database.py + auth.py...")
    payload = {
        "api_main": "from fastapi import FastAPI\napp = FastAPI()",
        "database_py": "from sqlalchemy import create_engine\nengine = create_engine('sqlite:///')",
        "auth_py": "from fastapi import APIRouter\nrouter = APIRouter()",
        "frontend_html": "<html><body>Test</body></html>",
        "requirements": ["fastapi"],
        "test_api": "def test_ok(): assert True",
        "test_models": "def test_models(): assert True",
        "conftest": "import pytest",
    }
    result = render_project("smoke_v3_test", payload)
    files = result["files"]
    assert any("database.py" in f for f in files), "database.py nao criado"
    assert any("auth.py" in f for f in files), "auth.py nao criado"
    print("[PASS] Scaffold database+auth OK")


def main():
    print("=" * 50)
    print("SMOKE TEST v3 — DB real + Auth + Fetch")
    print("=" * 50)
    tests = [
        test_orm_models_generated,
        test_api_uses_sqlalchemy,
        test_frontend_has_fetch,
        test_tests_cover_auth_and_db,
        test_scaffold_creates_database_and_auth,
    ]
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {t.__name__}: {e}")
        except Exception as e:
            print(f"[ERRO] {t.__name__}: {e}")
    print("=" * 50)
    print(f"RESULTADO: {passed}/{len(tests)} PASS")
    if passed == len(tests):
        print("FASE 3 VALIDADA — apps gerados tem DB real, auth e fetch.")
    else:
        print("FALHA — revisar generators.")
    return passed == len(tests)


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
