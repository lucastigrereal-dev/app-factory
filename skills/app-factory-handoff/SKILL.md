---
name: app-factory-handoff
version: "1.0"
description: "Empacota tudo (PRD + blueprint + scaffold + testes + deploy) em prompt executável pro Claude Code."
wave: wave_2_core
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: automacao
status: active
risk: low
model: sonnet
cost_estimate: "$0.002/run"
depends_on: [all-pipeline-skills]
next_skill: memory-writeback
---

# Skill: app-factory-handoff

## Role
Input: Todos os artefatos gerados + riscos + project name
Output: Handoff package + CLAUDE_CODE_PROMPT.md + execution order + gates

## Input Contract
```json
{
  "artifacts": {
    "prd": "artifacts/prd/output.md",
    "blueprint": "artifacts/blueprint/output.md",
    "scaffold": "artifacts/scaffold/output/",
    "deploy_plan": "artifacts/deploy/output.md"
  },
  "risks": [
    {"level": "R1", "description": "Baixo budget"},
    {"level": "R2", "description": "Integração manual com restaurantes"}
  ],
  "project_name": "hotel-delivery-natal",
  "stack": {"frontend": "Next.js 14", "backend": "Supabase"},
  "estimated_build_time": "2 semanas"
}
```

## Output Contract
```json
{
  "handoff_package": "artifacts/handoff/package.zip",
  "claude_code_prompt": "CLAUDE_CODE_PROMPT.md",
  "execution_order": [
    {"step": 1, "action": "Criar projeto Next.js", "skill": "repo-scaffolder", "time": "10min"},
    {"step": 2, "action": "Configurar Supabase", "skill": "app-factory-schema-designer", "time": "20min"},
    {"step": 3, "action": "Implementar API", "skill": "app-factory-api-contractor", "time": "30min"},
    {"step": 4, "action": "Criar frontend", "skill": "app-factory-frontend-planner", "time": "1h"},
    {"step": 5, "action": "Testes", "skill": "app-factory-test-oracle", "time": "30min"},
    {"step": 6, "action": "Deploy", "skill": "app-factory-deploy-planner", "time": "15min"}
  ],
  "gates": [
    {"checkpoint": "CP-8", "condition": "Build passando", "blocker": true},
    {"checkpoint": "CP-9", "condition": "Testes E2E passando", "blocker": true},
    {"checkpoint": "CP-12", "condition": "Risco R3 = aprovação", "blocker": true}
  ],
  "estimated_total_time": "2h 45min",
  "next_action": "Executar handoff no Claude Code"
}
```

## Execution
1. Coleta todos os artefatos do pipeline
2. Resume riscos em ordem de severidade
3. Gera execution_order com tempo estimado por step
4. Lista gates obrigatórios (blocker=true = não pula)
5. Gera CLAUDE_CODE_PROMPT.md com:
   - Contexto do projeto
   - Stack escolhida
   - Ordens de execução
   - Gates e riscos
   - Comandos exatos (npx, npm, git)
6. Empacota tudo em handoff_package

## Guardrails
- Prompt sem gates = rejeitado
- Sem riscos documentados = rejeitado
- Sem rollback plan = rejeitado
- SEMPRE inclui alternativas se risco alto
- Execution order SEM tempos estimados = rejeitado

## Next Skill
→ memory-writeback
