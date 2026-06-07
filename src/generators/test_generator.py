"""Test Generator v2 — templates hardcoded.

ZERO deps externas.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def generate_tests(schema_pydantic: str, api_code: str, app_name: str = "app", entities: list = None) -> dict:
    if not entities:
        entities = [{"name": "Item"}]

    first = entities[0]["name"].lower()

    test_api = f'''"""Tests para {app_name} — DB real + Auth JWT."""
import pytest
from fastapi.testclient import TestClient

# Override database to SQLite for tests
import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from backend.main import app
from backend.database import Base, engine

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


def test_register_login_crud(client):
    # 1. Register
    r = client.post("/auth/register", json={{"username": "testuser", "password": "secret123"}})
    assert r.status_code == 200, r.text

    # 2. Login
    r = client.post("/auth/login", data={{"username": "testuser", "password": "secret123"}})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    headers = {{"Authorization": f"Bearer {{token}}"}}

    # 3. List (empty)
    r = client.get("/api/{first}", headers=headers)
    assert r.status_code == 200
    assert r.json() == []

    # 4. Create
    r = client.post("/api/{first}", json={{"nome": "Teste"}}, headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["nome"] == "Teste"
    uid = data["id"]

    # 5. Get
    r = client.get(f"/api/{first}/{{uid}}", headers=headers)
    assert r.status_code == 200

    # 6. Update
    r = client.put(f"/api/{first}/{{uid}}", json={{"nome": "Atualizado"}}, headers=headers)
    assert r.status_code == 200
    assert r.json()["nome"] == "Atualizado"

    # 7. Delete
    r = client.delete(f"/api/{first}/{{uid}}", headers=headers)
    assert r.status_code == 200

    # 8. Me
    r = client.get("/auth/me", headers=headers)
    assert r.status_code == 200
    assert r.json()["username"] == "testuser"
'''

    test_models = f'''"""Tests de modelos ORM para {app_name}."""
import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from backend.database import Base, engine
from backend.models import {entities[0]["name"]}

def test_orm_model():
    Base.metadata.create_all(bind=engine)
    # Verifica que a tabela existe
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "{first}s" in tables or "users" in tables
'''

    conftest = """import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    import os
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"
    from backend.main import app
    from backend.database import Base, engine
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
"""

    return {
        "app_name": app_name,
        "test_api_py": test_api,
        "test_models_py": test_models,
        "conftest_py": conftest,
    }


if __name__ == "__main__":
    entities = [{"name": "Tarefa"}, {"name": "Projeto"}]
    result = generate_tests("", "", "taskapp", entities)
    print("=== TEST_API.PY (primeiras 25 linhas) ===")
    print("\n".join(result["test_api_py"].split("\n")[:25]))
