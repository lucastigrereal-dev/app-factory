import json
import os
import pytest

from bridge.mission_package import MissionPackage, load_mission_package, save_mission_package


def test_mission_package_load_and_save(tmp_path):
    # Prepare a sample mission JSON
    mission_data = {
        "title": "Teste de Missão",
        "description": "Descrição de teste",
        "sector": "financeiro",
        "priority": 2,
    }
    input_file = tmp_path / "mission.json"
    output_file = tmp_path / "mission_out.json"
    with open(input_file, "w", encoding="utf-8") as f:
        json.dump(mission_data, f)
    # Load mission package
    pkg = load_mission_package(str(input_file))
    assert pkg.title == mission_data["title"]
    assert pkg.description == mission_data["description"]
    assert pkg.sector == mission_data["sector"]
    # is_dry_run should default to True when missing
    assert pkg.is_dry_run is True
    # Save and reload
    save_mission_package(pkg, str(output_file))
    assert output_file.exists()
    reloaded = load_mission_package(str(output_file))
    assert reloaded.title == pkg.title
    assert reloaded.is_dry_run is True


def test_mission_package_missing_fields(tmp_path):
    # Missing title should raise ValueError
    bad_data = {"description": "Sem título"}
    input_file = tmp_path / "bad.json"
    with open(input_file, "w", encoding="utf-8") as f:
        json.dump(bad_data, f)
    with pytest.raises(ValueError):
        load_mission_package(str(input_file))