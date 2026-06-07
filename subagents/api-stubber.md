---
name: api-stubber
type: subagent
squad: engineering
description: Gera stubs de API FastAPI/Nest/Next.js a partir de API contract.
model: haiku
cost_estimate: "$0.003/run"
---

# Subagente: api-stubber

## Propósito
Gera código de endpoints API com validação Zod/Pydantic a partir do contrato OpenAPI.

## Input
```json
{
  "api_contract_yaml": "artifacts/api/api_contract.yaml",
  "framework": "next.js",
  "language": "typescript"
}
```

## Output
```json
{
  "files": [
    {"path": "src/app/api/users/route.ts", "content": "..."},
    {"path": "src/app/api/orders/route.ts", "content": "..."}
  ],
  "schemas": [
    {"path": "src/lib/schemas.ts", "content": "Zod schemas..."}
  ]
}
```

## Quando despachar
- `app-factory-api-contractor` gera stubs após contrato definido

## Exemplo
```
Agent tool: api-stubber
Prompt: "Gere API routes Next.js para endpoints /api/users e /api/orders"
```
