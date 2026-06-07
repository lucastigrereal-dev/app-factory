---
name: app-factory-frontend-planner
version: "1.0"
description: "Planeja interface de usuário: páginas, componentes, navegação, chamadas de API. Gera frontend plan markdown."
wave: wave_3_agents
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: coding
status: active
risk: low
model: sonnet
cost_estimate: "$0.004/run"
depends_on: [app-factory-api-contractor]
next_skill: app-factory-test-oracle
---

# Skill: app-factory-frontend-planner

## Role
Input: PRD + blueprint + API contract
Output: Frontend plan markdown + mapa de navegação + lista de componentes

## Input Contract
```json
{
  "prd_path": "artifacts/prd/output.md",
  "blueprint_path": "artifacts/blueprint/output.md",
  "api_contract_yaml": "artifacts/api/api_contract.yaml",
  "product_name": "hotel-delivery-natal"
}
```

## Output Contract
```json
{
  "frontend_plan": "artifacts/frontend/frontend-plan.md",
  "pages": [
    {"route": "/", "name": "Home", "components": ["Header", "Hero"], "apis": []},
    {"route": "/dashboard", "name": "Dashboard", "components": ["Sidebar", "StatsCard"], "apis": ["GET /api/stats"]}
  ],
  "components": ["Header", "Sidebar", "Button", "Form", "StatsCard"],
  "user_journeys": ["Login -> Dashboard -> Criar Pedido -> Confirmação"],
  "dry_run": true,
  "next_action": "Prosseguir para app-factory-test-oracle"
}
```

## Execution
1. Parse PRD -> funcionalidades visíveis
2. Parse API contract -> endpoints por tela
3. Mapeia navegação (rotas + fluxos)
4. Especifica componentes reutilizáveis
5. Indica chamadas de API por tela
6. Valida acessibilidade (ARIA, contrast)
7. Gera markdown de plano

## Guardrails
- Tela sem endpoint associado = flag de risco
- Componente sem uso real = removido
- Falta acessibilidade = rejeitado
- SEMPRE inclui mobile-first

## Next Skill
→ app-factory-test-oracle
