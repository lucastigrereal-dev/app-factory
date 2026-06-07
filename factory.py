#!/usr/bin/env python3
"""
App Factory v8 — Entrypoint CLI
Uso: python factory.py --intention "criar landing page para hotel" [--type saas] [--output-dir ./out]
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="App Factory v8 CLI")
    parser.add_argument("--intention", required=True, help="Descricao da ideia/app")
    parser.add_argument("--type", default="saas", choices=["landing", "crm", "dashboard", "saas", "factory"])
    parser.add_argument("--output-dir", default="artifacts", help="Diretorio de artefatos")
    parser.add_argument("--checkpoint", default="all", help="Parar em checkpoint especifico")
    parser.add_argument("--live", action="store_true", help="Desativar dry-run (requer aprovacao)")
    args = parser.parse_args()

    master = Path(__file__).resolve().parent / "skills" / "app-factory-master" / "run.py"
    if not master.exists():
        print("[ERRO] Skill master nao encontrada:", master, file=sys.stderr)
        return 1

    cmd = [
        sys.executable, str(master),
        "--intention", args.intention,
        "--type", args.type,
        "--artifacts-dir", args.output_dir,
        "--checkpoint", args.checkpoint,
        "--output", f"{args.output_dir}/master_output.json",
    ]
    if not args.live:
        cmd.append("--dry-run")

    print("[FACTORY] Iniciando pipeline...")
    print("[FACTORY] Comando:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

    if result.returncode != 0:
        print("[FACTORY] ERRO:", result.stderr, file=sys.stderr)
        return result.returncode

    try:
        output = json.loads(result.stdout)
    except Exception:
        output = {"raw": result.stdout}

    print("\n=== RESUMO ===")
    print(f"Status      : {output.get('status')}")
    print(f"Estado atual: {output.get('current_state')}")
    print(f"Completados : {len(output.get('completed_states', []))}")
    print(f"Pendentes   : {len(output.get('pending_states', []))}")
    print(f"Proximo     : {output.get('next_action')}")
    print(f"Artifacts   : {output.get('artifacts_dir')}")

    # Salva output no root tambem
    root_output = Path(args.output_dir) / "master_output.json"
    root_output.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] Output salvo em: {root_output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
