#!/usr/bin/env python3
"""
create-dashboard
Gera pacote inicial para dashboard: PRD, blueprint, frontend plan, acceptance criteria.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create Dashboard Pack")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="dashboard_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    result = {
        "prd_path": "docs/dashboard_PRD.md",
        "blueprint_path": "templates/dashboard/product_blueprint.yaml",
        "frontend_plan": "docs/dashboard_frontend_plan.md",
        "acceptance_criteria": "docs/dashboard_acceptance_criteria.md",
        "widgets": ["grafico_barras", "grafico_linhas", "tabela"],
        "metrics": ["visitantes", "conversoes", "churn"],
        "dry_run": args.dry_run,
        "next_action": "Revisar PRD e blueprint antes de aprovar CP-1/CP-2",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
