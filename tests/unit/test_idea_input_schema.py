import json
from pathlib import Path

from jsonschema import Draft7Validator


def test_idea_input_schema_is_valid() -> None:
    """Ensure the idea input schema is a valid JSON schema."""
    schema_path = Path(__file__).resolve().parents[2] / "schemas" / "idea_input_schema.json"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    # This will raise an exception if the schema is invalid
    Draft7Validator.check_schema(schema)