#!/usr/bin/env python3
"""
kratos-snapshot
Gera snapshot JSON do estado do projeto para auditoria.
"""

import argparse
import json
import sys
import uuid
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Kratos Snapshot Generator")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="kratos_snapshot.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    snapshot = {
        "snapshot_id": str(uuid.uuid4()),
        "project_id": data.get("project_id", "unknown"),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "phase": data.get("phase", "unknown"),
        "status": data.get("status", "in_progress"),
        "cost": data.get("cost", 0.0),
        "risk": data.get("risk", "low"),
        "approval": data.get("approval", False),
        "is_dry_run": args.dry_run,
    }

    result = {
        "snapshot": snapshot,
        "snapshot_path": "examples/kratos_snapshot_event.json",
        "dry_run": args.dry_run,
        "next_action": "Exportar para Kratos (requer aprovacao CP-3)",
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
