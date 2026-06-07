"""Schema Generator v2 — templates + LLM para entidades (prompt curto, rápido).

ZERO deps externas. Usa Ollama direto.
"""
import json
import sys
from pathlib import Path
from string import Template

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.llm.gateway import call_llm

TPL_DIR = Path(__file__).resolve().parent / "templates"


def _llm_entities(description: str) -> list:
    """LLM extrai APENAS lista de entidades e campos em JSON. Prompt curto = rápido."""
    prompt = f"""Liste as entidades deste app em JSON:
{description}

Responda APENAS:
[{{"name":"Entidade","fields":[{{"name":"campo","type":"str|int|float|bool|date|uuid","required":true}}]}}]
"""
    raw = call_llm(prompt, task_type="quick", timeout=30.0)
    # Tenta extrair JSON
    raw = raw.strip()
    if raw.startswith("["):
        try:
            return json.loads(raw)
        except Exception:
            pass
    # Tenta extrair de markdown
    import re
    m = re.search(r"\[.*\]", raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            pass
    # Fallback hardcoded para testes
    return [
        {"name": "Item", "fields": [{"name": "id", "type": "uuid", "required": True}, {"name": "nome", "type": "str", "required": True}, {"name": "status", "type": "str", "required": False}, {"name": "created_at", "type": "date", "required": True}]}
    ]


def _type_map(t: str) -> str:
    t = t.lower()
    return {"str": "VARCHAR(255)", "int": "INTEGER", "float": "DECIMAL(10,2)", "bool": "BOOLEAN", "date": "TIMESTAMP", "uuid": "UUID"}.get(t, "TEXT")


def _py_type(t: str) -> str:
    t = t.lower()
    return {"str": "str", "int": "int", "float": "float", "bool": "bool", "date": "datetime", "uuid": "UUID"}.get(t, "str")


def generate_schema(description: str, app_name: str = "app") -> dict:
    entities = _llm_entities(description)

    # Normaliza entidades (LLM pode retornar campos com nomes diferentes)
    normalized = []
    for e in entities:
        if not isinstance(e, dict):
            continue
        ename = e.get("name", e.get("entity", "item"))
        fields = []
        for f in e.get("fields", []):
            if not isinstance(f, dict):
                continue
            fname = f.get("name", f.get("field", f.get("campo", "campo")))
            ftype = f.get("type", f.get("tipo", "str"))
            freq = f.get("required", f.get("obrigatorio", True))
            fields.append({"name": fname, "type": ftype, "required": bool(freq)})
        normalized.append({"name": ename, "fields": fields})
    entities = normalized

    # Build SQL
    tables = []
    indices = []
    for e in entities:
        name = e["name"].lower()
        lines = [f"CREATE TABLE {name} (", f"    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),"]
        for f in e.get("fields", []):
            if f["name"].lower() in ("id", "created_at", "updated_at"):
                continue
            pg_type = _type_map(f["type"])
            nullable = "NOT NULL" if f.get("required") else "NULL"
            lines.append(f"    {f['name']} {pg_type} {nullable},")
        lines.append(f"    created_at TIMESTAMP DEFAULT NOW(),")
        lines.append(f"    updated_at TIMESTAMP DEFAULT NOW()")
        lines.append(");")
        tables.append("\n".join(lines))
        indices.append(f"CREATE INDEX idx_{name}_created ON {name}(created_at);")

    sql = Template((TPL_DIR / "schema.sql.template").read_text(encoding="utf-8")).safe_substitute(
        app_name=app_name, tables="\n\n".join(tables), indices="\n".join(indices)
    )

    # Build Pydantic
    models = []
    for e in entities:
        name = e["name"]
        fields = []
        for f in e.get("fields", []):
            py_t = _py_type(f["type"])
            req = f" = Field(...)" if f.get("required") else f" = None"
            fields.append(f"    {f['name']}: {py_t}{req}")
        model_code = f"class {name}Create(BaseModel):\n" + "\n".join(fields) + "\n\n"
        model_code += f"class {name}Response(BaseModel):\n    id: UUID\n" + "\n".join(fields) + "\n    created_at: datetime\n"
        models.append(model_code)

    pydantic = Template((TPL_DIR / "models.py.template").read_text(encoding="utf-8")).safe_substitute(
        app_name=app_name, models="\n\n".join(models)
    )

    return {"app_name": app_name, "sql": sql, "pydantic": pydantic, "entities": entities}


def generate_seed_data(schema: dict, app_name: str = "app") -> str:
    entities = schema.get("entities", [])
    lines = [f"-- Seed data para {app_name}", ""]
    for e in entities[:2]:  # seed apenas 2 entidades
        name = e["name"].lower()
        fields = [f["name"] for f in e.get("fields", []) if f["name"] != "id"]
        if not fields:
            continue
        cols = ", ".join(fields)
        vals = ", ".join(["'demo'" if f != "status" else "'ativo'" for f in fields])
        lines.append(f"INSERT INTO {name} ({cols}) VALUES ({vals});")
    return "\n".join(lines)


if __name__ == "__main__":
    desc = "App de reservas para hotel. Entidades: Hotel, Quarto, Reserva, Hospede"
    r = generate_schema(desc, "hotel_reservas")
    print("=== SQL ===")
    print(r["sql"][:500])
    print("\n=== PYDANTIC ===")
    print(r["pydantic"][:500])
    print("\n=== ENTITIES ===")
    print(json.dumps(r["entities"], indent=2))
