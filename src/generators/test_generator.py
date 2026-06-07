"""Test Generator v2 — templates hardcoded.

ZERO deps externas.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def generate_tests(schema_pydantic: str, api_code: str, app_name: str = "app", entities: list = None) -> dict:
    if not entities:
        entities = [{"name": "Item"}]

    test_cases = []
    for e in entities:
        ename = e["name"]
        elower = ename.lower()
        test_cases.append(f"""
def test_list_{elower}(client):
    r = client.get("/api/{elower}")
    assert r.status_code == 200

def test_create_{elower}(client):
    r = client.post("/api/{elower}", json={{"nome": "Teste {ename}"}})
    assert r.status_code == 200
    assert r.json()["nome"] == "Teste {ename}"

def test_get_{elower}(client):
    # Cria primeiro
    create = client.post("/api/{elower}", json={{"nome": "Find"}})
    uid = create.json()["id"]
    r = client.get(f"/api/{elower}/{{uid}}")
    assert r.status_code == 200
""")

    test_api = f'''"""Tests para {app_name}."""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    return TestClient(app)

{chr(10).join(test_cases)}
'''

    test_models = f'''"""Tests de modelos para {app_name}."""
from pydantic import BaseModel

def test_models_exist():
    # Placeholder — substituir por testes reais de validacao
    assert True
'''

    conftest = """import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    from backend.main import app
    return TestClient(app)
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
