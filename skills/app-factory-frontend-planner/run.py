#!/usr/bin/env python3
"""
app-factory-frontend-planner
Planeja interface de usuario.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Frontend Planner")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="frontend_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    product = data.get("product_name", "product")

    if args.dry_run:
        result = {
            "frontend_plan": f"artifacts/frontend/{product}-frontend-plan.md",
            "pages": [
                {"route": "/", "name": "Home", "components": ["Header", "Hero"], "apis": []},
                {"route": "/dashboard", "name": "Dashboard", "components": ["Sidebar", "StatsCard"], "apis": ["GET /api/stats"]}
            ],
            "components": ["Header", "Sidebar", "Button", "Form", "StatsCard"],
            "user_journeys": ["Login -> Dashboard -> Criar Pedido -> Confirmacao"],
            "dry_run": True,
            "next_action": "Prosseguir para app-factory-test-oracle",
        }
    else:
        result = {
            "frontend_plan": f"artifacts/frontend/{product}-frontend-plan.md",
            "pages": [],
            "components": [],
            "user_journeys": [],
            "dry_run": False,
            "next_action": "Analisar PRD e API contract",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
