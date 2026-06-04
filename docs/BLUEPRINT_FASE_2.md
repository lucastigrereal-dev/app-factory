# Blueprint das 4 Skills Core — App Factory Fase 2
> Gerado em: 2026-06-04 | Modo: Híbrido (planejamento paralelo → execução sequencial)

## Padrão Compartilhado

### SKILL.md Template
```yaml
---
name: app-factory-XXXX
version: "1.0"
description: "..."
wave: wave_2_core
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: produto | arquitetura | devops | automacao
status: active
risk: low | medium
model: sonnet | haiku
cost_estimate: "$0.0XX/run"
depends_on: [skill_id]
next_skill: skill_id
---

# Skill: app-factory-XXXX

## Role
Input: ...
Output: ...

## Input Contract
```json
{...}
```

## Output Contract
```json
{...}
```

## Execution
1. ...
2. ...

## Guardrails
- ...

## Next Skill
→ ...
```

### run.py Template
```python
#!/usr/bin/env python3
"""..."""
import argparse
import json
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--input", required=True, help="Path to input JSON/YAML")
    parser.add_argument("--output", default="output.json", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()

    # Load input
    input_path = Path(args.input)
    data = json.loads(input_path.read_text(encoding="utf-8"))

    # Process
    result = {...}

    # Write output
    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### test_1.py Template
```python
import json, subprocess, sys
from pathlib import Path

RUN_PY = Path(__file__).parent.parent / "run.py"

def test_run_py_exists():
    assert RUN_PY.exists()

def test_main_runs_dry_run():
    # cria input fixture temporário
    # roda com --dry-run
    # valida output schema

def test_output_schema():
    # valida campos obrigatórios
```

---

## Skill 1: app-factory-discovery

| Campo | Valor |
|---|---|
| **Tipo** | produto |
| **Squad** | Product |
| **Objetivo** | Validar se a ideia é problema real antes de gerar PRD |
| **Risk** | low |
| **Model** | sonnet |
| **Input** | `{"intention": "...", "market_context": "...", "budget": "...", "timeline": "..."}` |
| **Output** | `{"go": true/false, "confidence": 0-1, "problem_statement": "...", "competitors": [...], "risks": [...], "alternatives": [...], "next_action": "..."}` |
| **Depends on** | app-factory-intake |
| **Next skill** | prd-generator (se go=true) ou retorna (se go=false) |
| **Execution** | 1. Busca contexto Akasha + trends 2. Analisa competição 3. Valida dor do usuário 4. Gera go/no-go |
| **Guardrails** | Sem dados de mercado = baixa confiança. Ideia sem dor clara = no-go. |

---

## Skill 2: app-factory-stack-decider

| Campo | Valor |
|---|---|
| **Tipo** | arquitetura |
| **Squad** | Architecture |
| **Objetivo** | Escolher stack ideal baseado em constraints |
| **Risk** | medium |
| **Model** | sonnet |
| **Input** | `{"prd_path": "...", "budget": "...", "team_skills": [...], "scale_estimate": "...", "non_functional": [...]}` |
| **Output** | `{"frontend": "...", "backend": "...", "database": "...", "hosting": "...", "ci_cd": "...", "cost_estimate": "...", "justification": "...", "alternatives": [...]}` |
| **Depends on** | prd-generator |
| **Next skill** | blueprint-generator |
| **Execution** | 1. Parse PRD por requisitos técnicos 2. Mapeia constraints 3. Compara stacks 4. Justifica escolha |
| **Guardrails** | Budget < R$500 = low-code/n8n-first. Escalabilidade > 10k users = PostgreSQL obrigatório. |

---

## Skill 3: app-factory-deploy-planner

| Campo | Valor |
|---|---|
| **Tipo** | devops |
| **Squad** | Governance |
| **Objetivo** | Gerar plano de deploy completo |
| **Risk** | medium |
| **Model** | sonnet |
| **Input** | `{"blueprint_path": "...", "stack": {...}, "environment": "preview|staging|prod", "rollback_required": true}` |
| **Output** | `{"deploy_plan": "...", "github_actions": "...", "dockerfile": "...", "vercel_json": "...", "env_vars": [...], "rollback_plan": "...", "estimated_time": "..."}` |
| **Depends on** | blueprint-generator, app-factory-stack-decider |
| **Next skill** | app-factory-handoff |
| **Execution** | 1. Analisa stack 2. Escolhe hosting 3. Gera CI/CD 4. Define env vars 5. Plano rollback |
| **Guardrails** | Sem testes = não deploya produção. Preview obrigatório antes de prod. |

---

## Skill 4: app-factory-handoff

| Campo | Valor |
|---|---|
| **Tipo** | automacao |
| **Squad** | Governance |
| **Objetivo** | Empacotar tudo em prompt executável pro Claude Code |
| **Risk** | low |
| **Model** | sonnet |
| **Input** | `{"artifacts": {"prd": "...", "blueprint": "...", "scaffold": "...", "deploy_plan": "..."}, "risks": [...], "project_name": "..."}` |
| **Output** | `{"handoff_package": "...", "claude_code_prompt": "...", "execution_order": [...], "gates": [...], "estimated_total_time": "..."}` |
| **Depends on** | Todas as skills de pipeline |
| **Next skill** | memory-writeback |
| **Execution** | 1. Coleta artefatos 2. Resume riscos 3. Ordena execução 4. Gera prompt final 5. Empacota markdown |
| **Guardrails** | Prompt sem gates = rejeitado. Sem riscos documentados = rejeitado. |

---

## Dependências

```
app-factory-intake
    ↓
app-factory-discovery ⏵ prd-generator
    ↓
app-factory-stack-decider ⏵ blueprint-generator
    ↓
app-factory-schema-designer (Fase 3)
    ↓
app-factory-api-contractor (Fase 3)
    ↓
app-factory-frontend-planner (Fase 3)
    ↓
app-factory-test-oracle (Fase 3)
    ↓
repo-scaffolder
    ↓
validation-gate-runner
    ↓
app-factory-deploy-planner
    ↓
app-factory-handoff
    ↓
memory-writeback → kratos-snapshot
```

## Execução Sequencial
1. Criar `app-factory-discovery` (padrão definido)
2. Criar `app-factory-stack-decider` (mesmo padrão)
3. Criar `app-factory-deploy-planner` (mesmo padrão)
4. Criar `app-factory-handoff` (mesmo padrão)
5. Atualizar registries
6. Rodar testes (12 total = 4 skills × 3 tests)
