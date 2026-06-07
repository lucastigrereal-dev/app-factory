---
name: app-factory-master
version: "1.0"
description: "Orquestrador master da App Factory. Recebe intenção, roteia para squads, monitora pipeline, resolve conflitos, entrega pacote final."
wave: wave_1_orchestration
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: orquestrador
status: active
risk: medium
model: sonnet
cost_estimate: "$0.02/run"
next_skill: app-factory-discovery
---

# Skill: app-factory-master

Orquestrador master da App Factory v8.

## Role
Input: intenção do usuário ("crie um CRM para hotéis")
Output: pacote completo (PRD + blueprint + scaffold + deploy plan + handoff)

## Pipeline State Machine
```
intake → discovery → prd → blueprint → stack → schema → api → frontend → test → scaffold → security → deploy → handoff → akasha → kratos
```

## States
| State | Squad | Skill | Go Condition |
|---|---|---|---|
| intake | Product | app-intake | Ideia recebida |
| discovery | Product | app-factory-discovery | Go: problema real |
| prd | Product | prd-generator | PRD aprovado |
| blueprint | Architecture | blueprint-generator | Blueprint completo |
| stack | Architecture | app-factory-stack-decider | Stack justificada |
| schema | Architecture | app-factory-schema-designer | Schema validado |
| api | Architecture | app-factory-api-contractor | Contrato assinado |
| frontend | Engineering | app-factory-frontend-planner | UI planejada |
| test | Engineering | app-factory-test-oracle | Testes gerados |
| scaffold | Engineering | repo-scaffolder | Build passando |
| security | Governance | validation-gate-runner | Gates passaram |
| deploy | Governance | app-factory-deploy-planner | Deploy plan pronto |
| handoff | Governance | app-factory-handoff | Prompt executável gerado |
| akasha | Memory | memory-writeback | Persistido |
| kratos | Memory | kratos-snapshot | Snapshot tirado |

## Squads Router
- **Product Squad**: intake, discovery, prd
- **Architecture Squad**: blueprint, stack, schema, api
- **Engineering Squad**: frontend, test, scaffold
- **Governance Squad**: security, deploy, handoff
- **Memory Squad**: akasha, kratos

## Execution
1. Recebe intenção do usuário
2. Classifica tipo de produto (landing, crm, dashboard, saas, factory)
3. Delega para Product Squad (intake)
4. Aguarda checkpoint antes de avançar
5. Se go → delega próximo squad
6. Se no-go → retorna com razão + sugestão
7. Ao final → entrega handoff package

## Output Contract
```json
{
  "status": "in_progress|completed|blocked|failed",
  "current_state": "string",
  "completed_states": [],
  "pending_states": [],
  "squads_invoked": [],
  "artifacts": {
    "prd": "path",
    "blueprint": "path",
    "scaffold": "path",
    "deploy_plan": "path",
    "handoff": "path"
  },
  "risks": [],
  "next_action": "Continuar? (sim/nao)"
}
```

## Guardrails
- SEMPRE usa dry-run como padrão
- NUNCA pula checkpoints
- R3 = requer aprovação explícita
- Schema/API changes = sequencial obrigatório
- Shared files = HIGH RISK, loga conflito

## Next Skill
→ app-factory-discovery (primeira do pipeline)
