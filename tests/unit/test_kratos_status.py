"""
Unit tests for the kratos_status API stub.
"""

import pytest
from src.api.kratos_status import get_status


def test_get_status_dry_run_returns_state_string():
    status = get_status(dry_run=True)
    assert isinstance(status["state"], str)
    assert status["dry_run"] is True


def test_get_status_live_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        get_status(dry_run=False)