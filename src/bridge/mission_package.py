"""MissionPackage model and helpers.

This module defines a simple dataclass for mission packages and helper
functions to load and save mission packages from/to JSON files. The
dataclass includes a flag ``is_dry_run`` to indicate that the mission
is being processed in simulation mode only. All functions avoid side
effects by design; they never write outside of the specified paths.

Example:

    pkg = load_mission_package("examples/mission_package.json")
    # inspect fields
    pkg.title
    # modify and save
    save_mission_package(pkg, "examples/mission_package_copy.json")
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Any, Dict


@dataclass
class MissionPackage:
    """Container for mission intake data.

    Attributes:
        id: Unique identifier of the mission.
        title: A short summary of the mission.
        description: Detailed description of the mission/problem.
        sector: Optional business sector associated with the mission.
        priority: Priority score (0–3) indicating urgency.
        created_at: Timestamp of package creation (ISO format).
        metadata: Additional free‑form metadata.
        is_dry_run: Indicates if the mission is processed in dry‑run mode.
    """

    title: str
    description: str
    sector: Optional[str] = None
    priority: int = 1
    metadata: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    is_dry_run: bool = True


def load_mission_package(path: str) -> MissionPackage:
    """Load a MissionPackage from a JSON file.

    Args:
        path: Path to a JSON file containing mission data.

    Returns:
        MissionPackage: Parsed package.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If required fields are missing.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Validate required fields
    if not data.get("title") or not data.get("description"):
        raise ValueError("MissionPackage must contain 'title' and 'description'")
    # Build and return dataclass
    return MissionPackage(
        title=data["title"],
        description=data["description"],
        sector=data.get("sector"),
        priority=data.get("priority", 1),
        metadata=data.get("metadata", {}),
        id=data.get("id", str(uuid.uuid4())),
        created_at=data.get("created_at", datetime.utcnow().isoformat()),
        is_dry_run=data.get("is_dry_run", True),
    )


def save_mission_package(package: MissionPackage, path: str) -> None:
    """Save a MissionPackage to a JSON file.

    Args:
        package: The MissionPackage instance to save.
        path: Destination path where the JSON will be written.

    Raises:
        IOError: If the file cannot be written.
    """
    data = {
        "id": package.id,
        "title": package.title,
        "description": package.description,
        "sector": package.sector,
        "priority": package.priority,
        "metadata": package.metadata,
        "created_at": package.created_at,
        "is_dry_run": package.is_dry_run,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)