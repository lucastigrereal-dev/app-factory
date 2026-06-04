import json
import os
from bridge.mission_package import load_mission_package, save_mission_package, MissionPackage
from bridge.work_order_result import WorkOrderResult, save_work_order_result


def test_bridge_flow_dry_run(tmp_path):
    # Create mission data
    mission_data = {"title": "Integração", "description": "Teste de integração"}
    mission_path = tmp_path / "mission.json"
    result_path = tmp_path / "result.json"
    # Save mission package
    mission_pkg = MissionPackage(title=mission_data["title"], description=mission_data["description"])
    save_mission_package(mission_pkg, str(mission_path))
    # Load again to simulate reading from disk
    loaded = load_mission_package(str(mission_path))
    # Create work order result using mission id
    result = WorkOrderResult(mission_id=loaded.id, status="dry_run", outputs={"checked": True}, errors=[], is_dry_run=True)
    save_work_order_result(result, str(result_path))
    assert result_path.exists()
    # Verify saved result references correct mission_id
    with open(result_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["mission_id"] == loaded.id
    assert data["is_dry_run"] is True