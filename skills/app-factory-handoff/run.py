#!/usr/bin/env python3
"""
app-factory-handoff
Empacota artefatos em prompt executável pro Claude Code.
"""

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Handoff")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="handoff_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    artifacts = data.get("artifacts", {})
    risks = data.get("risks", [])
    project = data.get("project_name", "projeto")

    if args.dry_run:
        result = {
            "handoff_package": f"artifacts/handoff/{project}.zip",
            "claude_code_prompt": f"CLAUDE_CODE_PROMPT_{project}.md",
            "execution_order": [
                {"step": 1, "action": "Setup", "time": "10min"},
                {"step": 2, "action": "Build", "time": "30min"},
                {"step": 3, "action": "Test", "time": "20min"},
            ],
            "gates": [
                {"checkpoint": "CP-8", "condition": "Build passando", "blocker": True}
            ],
            "estimated_total_time": "1h",
            "risks_summary": risks,
            "dry_run": True,
            "next_action": "Executar handoff no Claude Code",
        }
    else:
        result = {
            "handoff_package": f"artifacts/handoff/{project}_real.zip",
            "claude_code_prompt": f"CLAUDE_CODE_PROMPT_{project}_real.md",
            "execution_order": [],
            "gates": [],
            "estimated_total_time": "Calculando...",
            "risks_summary": risks,
            "dry_run": False,
            "next_action": "Gerar handoff real",
        }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
