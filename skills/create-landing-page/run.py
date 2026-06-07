#!/usr/bin/env python3
"""
create-landing-page
Gera template de landing page com blueprint, plano de frontend e criterios.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create Landing Page Template")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="landing_page_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    result = {
        "template_dir": "templates/landing_page/",
        "files": [
            "templates/landing_page/TEMPLATE_README.md",
            "templates/landing_page/product_blueprint.yaml",
            "templates/landing_page/frontend_plan.template.md",
            "templates/landing_page/acceptance_criteria.md",
        ],
        "sections": ["hero", "features", "call-to-action"],
        "dry_run": args.dry_run,
        "next_action": "Revisar template com marketing/design antes de CP-0",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
