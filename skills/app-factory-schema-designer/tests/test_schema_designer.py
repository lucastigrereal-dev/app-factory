"""Testes de fumaça para app-factory-schema-designer."""

import json
import subprocess
import sys
from pathlib import Path

RUN_PY = Path(__file__).parent.parent / "run.py"
FIXTURES = Path(__file__).parent / "fixtures"


def test_run_py_exists():
    assert RUN_PY.exists(), "run.py não encontrado"


def test_dry_run_outputs_schema():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input.json"
    input_file.write_text(json.dumps({
        "prd_path": "artifacts/prd/output.md",
        "blueprint_path": "artifacts/blueprint/output.md",
        "stack": {"database": "PostgreSQL"},
        "product_name": "test-app"
    }), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    output = json.loads(result.stdout)
    assert "schema_yaml" in output
    assert "entities" in output
    assert len(output["entities"]) > 0
    assert output["normalization"] == "3NF"


def test_output_schema():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input2.json"
    input_file.write_text(json.dumps({"product_name": "x"}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    output = json.loads(result.stdout)
    required = ["schema_yaml", "migrations_sql", "report", "entities", "normalization", "sensitive_fields", "next_action"]
    for key in required:
        assert key in output, f"Campo faltando: {key}"
