"""Testes de fumaça para app-factory-discovery."""

import json
import subprocess
import sys
from pathlib import Path

RUN_PY = Path(__file__).parent.parent / "run.py"
FIXTURES = Path(__file__).parent / "fixtures"


def test_run_py_exists():
    assert RUN_PY.exists(), "run.py não encontrado"


def test_dry_run_completes():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input.json"
    input_file.write_text(json.dumps({
        "intention": "Criar app de delivery",
        "market_context": "Natal/RN",
        "budget": "R$2000",
        "timeline": "2 semanas",
        "target_users": ["hóspedes"]
    }), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    output = json.loads(result.stdout)
    assert output["go"] in [True, False]
    assert 0 <= output["confidence"] <= 1
    assert "next_action" in output


def test_output_schema():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input2.json"
    input_file.write_text(json.dumps({"intention": "x"}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    output = json.loads(result.stdout)
    required = ["go", "confidence", "problem_statement", "competitors", "risks", "alternatives", "next_action"]
    for key in required:
        assert key in output, f"Campo faltando: {key}"
