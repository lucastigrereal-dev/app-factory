import pytest

from src.governance.cost_tracker import CostTracker


def test_cost_tracker_accumulates() -> None:
    tracker = CostTracker()
    tracker.record_cost(1.5)
    tracker.record_cost(2.0)
    assert tracker.total == 3.5


def test_negative_cost_raises() -> None:
    tracker = CostTracker()
    with pytest.raises(ValueError):
        tracker.record_cost(-1.0)