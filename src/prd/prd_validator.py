"""
prd_validator.py
----------------

Provides a simple validator for PRD JSON documents according to
``schemas/prd_output_schema.json``.  This module relies on the
``jsonschema`` library to perform validation.  Validation errors will be
raised as ``jsonschema.exceptions.ValidationError``.

Example usage::

    from prd.prd_validator import validate_prd
    with open("sample_prd.json") as f:
        data = json.load(f)
    validate_prd(data)

This skeleton is minimal and should be extended to integrate with the
factory's gate system and provide better error reporting.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

try:
    from jsonschema import validate as json_validate
    from jsonschema import Draft7Validator
except ImportError as exc:
    raise RuntimeError(
        "jsonschema package is required for PRD validation; install via pip"
    ) from exc


def load_schema(schema_path: str) -> Dict[str, Any]:
    """Load a JSON schema from disk."""
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_prd(prd_data: Dict[str, Any], schema_path: str | Path | None = None) -> None:
    """Validate a PRD against the PRD output schema.

    Args:
        prd_data: The PRD data to validate.
        schema_path: Optional path to the PRD JSON schema.  If omitted,
            ``schemas/prd_output_schema.json`` relative to the package root is used.

    Raises:
        jsonschema.exceptions.ValidationError: If the PRD does not conform
            to the schema.
    """
    if schema_path is None:
        # Resolve default schema relative to this file
        base_dir = Path(__file__).resolve().parents[2]
        schema_path = base_dir / "schemas" / "prd_output_schema.json"
    schema = load_schema(str(schema_path))
    json_validate(instance=prd_data, schema=schema)


__all__ = ["validate_prd"]