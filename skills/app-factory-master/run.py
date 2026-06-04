#!/usr/bin/env python3
"""
app-factory-master
Orquestrador master da App Factory v8 — executa skills reais via subprocess.
Recebe intencao, roteia para squads, monitora pipeline, coleta artefatos.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# Mapeamento estado -> diretorio da skill
STATE_TO_SKILL = {
    "intake": None,
    "discovery": "app-factory-discovery",
    "prd": None,
    "blueprint": None,
    "stack": "app-factory-stack-decider",
    "schema": "app-factory-schema-designer",
    "api": "app-factory-api-contractor",
    "frontend": "app-factory-frontend-planner",
    "test": "app-factory-test-oracle",
    "scaffold": None,
    "security": None,
    "deploy": "app-factory-deploy-planner",
    "handoff": "app-factory-handoff",
    "akasha": None,
    "kratos": None,
}

# Squad mapping (cores para logs)
SQUADS = {
    "intake": "product",
    "discovery": "product",
    "prd": "product",
    "blueprint": "architecture",
    "stack": "architecture",
    "schema": "architecture",
    "api": "architecture",
    "frontend": "engineering",
    "test": "engineering",
    "scaffold": "engineering",
    "security": "governance",
    "deploy": "governance",
    "handoff": "governance",
    "akasha": "memory",
    "kratos": "memory",
}

ALL_STATES = list(STATE_TO_SKILL.keys())


def skill_has_run_py(skill_dir: Path) -> bool:
    return (skill_dir / "run.py").is_file()


def run_skill(skill_dir: Path, input_path: Path, output_path: Path, dry_run: bool = True) -> dict:
    """Executa uma skill via subprocess e retorna o output JSON."""
    cmd = [
        sys.executable,
        str(skill_dir / "run.py"),
        "--input", str(input_path),
        "--output", str(output_path),
    ]
    if dry_run:
        cmd.append("--dry-run")

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    if result.returncode != 0:
        raise RuntimeError(
            f"Skill {skill_dir.name} falhou (exit {result.returncode}): {result.stderr.strip()}"
        )

    if output_path.exists():
        return json.loads(output_path.read_text(encoding="utf-8"))
    # fallback: tenta parse stdout como JSON
    try:
        return json.loads(result.stdout)
    except Exception:
        return {"stdout": result.stdout, "stderr": result.stderr}


def main():
    parser = argparse.ArgumentParser(description="App Factory Master Orchestrator")
    parser.add_argument("--intention", required=True, help="Intencao do usuario")
    parser.add_argument("--type", default="saas", choices=["landing", "crm", "dashboard", "saas", "factory"])
    parser.add_argument("--dry-run", action="store_true", default=True, help="Modo simulacao")
    parser.add_argument("--checkpoint", default="all", help="Checkpoint alvo (all|intake|discovery|...)")
    parser.add_argument("--output", default="app_factory_output.json", help="Arquivo de saida master")
    parser.add_argument("--artifacts-dir", default="artifacts", help="Diretorio de artefatos")
    args = parser.parse_args()

    artifacts_dir = Path(args.artifacts_dir)
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Define target states
    if args.checkpoint == "all":
        target_states = ALL_STATES.copy()
    else:
        idx = ALL_STATES.index(args.checkpoint)
        target_states = ALL_STATES[: idx + 1]

    completed = []
    pending = []
    current = None
    errors = []

    # Acumulador de contexto
    context = {
        "intention": args.intention,
        "type": args.type,
        "dry_run": args.dry_run,
    }

    for state in target_states:
        current = state
        state_dir = artifacts_dir / state
        state_dir.mkdir(parents=True, exist_ok=True)
        skill_name = STATE_TO_SKILL.get(state)
        skill_dir = Path(__file__).resolve().parent.parent / skill_name if skill_name else None

        input_path = state_dir / "input.json"
        output_path = state_dir / "output.json"

        # Escreve input
        input_path.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")

        if skill_dir and skill_has_run_py(skill_dir):
            try:
                result = run_skill(skill_dir, input_path, output_path, dry_run=args.dry_run)
                completed.append({
                    "state": state,
                    "squad": SQUADS[state],
                    "status": "done",
                    "artifact": str(output_path),
                    "skill": skill_name,
                })
                # Alimenta contexto para proximos estados
                context[f"{state}_output"] = result
            except Exception as exc:
                errors.append({"state": state, "error": str(exc)})
                completed.append({
                    "state": state,
                    "squad": SQUADS[state],
                    "status": "failed",
                    "artifact": str(output_path),
                    "skill": skill_name,
                })
                break
        else:
            # Simula estado sem skill run.py
            simulated = {
                "state": state,
                "squad": SQUADS[state],
                "status": "simulated",
                "artifact": str(output_path),
                "skill": skill_name,
                "note": "Skill sem run.py — simulado pelo master",
            }
            completed.append(simulated)
            context[f"{state}_output"] = simulated

    pending = [s for s in ALL_STATES if s not in [c["state"] for c in completed]]

    # Compatibilidade: manter campos legados usados pelos testes v7
    legacy_artifacts = {
        "prd": str(artifacts_dir / "prd" / "output.json"),
        "blueprint": str(artifacts_dir / "blueprint" / "output.json"),
        "scaffold": str(artifacts_dir / "scaffold" / "output.json"),
        "deploy_plan": str(artifacts_dir / "deploy" / "output.json"),
        "handoff": str(artifacts_dir / "handoff" / "output.json"),
    }
    risks = [{"level": "R0", "reason": "Dry-run mode: nenhum risco real"}] if args.dry_run else [{"level": "R1", "reason": "Pipeline iniciado — requer monitoramento"}]

    output = {
        "status": "completed" if not errors else "failed",
        "current_state": current,
        "completed_states": completed,
        "pending_states": pending,
        "squads_invoked": list(set(SQUADS[s] for s in [c["state"] for c in completed])),
        "artifacts_dir": str(artifacts_dir.resolve()),
        "artifacts": legacy_artifacts,
        "errors": errors,
        "risks": risks,
        "dry_run": args.dry_run,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "next_action": (
            "Pipeline completo. Revisar artefatos em " + str(artifacts_dir)
            if not errors
            else f"Corrigir erro em '{current}' e reexecutar."
        ),
    }

    out_path = Path(args.output)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
