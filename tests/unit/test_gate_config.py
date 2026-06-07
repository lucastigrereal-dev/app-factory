import yaml
from pathlib import Path


def test_gates_config_loads_and_has_sections():
    gates_path = Path(__file__).resolve().parents[2] / "config" / "gates.yaml"
    assert gates_path.exists(), "config/gates.yaml missing"
    with open(gates_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "gates.yaml should be a dict"
    # Basic sanity: check presence of at least one stage gate definition
    assert any(isinstance(v, dict) for v in data.values()), "No gate definitions found"