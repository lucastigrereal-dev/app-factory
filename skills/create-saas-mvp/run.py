#!/usr/bin/env python3
"""
create-saas-mvp
Gera pacote inicial para SaaS MVP: PRD, blueprint, frontend/backend plan, acceptance criteria.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create SaaS MVP Pack")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="saas_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    result = {
        "prd_path": "docs/saas_PRD.md",
        "blueprint_path": "templates/saas/product_blueprint.yaml",
        "frontend_plan": "docs/saas_frontend_plan.md",
        "backend_plan": "docs/saas_backend_plan.md",
        "acceptance_criteria": "docs/saas_acceptance_criteria.md",
        "features": ["auth", "billing", "crud_principal"],
        "stack": {"frontend": "Next.js", "backend": "Supabase"},
        "dry_run": args.dry_run,
        "next_action": "Revisar PRD e blueprint antes de aprovar CP-1/CP-2",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
