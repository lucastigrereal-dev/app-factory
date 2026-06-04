import json
from pathlib import Path

from jsonschema import Draft7Validator


def test_handoff_report_schema_is_valid() -> None:
    """Ensure the handoff report schema is a valid JSON schema."""
    schema_path = Path(__file__).resolve().parents[2] / "schemas" / "handoff_report_schema.json"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    Draft7Validator.check_schema(schema)