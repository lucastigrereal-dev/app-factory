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

    # Build resources code
    resources = []
    for r in routes:
        ename = r["entity"]
        elower = ename.lower()
        code = f"""
# {ename}
class {ename}Create(BaseModel):
    nome: str = Field(...)

class {ename}Response(BaseModel):
    id: UUID
    nome: str
    created_at: datetime

@app.get("/api/{elower}", response_model=List[{ename}Response])
def list_{elower}():
    return db.get("{elower}", [])

@app.post("/api/{elower}", response_model={ename}Response)
def create_{elower}(item: {ename}Create):
    new = {{"id": uuid4(), "nome": item.nome, "created_at": datetime.now()}}
    db.setdefault("{elower}", []).append(new)
    return new

@app.get("/api/{elower}/{{id}}", response_model={ename}Response)
def get_{elower}(id: UUID):
    for item in db.get("{elower}", []):
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="{ename} not found")

@app.put("/api/{elower}/{{id}}", response_model={ename}Response)
def update_{elower}(id: UUID, item: {ename}Create):
    for i, existing in enumerate(db.get("{elower}", [])):
        if existing["id"] == id:
            existing["nome"] = item.nome
            return existing
    raise HTTPException(status_code=404, detail="{ename} not found")

@app.delete("/api/{elower}/{{id}}")
def delete_{elower}(id: UUID):
    db["{elower}"] = [x for x in db.get("{elower}", []) if x["id"] != id]
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
        "requirements": ["fastapi", "uvicorn", "pydantic", "python-multipart"],
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
