#!/usr/bin/env python3
"""
repo-scaffolder
Gera estrutura de diretorios e placeholders a partir do blueprint.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Repo Scaffolder")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="scaffold_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    modules = data.get("blueprint", {}).get("modules", ["core", "api", "frontend"])
    structure = {}
    for mod in modules:
        structure[mod] = ["__init__.py", "README.md", "TODO.md"]

    result = {
        "structure": structure,
        "base_dir": "src/",
        "manifest_updated": args.dry_run is False,
        "dry_run": args.dry_run,
        "next_action": "Revisar estrutura com arquitetura e passar CP-3",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
