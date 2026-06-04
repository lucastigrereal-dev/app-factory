"""
KRATOS status API stub.

This module exposes a function that returns the current build state for consumption
by the KRATOS cockpit.  It operates in dry‑run mode by default and does not
perform any external calls.
"""

from pathlib import Path
from typing import Any, Dict


def get_status(dry_run: bool = True) -> Dict[str, Any]:
    """Return a status snapshot of the System Creation OS.

    Parameters
    ----------
    dry_run: bool, optional
        When True (default), the function returns static data based on the
        SYSTEM_STATE.md file.  When False, this function would normally fetch
        real‑time status from running services (not implemented).

    Returns
    -------
    dict
        A dictionary containing the state summary and timestamp.
    """
    state_file = Path(__file__).resolve().parents[3] / "SYSTEM_STATE.md"
    if dry_run:
        # Read the SYSTEM_STATE.md file and extract the general status line.
        try:
            content = state_file.read_text(encoding="utf-8")
            first_line = content.splitlines()[0].strip()
            status_summary = first_line
        except Exception:
            status_summary = "Unknown (unable to read SYSTEM_STATE.md)"
        return {
            "state": status_summary,
            "timestamp": None,
            "dry_run": True,
        }
    else:
        # In a real implementation, gather live status from databases, queues,
        # and external integrations.  For now, raise NotImplementedError.
        raise NotImplementedError("Live status retrieval is not implemented")