import pytest

from src.governance.approval_gate import require_approval


def test_approval_gate_blocks_r3() -> None:
    with pytest.raises(PermissionError):
        require_approval("deploy", "R3", approved=False)


def test_approval_gate_allows_r3_if_approved() -> None:
    # Should not raise if approval is granted
    require_approval("deploy", "R3", approved=True)


def test_approval_gate_allows_lower_risks() -> None:
    # Non‑R3 actions should pass without approval
    require_approval("write docs", "R1", approved=False)