"""Testes de fumaça para app-factory-test-oracle."""

import json
import subprocess
import sys
from pathlib import Path

RUN_PY = Path(__file__).parent.parent / "run.py"
FIXTURES = Path(__file__).parent / "fixtures"


def test_run_py_exists():
    assert RUN_PY.exists(), "run.py não encontrado"


def test_dry_run_outputs_tests():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input.json"
    input_file.write_text(json.dumps({
        "prd_path": "artifacts/prd/output.md",
        "blueprint_path": "artifacts/blueprint/output.md",
        "api_contract_yaml": "artifacts/api/api_contract.yaml",
        "frontend_plan": "artifacts/frontend/frontend-plan.md",
        "product_name": "test-app"
    }), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    output = json.loads(result.stdout)
    assert "test_plan" in output
    assert "unit_tests" in output
    assert "integration_tests" in output
    assert "e2e_tests" in output
    assert "coverage_estimate" in output


def test_output_schema():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input2.json"
    input_file.write_text(json.dumps({"product_name": "x"}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    output = json.loads(result.stdout)
    required = ["test_plan", "unit_tests", "integration_tests", "e2e_tests", "coverage_estimate", "critical_gaps", "next_action"]
    for key in required:
        assert key in output, f"Campo faltando: {key}"
