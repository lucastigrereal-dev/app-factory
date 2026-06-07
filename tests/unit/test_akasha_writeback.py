"""
Unit tests for the AKASHA writeback stub.
"""

import pytest
from src.memory_writeback.akasha_writeback import writeback_event


def test_writeback_event_dry_run_logs_action(capsys):
    event = {
        "id": "e123",
        "mission_id": "m123",
        "timestamp": "2026-06-04T00:00:00Z",
        "event_type": "handoff",
    }
    record = writeback_event(event, dry_run=True)
    assert record["status"] == "logged"
    captured = capsys.readouterr()
    assert "Would writeback event e123" in captured.out


def test_writeback_event_missing_keys_raises():
    with pytest.raises(ValueError):
        writeback_event({"id": "e123"}, dry_run=True)


def test_writeback_event_live_raises_not_implemented():
    event = {
        "id": "e123",
        "mission_id": "m123",
        "timestamp": "2026-06-04T00:00:00Z",
        "event_type": "handoff",
    }
    with pytest.raises(NotImplementedError):
        writeback_event(event, dry_run=False)