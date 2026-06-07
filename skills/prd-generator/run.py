#!/usr/bin/env python3
"""
prd-generator
Gera PRD Markdown estruturado a partir de MissionPackage.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="PRD Generator")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="prd_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    mission = data.get("mission_package", {})
    intention = mission.get("description", "") or data.get("intention", "")

    prd = {
        "title": mission.get("title", "PRD Draft"),
        "sections": [
            "Visao",
            "Problema",
            "Solucao",
            "Requisitos Funcionais",
            "Requisitos Nao-Funcionais",
            "Metricas",
            "Riscos",
            "Cronograma",
        ],
        "status": "DRAFT",
        "intention_summary": intention,
    }

    result = {
        "prd": prd,
        "prd_path": "docs/PRD.md",
        "dry_run": args.dry_run,
        "next_action": "Revisar PRD com stakeholders e passar CP-1",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
