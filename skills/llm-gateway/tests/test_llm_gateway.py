#!/usr/bin/env python3
"""Tests for llm-gateway"""
import subprocess, sys, json
from pathlib import Path

RUN_PY = Path(__file__).resolve().parent.parent / "run.py"

def test_run_py_exists():
    assert RUN_PY.is_file(), f"run.py not found at {RUN_PY}"

def test_dry_run_completes():
    fixture = Path(__file__).resolve().parent / "fixture.json"
    fixture.write_text(json.dumps({"intention": "test"}), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(fixture), "--dry-run"],
        capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0, f"dry_run failed: {result.stderr}"
    output = json.loads(result.stdout)
    assert output.get("status") == "success"
    assert output.get("dry_run") is True

def test_output_schema():
    fixture = Path(__file__).resolve().parent / "fixture.json"
    fixture.write_text(json.dumps({"intention": "test"}), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(fixture), "--output", "test_output.json", "--dry-run"],
        capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0
    out = Path("test_output.json")
    assert out.exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "status" in data
    assert "dry_run" in data
    out.unlink(missing_ok=True)
