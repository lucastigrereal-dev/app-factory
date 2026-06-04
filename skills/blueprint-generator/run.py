#!/usr/bin/env python3
"""
blueprint-generator
Gera blueprint tecnico a partir de PRD e contexto.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Blueprint Generator")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="blueprint_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    blueprint = {
        "modules": ["core", "api", "frontend", "auth", "database"],
        "architecture": "modular",
        "integrations": [],
        "database": {"type": "relational", "entities": ["user", "project"]},
        "ui_plan": {"pages": ["home", "dashboard"]},
        "test_requirements": ["unit", "integration", "e2e"],
        "notes": f"Blueprint para: {intention[:60]}...",
    }

    result = {
        "blueprint": blueprint,
        "blueprint_path": "docs/BLUEPRINT.md",
        "system_yaml_updated": args.dry_run is False,
        "dry_run": args.dry_run,
        "next_action": "Prosseguir para repo-scaffolder (requer aprovacao CP-2)",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
