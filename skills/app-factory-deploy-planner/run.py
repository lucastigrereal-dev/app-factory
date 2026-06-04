#!/usr/bin/env python3
"""
app-factory-deploy-planner
Gera plano de deploy completo.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Deploy Planner")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="deploy_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    stack = data.get("stack", {})
    env = data.get("environment", "preview")

    if args.dry_run:
        result = {
            "deploy_plan": f"1. Build\n2. Test\n3. Deploy to {env}",
            "github_actions": "artifacts/deploy/.github/workflows/deploy.yml",
            "dockerfile": "artifacts/deploy/Dockerfile",
            "vercel_json": "artifacts/deploy/vercel.json",
            "env_vars": [
                {"name": "NEXT_PUBLIC_API_URL", "required": True, "secret": False},
                {"name": "DATABASE_URL", "required": True, "secret": True}
            ],
            "rollback_plan": "1. Reverter deploy\n2. Restaurar backup",
            "estimated_time": "15 min",
            "dry_run": True,
            "next_action": "Prosseguir para app-factory-handoff",
        }
    else:
        result = {
            "deploy_plan": f"Deploy real para {env} em execução",
            "github_actions": "",
            "dockerfile": "",
            "vercel_json": "",
            "env_vars": [],
            "rollback_plan": "",
            "estimated_time": "Calculando...",
            "dry_run": False,
            "next_action": "Executar deploy",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
