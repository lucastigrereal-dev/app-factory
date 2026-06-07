import json
from pathlib import Path


def test_scaffold_plan_schema_exists_and_loads():
    schema_path = Path(__file__).resolve().parents[2] / "schemas" / "scaffold_plan_schema.json"
    assert schema_path.exists(), f"Scaffold plan schema missing: {schema_path}"
    with open(schema_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "required" in data and isinstance(data["required"], list)
    assert "properties" in data and isinstance(data["properties"], dict)