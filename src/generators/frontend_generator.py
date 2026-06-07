"""Frontend Generator v2 — templates hardcoded + LLM para layout.

ZERO deps externas.
"""
import json
import sys
from pathlib import Path
from string import Template

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.llm.gateway import call_llm

TPL_DIR = Path(__file__).resolve().parent / "templates"


def _llm_dashboard_data(entities: list) -> dict:
    """LLM gera titulos/cards/mock data para dashboard."""
    prompt = f"""Para estas entidades:
{json.dumps([e['name'] for e in entities])}

Responda JSON:
{{"cards":[{{"title":"Total X","value":"42","color":"blue"}}],"table_title":"Lista","mock":[{{"nome":"Demo","status":"Ativo"}}]}}
"""
    raw = call_llm(prompt, task_type="quick", timeout=15.0)
    import re
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            pass
    return {
        "cards": [{"title": f"Total {e['name']}", "value": "0", "color": "blue"} for e in entities[:3]],
        "table_title": entities[0]["name"] + "s",
        "mock": [{"nome": "Exemplo", "status": "Ativo"}],
    }


def generate_frontend(description: str, app_name: str = "app", stack: str = "html", entities: list = None) -> dict:
    if not entities:
        entities = [{"name": "Item"}]

    dash = _llm_dashboard_data(entities)

    nav_items = "\n".join([f'        <a href="#" class="block py-2 px-3 rounded hover:bg-gray-800">{e["name"]}s</a>' for e in entities[:4]])
    cards = "\n".join([f'      <div class="bg-white rounded-xl shadow p-6"><p class="text-gray-500 text-sm">{c["title"]}</p><p class="text-3xl font-bold">{c["value"]}</p></div>' for c in dash["cards"][:3]])
    mock_list = dash.get("mock", [{"nome": "Exemplo", "status": "Ativo"}])
    if not isinstance(mock_list, list) or len(mock_list) == 0:
        mock_list = [{"nome": "Exemplo", "status": "Ativo"}]
    headers = "\n".join([f'<th class="text-left py-2">{k.capitalize()}</th>' for k in mock_list[0].keys()])

    html = Template((TPL_DIR / "frontend.html.template").read_text(encoding="utf-8")).safe_substitute(
        app_name=app_name,
        nav_items=nav_items,
        cards=cards,
        table_title=dash["table_title"],
        table_headers=headers,
        mock_data=json.dumps(mock_list, ensure_ascii=False),
    )

    return {"app_name": app_name, "index_html": html, "app_js": "", "style_css": ""}


if __name__ == "__main__":
    entities = [{"name": "Tarefa"}, {"name": "Projeto"}]
    result = generate_frontend("Dashboard de tarefas", "taskapp", "html", entities)
    print("=== HTML (primeiras 20 linhas) ===")
    print("\n".join(result["index_html"].split("\n")[:20]))
