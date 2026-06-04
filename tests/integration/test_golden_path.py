"""
test_golden_path.py
-------------------

An integration smoke test for the App Factory golden path.  This test
exercises the pipeline from idea intake through PRD generation,
blueprint generation, scaffold planning and export.  At this stage the
test only ensures that the modules can be imported and invoked without
crashing; it does not perform full pipeline execution.

Future implementations should construct a realistic mission package,
call each module in sequence and assert that the expected files are
produced in dry‑run mode.
"""

import pytest


def test_golden_path_smoke() -> None:
    """Smoke test to verify that core modules exist and can be imported."""
    try:
        import src.governance.risk_classifier as rc
        import src.governance.gate_runner as gr
        import src.prd.prd_validator as pv
        import src.scaffold.scaffold_planner as sp
    except ImportError as exc:
        pytest.fail(f"Failed to import core modules: {exc}")

    # simple sanity calls
    rc.classify("read documentation")
    gate_runner = gr.GateRunner({})
    _ = gate_runner.gate_exists("GATE-01")
    planner = sp.ScaffoldPlanner()
    plan = planner.plan(["src/__init__.py", "README.md"])
    assert plan["dry_run"] is True