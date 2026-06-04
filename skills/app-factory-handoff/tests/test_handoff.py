"""Testes de fumaça para app-factory-handoff."""

import json
import subprocess
import sys
from pathlib import Path

RUN_PY = Path(__file__).parent.parent / "run.py"
FIXTURES = Path(__file__).parent / "fixtures"


def test_run_py_exists():
    assert RUN_PY.exists(), "run.py não encontrado"


def test_dry_run_outputs_handoff():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input.json"
    input_file.write_text(json.dumps({
        "artifacts": {"prd": "a.md", "blueprint": "b.md", "scaffold": "c/", "deploy_plan": "d.md"},
        "risks": [{"level": "R1", "description": "x"}],
        "project_name": "test-app",
        "stack": {"frontend": "Next.js"}
    }), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    output = json.loads(result.stdout)
    assert "handoff_package" in output
    assert "claude_code_prompt" in output
    assert "execution_order" in output
    assert len(output["execution_order"]) > 0


def test_output_schema():
    FIXTURES.mkdir(exist_ok=True)
    input_file = FIXTURES / "input2.json"
    input_file.write_text(json.dumps({"project_name": "x"}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(input_file), "--dry-run"],
        capture_output=True, text=True, cwd=str(RUN_PY.parent)
    )
    output = json.loads(result.stdout)
    required = ["handoff_package", "claude_code_prompt", "execution_order", "gates", "estimated_total_time", "next_action"]
    for key in required:
        assert key in output, f"Campo faltando: {key}"
