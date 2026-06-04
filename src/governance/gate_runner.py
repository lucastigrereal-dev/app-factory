"""
gate_runner.py
---------------

This module defines a minimal gate runner for the System Creation OS.  Gates
are checkpoints described in config/gates.yaml and docs/ENTERPRISE_QUALITY_GATES.md.
Each gate has an input, output, automatic and manual checks, and a risk level.
The GateRunner class reads the YAML configuration and performs the automatic
checks.  Manual checks must be performed by a human reviewer.

This skeleton outlines the expected interface.  The actual implementation
should load YAML, validate schema and run user-defined checks.  For now it
only stores gate definitions and provides a method to evaluate whether a
gate is defined for a given name.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Gate:
    """Representation of a quality gate definition."""

    name: str
    input: str
    output: str
    risk: str
    description: Optional[str] = None


class GateRunner:
    """Simple gate runner that loads gate definitions and checks them."""

    def __init__(self, gates: Dict[str, Gate]):
        self.gates = gates

    @classmethod
    def from_yaml(cls, yaml_path: str) -> "GateRunner":
        """Construct a GateRunner by parsing a YAML file.

        Args:
            yaml_path: Path to a YAML file defining gates.

        Returns:
            GateRunner instance with gates loaded.
        """
        try:
            import yaml
        except ImportError as exc:
            raise RuntimeError("PyYAML is required to load gate definitions") from exc
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        gates: Dict[str, Gate] = {}
        for item in data.get("gates", []):
            gates[item["name"]] = Gate(
                name=item["name"],
                input=item.get("input", ""),
                output=item.get("output", ""),
                risk=item.get("risk", "R0"),
                description=item.get("description"),
            )
        return cls(gates)

    def gate_exists(self, name: str) -> bool:
        """Check if a gate with the given name is defined."""
        return name in self.gates

    def run_gate(self, name: str, context: Optional[Dict] = None) -> bool:
        """Run a gate's automatic check.

        Args:
            name: Name of the gate to run.
            context: Optional context dictionary with values needed to
                evaluate the gate (e.g. file paths, scores).

        Returns:
            bool: True if the gate passes automatically, False otherwise.

        Note:
            This dummy implementation always returns True.  Replace this with
            actual logic referencing context and gate definitions.
        """
        if name not in self.gates:
            raise KeyError(f"Gate '{name}' is not defined")
        # TODO: implement real automatic checks
        return True


__all__ = ["Gate", "GateRunner"]