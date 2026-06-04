"""
Bridge to OMNIS Core (WAF‑01).

This module provides a stub implementation for dispatching missions from
OMNIS Core to the System Creation OS.  All operations are dry‑run by
default and merely log the actions that would be taken.
"""

from typing import Dict, Any


class OmnisBridge:
    """Thin wrapper around ``dispatch_mission`` for backwards compatibility."""

    @staticmethod
    def dispatch(mission: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
        return dispatch_mission(mission, dry_run)


def dispatch_mission(mission: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
    """Dispatch a mission from OMNIS Core to the App Factory.

    Parameters
    ----------
    mission: dict
        A mission object containing at least an `id` and `idea`.
    dry_run: bool, optional
        When True (default), the function logs the action without performing
        any external calls.

    Returns
    -------
    dict
        A record of the action taken or planned.
    """
    required_keys = {"id", "idea"}
    missing = required_keys - mission.keys()
    if missing:
        raise ValueError(f"Mission is missing required keys: {missing}")

    action = {
        "mission_id": mission["id"],
        "status": "queued" if dry_run else "dispatched",
        "dry_run": dry_run,
        "details": {
            "idea": mission["idea"],
        },
    }

    if dry_run:
        # Log the action; in a real implementation, insert into a queue or
        # call an API.
        print(f"[dry_run] Would dispatch mission {mission['id']} with idea: {mission['idea']}")
    else:
        # Placeholder for real dispatch logic.
        raise NotImplementedError("Mission dispatch is not implemented for live runs")

    return action