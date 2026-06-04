"""Smoke tests for blueprint-generator."""
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
RUN_PY = SKILL_DIR / "run.py"
FIXTURE = SKILL_DIR / "tests" / "fixture.json"


def setup_module():
    FIXTURE.write_text(json.dumps({"intention": "crm para hotel", "prd_path": "docs/PRD.md"}, ensure_ascii=False), encoding="utf-8")


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
    assert "blueprint" in output


def test_output_schema():
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(FIXTURE), "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    output = json.loads(result.stdout)
    assert "blueprint" in output
    assert "modules" in output["blueprint"]
    assert "next_action" in output
