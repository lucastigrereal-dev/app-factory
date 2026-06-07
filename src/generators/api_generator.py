"""API Generator v2 — templates hardcoded + LLM para JSON de endpoints.

ZERO deps externas.
"""
import json
import sys
from pathlib import Path
from string import Template

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.llm.gateway import call_llm

TPL_DIR = Path(__file__).resolve().parent / "templates"


def _llm_routes(entities: list) -> list:
    """LLM decide quais rotas CRUD cada entidade precisa."""
    prompt = f"""Para estas entidades:
{json.dumps([e['name'] for e in entities])}

Responda JSON com rotas:
[{{"entity":"Nome","routes":["GET /api/nome","POST /api/nome","GET /api/nome/{{id}}","PUT /api/nome/{{id}}","DELETE /api/nome/{{id}}"]}}]
"""
    raw = call_llm(prompt, task_type="quick", timeout=20.0)
    raw = raw.strip()
    import re
    m = re.search(r"\[.*\]", raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            pass
    # Fallback: todas entidades com CRUD completo
    return [{"entity": e["name"], "routes": [f"GET /api/{e['name'].lower()}", f"POST /api/{e['name'].lower()}", f"GET /api/{e['name'].lower()}/{{id}}", f"PUT /api/{e['name'].lower()}/{{id}}", f"DELETE /api/{e['name'].lower()}/{{id}}"]} for e in entities]


def generate_api(schema_pydantic: str, schema_sql: str, app_name: str = "app", entities: list = None) -> dict:
    if not entities:
        entities = []

    routes = _llm_routes(entities)

    # Build resources code using SQLAlchemy
    resources = []
    for r in routes:
        ename = r["entity"]
        elower = ename.lower()
        code = f"""
from sqlalchemy.orm import Session
from database import get_db
from models import {ename}
from auth import get_current_user
from fastapi import Depends

class {ename}Create(BaseModel):
    nome: str = Field(...)

class {ename}Response(BaseModel):
    id: UUID
    nome: str
    created_at: datetime

    class Config:
        orm_mode = True

@app.get("/api/{elower}", response_model=List[{ename}Response])
def list_{elower}(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return db.query({ename}).all()

@app.post("/api/{elower}", response_model={ename}Response)
def create_{elower}(item: {ename}Create, db: Session = Depends(get_db), user = Depends(get_current_user)):
    new = {ename}(nome=item.nome)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.get("/api/{elower}/{{id}}", response_model={ename}Response)
def get_{elower}(id: UUID, db: Session = Depends(get_db), user = Depends(get_current_user)):
    obj = db.query({ename}).filter({ename}.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="{ename} not found")
    return obj

@app.put("/api/{elower}/{{id}}", response_model={ename}Response)
def update_{elower}(id: UUID, item: {ename}Create, db: Session = Depends(get_db), user = Depends(get_current_user)):
    obj = db.query({ename}).filter({ename}.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="{ename} not found")
    obj.nome = item.nome
    db.commit()
    db.refresh(obj)
    return obj

@app.delete("/api/{elower}/{{id}}")
def delete_{elower}(id: UUID, db: Session = Depends(get_db), user = Depends(get_current_user)):
    obj = db.query({ename}).filter({ename}.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="{ename} not found")
    db.delete(obj)
    db.commit()
    return {{"ok": True}}
"""
        resources.append(code)

    main_py = Template((TPL_DIR / "fastapi_main.py.template").read_text(encoding="utf-8")).safe_substitute(
        app_name=app_name, resources="\n".join(resources)
    )

    return {
        "app_name": app_name,
        "main_py": main_py,
        "router_py": "# Routes incluidos em main.py para simplificar",
        "requirements": ["fastapi", "uvicorn", "pydantic", "python-multipart", "sqlalchemy", "psycopg2-binary", "python-jose[cryptography]", "passlib[bcrypt]"],
    }


def generate_dockerfile() -> str:
    return """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""


def generate_docker_compose(app_name: str = "app") -> str:
    return f"""version: '3.8'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: {app_name}
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: {app_name}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://{app_name}:secret@db:5432/{app_name}
    depends_on:
      - db

volumes:
  pgdata:
"""


if __name__ == "__main__":
    entities = [{"name": "Tarefa"}, {"name": "Projeto"}]
    result = generate_api("", "", "taskapp", entities)
    print("=== MAIN.PY (primeiras 30 linhas) ===")
    print("\n".join(result["main_py"].split("\n")[:30]))
