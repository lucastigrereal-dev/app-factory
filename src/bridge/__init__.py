"""Bridge package for the System Creation OS.

This package contains abstractions for communicating with external services
and for representing mission packages and work order results. All bridges
operate in dry‑run mode by default; they never perform real network
operations or write to external systems without explicit approval.
"""

from .mission_package import MissionPackage, load_mission_package, save_mission_package
from .work_order_result import WorkOrderResult, save_work_order_result
from .omnis_bridge import OmnisBridge

__all__ = [
    "MissionPackage",
    "load_mission_package",
    "save_mission_package",
    "WorkOrderResult",
    "save_work_order_result",
    "OmnisBridge",
]