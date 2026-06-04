"""
Testes de fumaça para app-factory-master
"""

import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
RUN_PY = SKILL_DIR / "run.py"


def test_run_py_exists():
    """Skill deve ter run.py"""
    assert RUN_PY.exists(), "run.py não encontrado"


def test_main_runs_dry_run():
    """Dry-run deve completar sem erro"""
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--intention", "criar um crm", "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    assert result.returncode == 0, f"Erro: {result.stderr}"
    output = json.loads(result.stdout)
    assert output["status"] == "completed"
    assert output["dry_run"] is True
    assert len(output["completed_states"]) == 15  # todas as states


def test_output_schema():
    """Output deve conter campos obrigatórios"""
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--intention", "teste", "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    output = json.loads(result.stdout)
    required = ["status", "current_state", "completed_states", "pending_states",
                "squads_invoked", "artifacts", "risks", "next_action"]
    for key in required:
        assert key in output, f"Campo obrigatório faltando: {key}"
