#!/usr/bin/env python3
"""Wrapper: create-dashboard — chama orchestrator v2.

Uso:
    python run.py --desc "Dashboard de vendas para ecommerce" --name "dash-vendas"
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
ORCHESTRATOR = REPO_ROOT / "src" / "orchestrator_v2.py"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desc", required=True, help="Descricao do dashboard")
    parser.add_argument("--name", required=True, help="Nome do app (snake_case)")
    args = parser.parse_args()

    cmd = [sys.executable, str(ORCHESTRATOR), "--idea", args.desc, "--app-name", args.name, "--type", "dashboard"]
    print(f"[CREATE-DASHBOARD] Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"[ERRO] {result.stderr}")
        sys.exit(1)

    # Extrai path do output
    path = None
    for line in result.stdout.split("\n"):
        if "Pasta:" in line:
            path = line.split("Pasta:")[1].strip()
            break

    print(json.dumps({"status": "ok", "path": path, "type": "dashboard"}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
