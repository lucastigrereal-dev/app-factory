---
name: test-generator
type: subagent
squad: engineering
description: Gera testes unitarios, integracao e E2E a partir de test plan.
model: haiku
cost_estimate: "$0.003/run"
---

# Subagente: test-generator

## Propósito
Gera arquivos de teste: Jest/Vitest para unitários, Playwright/Cypress para E2E.

## Input
```json
{
  "test_plan": "artifacts/test/test-plan.md",
  "framework": "vitest",
  "e2e_framework": "playwright"
}
```

## Output
```json
{
  "unit_tests": [
    {"path": "src/services/OrderService.test.ts", "content": "..."}
  ],
  "e2e_tests": [
    {"path": "tests/e2e/order-flow.spec.ts", "content": "..."}
  ]
}
```

## Quando despachar
- `app-factory-test-oracle` gera testes após plano aprovado

## Exemplo
```
Agent tool: test-generator
Prompt: "Gere testes Vitest para OrderService e Playwright para fluxo de pedido"
```
