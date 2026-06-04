#!/usr/bin/env python3
"""
app-factory-api-contractor
Construi contratos de API OpenAPI.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory API Contractor")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="api_output.json", help="Output file")
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
            "api_contract_yaml": f"artifacts/api/{product}_api_contract.yaml",
            "report": f"artifacts/api/api-report.md",
            "endpoints": [
                {"method": "GET", "path": "/api/users", "auth": True, "status_codes": [200, 401]},
                {"method": "POST", "path": "/api/orders", "auth": True, "status_codes": [201, 400, 401]}
            ],
            "version": "1.0.0",
            "auth_scheme": "JWT Bearer",
            "dry_run": True,
            "next_action": "Prosseguir para app-factory-frontend-planner",
        }
    else:
        result = {
            "api_contract_yaml": f"artifacts/api/{product}_api_contract.yaml",
            "report": f"artifacts/api/api-report.md",
            "endpoints": [],
            "version": "1.0.0",
            "auth_scheme": "JWT Bearer",
            "dry_run": False,
            "next_action": "Analisar schema YAML",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
