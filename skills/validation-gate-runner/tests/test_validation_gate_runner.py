"""Smoke tests for validation-gate-runner."""
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
RUN_PY = SKILL_DIR / "run.py"
FIXTURE = SKILL_DIR / "tests" / "fixture.json"


def setup_module():
    FIXTURE.write_text(json.dumps({"gate_id": "CP-1", "artifact_path": "docs/PRD.md"}, ensure_ascii=False), encoding="utf-8")


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
    assert "report" in output


def test_output_schema():
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(FIXTURE), "--dry-run"],
        capture_output=True, text=True, cwd=str(SKILL_DIR)
    )
    output = json.loads(result.stdout)
    report = output["report"]
    for key in ["gate_id", "artifact", "checks", "overall", "dry_run"]:
        assert key in report, f"missing {key}"
    assert "next_action" in output
