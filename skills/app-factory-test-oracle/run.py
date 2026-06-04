#!/usr/bin/env python3
"""
app-factory-test-oracle
Gera plano de testes completo.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Test Oracle")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="test_output.json", help="Output file")
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
            "test_plan": f"artifacts/test/{product}-test-plan.md",
            "unit_tests": [
                {"target": "OrderService.create", "cases": ["pedido valido", "pedido sem itens", "usuario inativo"], "expected": "criar|rejeitar|rejeitar"}
            ],
            "integration_tests": [
                {"target": "POST /api/orders", "cases": ["fluxo completo", "auth invalido"], "expected": "201|401"}
            ],
            "e2e_tests": [
                {"target": "Login -> Dashboard -> Criar Pedido", "cases": ["happy path", "timeout"], "expected": "sucesso|erro"}
            ],
            "coverage_estimate": "85%",
            "critical_gaps": [],
            "dry_run": True,
            "next_action": "Prosseguir para repo-scaffolder",
        }
    else:
        result = {
            "test_plan": f"artifacts/test/{product}-test-plan.md",
            "unit_tests": [],
            "integration_tests": [],
            "e2e_tests": [],
            "coverage_estimate": "Calculando...",
            "critical_gaps": [],
            "dry_run": False,
            "next_action": "Analisar PRD e blueprint",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
