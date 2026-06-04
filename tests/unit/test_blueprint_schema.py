import json
from pathlib import Path


def test_blueprint_schema_exists_and_loads():
    schema_path = Path(__file__).resolve().parents[2] / "schemas" / "blueprint_schema.json"
    assert schema_path.exists(), f"Blueprint schema missing: {schema_path}"
    with open(schema_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Basic sanity: check required keys exist
    assert "required" in data and isinstance(data["required"], list)
    assert "properties" in data and isinstance(data["properties"], dict)