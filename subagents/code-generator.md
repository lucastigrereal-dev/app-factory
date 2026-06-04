---
name: code-generator
type: subagent
squad: engineering
description: Gera código Python ou TypeScript real a partir de blueprint e schema.
model: sonnet
cost_estimate: "$0.005/run"
---

# Subagente: code-generator

## Propósito
Gera código real: models, services, controllers, API routes, migrations baseado no blueprint e schema.

## Input
```json
{
  "blueprint_path": "artifacts/blueprint/output.md",
  "schema_yaml": "artifacts/schema/schema.yaml",
  "language": "typescript",
  "framework": "next.js"
}
```

## Output
```json
{
  "files": [
    {"path": "src/models/User.ts", "content": "..."},
    {"path": "src/services/OrderService.ts", "content": "..."}
  ],
  "tests": [
    {"path": "src/services/OrderService.test.ts", "content": "..."}
  ]
}
```

## Quando despachar
- `repo-scaffolder` gera código após blueprint aprovado

## Exemplo
```
Agent tool: code-generator
Prompt: "Gere models e services TypeScript para schema de delivery de hotel"
```
