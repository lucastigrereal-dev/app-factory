"""Approval gate for high‑risk actions.

This module defines a helper that enforces human approval for risk level R3
operations.  Other modules should call :func:`require_approval` before
performing any action that interacts with external systems or modifies
production state.
"""

def require_approval(action_name: str, risk: str, approved: bool = False) -> None:
    """Enforce that R3 actions cannot proceed without approval.

    Args:
        action_name: Name of the action being performed (for logging).
        risk: Risk level of the action (e.g. "R0", "R1", "R2", "R3").
        approved: Whether the human operator has granted approval.

    Raises:
        PermissionError: If `risk` is "R3" and `approved` is False.
    """
    if risk == "R3" and not approved:
        raise PermissionError(f"Approval required for R3 action: {action_name}")