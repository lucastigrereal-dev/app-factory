"""Smoke tests for create-saas-mvp."""
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
RUN_PY = SKILL_DIR / "run.py"
FIXTURE = SKILL_DIR / "tests" / "fixture.json"


def setup_module():
    FIXTURE.write_text(json.dumps({"intention": "saas de tarefas com login e pagamento"}, ensure_ascii=False), encoding="utf-8")


def test_run_py_exists():
    assert RUN_PY.exists(), "run.py not found"


def test_dry_run_completes():
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(FIXTURE), "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    assert result.returncode == 0, result.stderr
    output = json.loads(result.stdout)
    assert output["dry_run"] is True
    assert "prd_path" in output


def test_output_schema():
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(FIXTURE), "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    output = json.loads(result.stdout)
    for key in ["prd_path", "blueprint_path", "frontend_plan", "backend_plan", "acceptance_criteria", "features", "stack", "next_action"]:
        assert key in output, f"missing {key}"
