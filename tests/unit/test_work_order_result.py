import json
import os
from bridge.work_order_result import WorkOrderResult, save_work_order_result


def test_work_order_result_save(tmp_path):
    result = WorkOrderResult(
        mission_id="123",
        status="success",
        outputs={"message": "ok"},
        errors=[],
        is_dry_run=True,
    )
    output_file = tmp_path / "result.json"
    save_work_order_result(result, str(output_file))
    assert output_file.exists()
    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["mission_id"] == "123"
    assert data["status"] == "success"
    assert data["outputs"] == {"message": "ok"}
    assert data["errors"] == []
    assert data["is_dry_run"] is True