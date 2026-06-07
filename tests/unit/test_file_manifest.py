import yaml
from pathlib import Path


def test_file_manifest_loads_and_has_entries():
    manifest_path = Path(__file__).resolve().parents[2] / "FILE_MANIFEST.yaml"
    assert manifest_path.exists(), "FILE_MANIFEST.yaml missing"
    with open(manifest_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "Manifest should be a dict"
    assert "files" in data, "Manifest missing 'files' key"
    files = data["files"]
    assert files, "Manifest files list is empty"
    # Ensure that each entry has at least purpose, action and owner
    for info in files:
        path = info.get("path", "unknown")
        assert "purpose" in info, f"{path} missing purpose"
        assert "action" in info, f"{path} missing action"
        assert "owner" in info, f"{path} missing owner"