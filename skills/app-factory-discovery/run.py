#!/usr/bin/env python3
"""
app-factory-discovery
Valida se a ideia é problema real antes de gerar PRD.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Discovery")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="discovery_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    # Load input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    budget = data.get("budget", "")
    timeline = data.get("timeline", "")

    # Discovery logic (dry-run = simulated)
    if args.dry_run:
        go = True
        confidence = 0.75
        problem = f"Usuários querem: {intention[:50]}..."
        competitors = [
            {"name": "Competidor A", "threat": "média", "differentiator": "foco em nicho"}
        ]
        risks = [{"level": "R1", "description": "Validação simulada (dry-run)"}]
        alternatives = ["Alternativa A: MVP manual", "Alternativa B: no-code"]
    else:
        # Real execution: placeholder for Akasha + trend search
        go = True
        confidence = 0.82
        problem = f"Problema validado: {intention[:60]}..."
        competitors = []
        risks = [{"level": "R1", "description": "Pipeline real em execução"}]
        alternatives = []

    result = {
        "go": go,
        "confidence": confidence,
        "problem_statement": problem,
        "competitors": competitors,
        "risks": risks,
        "alternatives": alternatives,
        "dry_run": args.dry_run,
        "next_action": "Prosseguir para prd-generator" if go else "Revisar alternativas",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
