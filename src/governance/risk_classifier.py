"""
risk_classifier.py
-------------------

This module provides a simple risk classification helper for the System Creation OS.
Risk levels are defined in SYSTEM_CANON.md and config/risk_policy.yaml.  The
classifier here should be extended to enforce those policies at runtime.  It
exposes a single function, ``classify``, which accepts a description of an
action and returns an appropriate risk level (``R0``–``R3``).

Usage:
    from governance.risk_classifier import classify
    risk = classify(action="create prd document")

The current implementation is intentionally conservative: it treats any
action containing keywords such as "deploy" or "push" as high risk (R3).
Developers should extend the keywords and logic based on real policies.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, Any


class RiskLevel(str, Enum):
    """Enumeration of risk levels used in the App Factory."""

    R0 = "R0"  # Safe — no side effects
    R1 = "R1"  # Low — reversible and internal
    R2 = "R2"  # Medium — potentially modifies state, requires dry_run
    R3 = "R3"  # High — irreversible or external, requires human approval


KEYWORDS_RISK: Dict[str, RiskLevel] = {
    "deploy": RiskLevel.R3,
    "push": RiskLevel.R3,
    "delete": RiskLevel.R3,
    "overwrite": RiskLevel.R3,
    "scaffold": RiskLevel.R2,
    "create": RiskLevel.R1,
    "generate": RiskLevel.R1,
    "update": RiskLevel.R2,
}


def classify(action: str) -> RiskLevel:
    """Classify an action string into one of the risk levels.

    Args:
        action: A short phrase describing the action to be taken, e.g.
            "scaffold project", "deploy to production".

    Returns:
        RiskLevel: the assessed risk level.

    Notes:
        This classifier uses a simple keyword heuristic.  It should be
        replaced by a more comprehensive parser that reads config/risk_policy.yaml.
    """
    if not action:
        return RiskLevel.R0
    lowered = action.lower()
    for keyword, level in KEYWORDS_RISK.items():
        if keyword in lowered:
            return level
    return RiskLevel.R0


__all__ = ["RiskLevel", "classify"]