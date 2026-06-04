---
name: app-factory-test-oracle
version: "1.0"
description: "Gera plano de testes completo: unitários, integração, E2E. Valida cobertura de requisitos críticos."
wave: wave_3_agents
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: qualidade
status: active
risk: low
model: sonnet
cost_estimate: "$0.003/run"
depends_on: [app-factory-frontend-planner]
next_skill: repo-scaffolder
---

# Skill: app-factory-test-oracle

## Role
Input: PRD + blueprint + API contract + frontend plan
Output: Test plan markdown + lista de casos de teste + cobertura estimada

## Input Contract
```json
{
  "prd_path": "artifacts/prd/output.md",
  "blueprint_path": "artifacts/blueprint/output.md",
  "api_contract_yaml": "artifacts/api/api_contract.yaml",
  "frontend_plan": "artifacts/frontend/frontend-plan.md",
  "product_name": "hotel-delivery-natal"
}
```

## Output Contract
```json
{
  "test_plan": "artifacts/test/test-plan.md",
  "unit_tests": [
    {"target": "OrderService.create", "cases": ["pedido válido", "pedido sem itens", "usuário inativo"], "expected": "criar|rejeitar|rejeitar"}
  ],
  "integration_tests": [
    {"target": "POST /api/orders", "cases": ["fluxo completo", "auth inválido"], "expected": "201|401"}
  ],
  "e2e_tests": [
    {"target": "Login -> Dashboard -> Criar Pedido", "cases": ["happy path", "timeout"], "expected": "sucesso|erro"}
  ],
  "coverage_estimate": "85%",
  "critical_gaps": [],
  "dry_run": true,
  "next_action": "Prosseguir para repo-scaffolder"
}
```

## Execution
1. Parse PRD -> requisitos críticos
2. Parse blueprint -> componentes testáveis
3. Parse API contract -> endpoints para testar
4. Parse frontend plan -> fluxos E2E
5. Gera casos de teste unitários
6. Gera casos de integração
7. Gena casos E2E (happy path + edge cases)
8. Calcula cobertura estimada
9. Identifica gaps críticos

## Guardrails
- Requisito crítico sem teste = rejeitado
- Critério vago = rejeitado
- Caso com dados sensíveis = mascarado
- SEMPRE inclui happy path + 2 edge cases
- Cobertura < 70% = flag de risco

## Next Skill
→ repo-scaffolder
