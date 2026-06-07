"""
scaffold_planner.py
-------------------

This module defines a planner responsible for generating scaffold plans
without executing them.  A scaffold plan is a structured representation
of the file tree and diff preview that would be produced when scaffolding
a project.  The plan is serialised according to the JSON schema
defined in ``schemas/scaffold_plan_schema.json``.

The ``ScaffoldPlanner`` below exposes a simple interface that accepts
a list of files and directories and generates a nested plan.  Real
implementations should integrate with the blueprint, API contracts,
database schema and templates to compute a comprehensive plan.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Union


class ScaffoldPlanner:
    """Plan a scaffold operation without side effects."""

    def __init__(self, dry_run: bool = True, risk_level: str = "R2") -> None:
        self.dry_run = dry_run
        self.risk_level = risk_level

    def generate_file_tree(self, paths: List[Union[str, Path]]) -> List[Dict[str, any]]:
        """Generate a hierarchical file tree from a flat list of file paths.

        Args:
            paths: A list of file or directory paths relative to the project root.

        Returns:
            A nested list representing the file tree.  Each entry has
            ``path`` and ``type``, and directories have a ``children`` key.
        """
        tree: List[Dict[str, any]] = []
        for path in sorted(map(str, paths)):
            parts = path.split("/")
            self._insert_path(tree, parts)
        return tree

    def _insert_path(self, tree: List[Dict[str, any]], parts: List[str]) -> None:
        """Recursively insert a path into the tree."""
        if not parts:
            return
        current = parts[0]
        rest = parts[1:]
        # Find or create node
        node = next((n for n in tree if n["path"] == current), None)
        if node is None:
            node = {"path": current, "type": "directory" if rest else "file"}
            tree.append(node)
        if rest:
            node.setdefault("children", [])
            self._insert_path(node["children"], rest)

    def plan(self, files_to_create: List[Union[str, Path]]) -> Dict[str, any]:
        """Construct a scaffold plan for the given list of files.

        Args:
            files_to_create: A list of relative file paths that would be
                created by the scaffold operation.

        Returns:
            A dictionary matching the ScaffoldPlan schema.
        """
        file_tree = self.generate_file_tree(files_to_create)
        diff_preview = "\n".join(f"ADD {path}" for path in files_to_create)
        return {
            "dry_run": self.dry_run,
            "file_tree": file_tree,
            "diff_preview": diff_preview,
            "risk_level": self.risk_level,
        }

    def save_plan(self, plan: Dict[str, any], output_path: Union[str, Path]) -> None:
        """Save a scaffold plan to a JSON file."""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)


__all__ = ["ScaffoldPlanner"]