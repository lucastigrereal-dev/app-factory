"""
Unit tests for the OMNIS bridge stub.
"""

import pytest
from src.bridge.omnis_bridge import dispatch_mission


def test_dispatch_mission_dry_run_logs_action(capsys):
    mission = {"id": "m123", "idea": "test mission"}
    record = dispatch_mission(mission, dry_run=True)
    assert record["status"] == "queued"
    captured = capsys.readouterr()
    assert "Would dispatch mission m123" in captured.out


def test_dispatch_mission_missing_keys_raises():
    with pytest.raises(ValueError):
        dispatch_mission({"id": "m123"}, dry_run=True)


def test_dispatch_mission_live_raises_not_implemented():
    mission = {"id": "m123", "idea": "live mission"}
    with pytest.raises(NotImplementedError):
        dispatch_mission(mission, dry_run=False)