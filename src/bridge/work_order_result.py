"""WorkOrderResult model and helpers.

This module defines a dataclass representing the result of executing
a work order. A work order is a unit of work generated from a mission
specification (workflow, integration, etc.). The result contains status,
outputs, error messages and a dry‑run flag. All writes are confined to
paths specified by the caller, and no external side effects are performed.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class WorkOrderResult:
    """Result of a work order execution.

    Attributes:
        mission_id: Identifier of the mission associated with this result.
        status: Execution status ("success", "failure", "dry_run").
        outputs: Dictionary of outputs produced by the work order.
        errors: List of error messages, if any.
        is_dry_run: Indicates if the work order was executed in dry‑run mode.
    """

    mission_id: str
    status: str
    outputs: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    is_dry_run: bool = True


def save_work_order_result(result: WorkOrderResult, path: str) -> None:
    """Persist a WorkOrderResult as JSON to a file.

    Args:
        result: The work order result to save.
        path: Destination file path.

    Raises:
        IOError: If the file cannot be written.
    """
    data = {
        "mission_id": result.mission_id,
        "status": result.status,
        "outputs": result.outputs,
        "errors": result.errors,
        "is_dry_run": result.is_dry_run,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)