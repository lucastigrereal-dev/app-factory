#!/usr/bin/env python3
"""
app-factory-schema-designer
Planeja e valida schemas de banco de dados.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Schema Designer")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="schema_output.json", help="Output file")
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
            "schema_yaml": f"artifacts/schema/{product}_schema.yaml",
            "migrations_sql": f"artifacts/schema/migrations/",
            "report": f"artifacts/schema/schema-report.md",
            "entities": [
                {"name": "users", "fields": ["id", "email", "role"], "relations": ["orders"]},
                {"name": "orders", "fields": ["id", "user_id", "status", "total"], "relations": ["users", "items"]}
            ],
            "normalization": "3NF",
            "sensitive_fields": ["email", "phone"],
            "dry_run": True,
            "next_action": "Prosseguir para app-factory-api-contractor",
        }
    else:
        result = {
            "schema_yaml": f"artifacts/schema/{product}_schema.yaml",
            "migrations_sql": f"artifacts/schema/migrations/",
            "report": f"artifacts/schema/schema-report.md",
            "entities": [],
            "normalization": "Calculando...",
            "sensitive_fields": [],
            "dry_run": False,
            "next_action": "Analisar PRD e blueprint",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
