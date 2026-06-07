#!/usr/bin/env python3
"""
app-intake
Transforma ideia bruta em MissionPackage padronizado.
"""

import argparse
import json
import sys
import uuid
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory Intake")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="intake_output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    client_id = data.get("client_id", "")

    mission = {
        "id": str(uuid.uuid4()),
        "title": intention[:80] if intention else "Untitled mission",
        "description": intention,
        "sector": data.get("sector") or None,
        "priority": data.get("priority", 1),
        "metadata": {"client_id": client_id, "type": data.get("type", "saas")},
        "created_at": datetime.utcnow().isoformat() + "Z",
        "is_dry_run": args.dry_run,
    }

    result = {
        "mission_package": mission,
        "dry_run": args.dry_run,
        "next_action": "Prosseguir para prd-generator",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
