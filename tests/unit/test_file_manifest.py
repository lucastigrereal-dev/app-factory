import yaml
from pathlib import Path


def test_file_manifest_loads_and_has_entries():
    manifest_path = Path(__file__).resolve().parents[2] / "FILE_MANIFEST.yaml"
    assert manifest_path.exists(), "FILE_MANIFEST.yaml missing"
    with open(manifest_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "Manifest should be a dict"
    assert data, "Manifest is empty"
    # Ensure that each entry has at least a description and a status
    for path, info in data.items():
        assert "purpose" in info, f"{path} missing purpose"
        assert "status" in info, f"{path} missing status"