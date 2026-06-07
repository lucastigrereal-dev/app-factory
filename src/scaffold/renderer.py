"""Scaffold Renderer — transforma código gerado em arquivos reais no disco.

Regras:
- Cria pasta do projeto em artifacts/
- Salva backend/, frontend/, tests/, infra/
- Gera tree.json com estrutura
- NUNCA sobrescreve sem aviso (adiciona suffix se existe)
"""
import json
import time
from pathlib import Path
from typing import Dict

ARTIFACTS_ROOT = Path("artifacts")


def _safe_path(base: Path, name: str) -> Path:
    """Retorna path seguro; adiciona _1, _2 se já existir."""
    target = base / name
    if not target.exists():
        return target
    i = 1
    while True:
        candidate = base / f"{name}_{i}"
        if not candidate.exists():
            return candidate
        i += 1


def render_project(project_name: str, payload: Dict) -> dict:
    """Cria arquivos físicos a partir do payload do pipeline.

    Args:
        project_name: nome base da pasta
        payload: dict com chaves opcionais:
            - schema_sql: str
            - schema_pydantic: str
            - api_main: str
            - api_routers: str
            - frontend_html: str
            - test_api: str
            - test_models: str
            - conftest: str
            - dockerfile: str
            - docker_compose: str
            - requirements: list[str]
            - readme: str
            - seed_sql: str

    Returns:
        dict com pasta, arquivos criados, tree
    """
    base = _safe_path(ARTIFACTS_ROOT, project_name)
    base.mkdir(parents=True, exist_ok=True)

    files = []

    # Backend
    backend = base / "backend"
    backend.mkdir(exist_ok=True)
    if payload.get("api_main"):
        p = backend / "main.py"
        p.write_text(payload["api_main"], encoding="utf-8")
        files.append(str(p))
    if payload.get("api_routers"):
        routers = backend / "routers"
        routers.mkdir(exist_ok=True)
        p = routers / "__init__.py"
        p.write_text("", encoding="utf-8")
        p = routers / "routes.py"
        p.write_text(payload["api_routers"], encoding="utf-8")
        files.append(str(p))
    if payload.get("schema_pydantic"):
        p = backend / "models.py"
        p.write_text(payload["schema_pydantic"], encoding="utf-8")
        files.append(str(p))
    if payload.get("database_py"):
        p = backend / "database.py"
        p.write_text(payload["database_py"], encoding="utf-8")
        files.append(str(p))
    if payload.get("auth_py"):
        p = backend / "auth.py"
        p.write_text(payload["auth_py"], encoding="utf-8")
        files.append(str(p))
    if payload.get("requirements"):
        p = backend / "requirements.txt"
        p.write_text("\n".join(payload["requirements"]), encoding="utf-8")
        files.append(str(p))
    if payload.get("dockerfile"):
        p = backend / "Dockerfile"
        p.write_text(payload["dockerfile"], encoding="utf-8")
        files.append(str(p))

    # DB
    db = base / "db"
    db.mkdir(exist_ok=True)
    if payload.get("schema_sql"):
        p = db / "schema.sql"
        p.write_text(payload["schema_sql"], encoding="utf-8")
        files.append(str(p))
    if payload.get("seed_sql"):
        p = db / "seed.sql"
        p.write_text(payload["seed_sql"], encoding="utf-8")
        files.append(str(p))

    # Frontend
    frontend = base / "frontend"
    frontend.mkdir(exist_ok=True)
    if payload.get("frontend_html"):
        p = frontend / "index.html"
        p.write_text(payload["frontend_html"], encoding="utf-8")
        files.append(str(p))

    # Tests
    tests = base / "tests"
    tests.mkdir(exist_ok=True)
    if payload.get("test_api"):
        p = tests / "test_api.py"
        p.write_text(payload["test_api"], encoding="utf-8")
        files.append(str(p))
    if payload.get("test_models"):
        p = tests / "test_models.py"
        p.write_text(payload["test_models"], encoding="utf-8")
        files.append(str(p))
    if payload.get("conftest"):
        p = tests / "conftest.py"
        p.write_text(payload["conftest"], encoding="utf-8")
        files.append(str(p))

    # Infra
    if payload.get("docker_compose"):
        p = base / "docker-compose.yml"
        p.write_text(payload["docker_compose"], encoding="utf-8")
        files.append(str(p))

    # README
    if payload.get("readme"):
        p = base / "README.md"
        p.write_text(payload["readme"], encoding="utf-8")
        files.append(str(p))
    else:
        p = base / "README.md"
        p.write_text(f"# {project_name}\n\nGerado por App Factory v3.1 em {time.strftime('%Y-%m-%d')}.\n", encoding="utf-8")
        files.append(str(p))

    # Tree JSON
    tree = {"project": project_name, "base": str(base), "files": files, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")}
    p = base / "tree.json"
    p.write_text(json.dumps(tree, indent=2, ensure_ascii=False), encoding="utf-8")
    files.append(str(p))

    return {"project": project_name, "path": str(base), "files": files, "file_count": len(files)}


def generate_readme(project_name: str, stack: dict) -> str:
    """Gera README.md padrão."""
    return f"""# {project_name}

Gerado por App Factory v3.1.

## Stack
- Backend: {stack.get('backend', 'FastAPI + SQLAlchemy')}
- Database: {stack.get('database', 'PostgreSQL')}
- Frontend: {stack.get('frontend', 'HTML + Tailwind CDN')}

## Como rodar
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Ou via Docker:
```bash
docker-compose up
```

## Estrutura
```
backend/     — API FastAPI
frontend/    — HTML estático
db/          — Schema SQL + seed
tests/       — pytest
```
"""


if __name__ == "__main__":
    demo = {
        "schema_sql": "CREATE TABLE users (id UUID PRIMARY KEY);",
        "schema_pydantic": "from pydantic import BaseModel\nclass User(BaseModel): id: str",
        "api_main": "from fastapi import FastAPI\napp = FastAPI()",
        "frontend_html": "<html><body>Hello</body></html>",
        "requirements": ["fastapi", "uvicorn"],
        "dockerfile": "FROM python:3.12-slim\nWORKDIR /app",
        "docker_compose": "version: '3.8'\nservices:\n  api:\n    build: .",
    }
    result = render_project("demo_app", demo)
    print(json.dumps(result, indent=2))
