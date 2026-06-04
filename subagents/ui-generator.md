---
name: ui-generator
type: subagent
squad: engineering
description: Gera componentes React + Tailwind a partir de frontend plan.
model: sonnet
cost_estimate: "$0.004/run"
---

# Subagente: ui-generator

## Propósito
Gera componentes React/TypeScript com Tailwind CSS baseado no frontend plan.

## Input
```json
{
  "frontend_plan": "artifacts/frontend/frontend-plan.md",
  "design_system": "shadcn/ui",
  "pages": ["Home", "Dashboard"]
}
```

## Output
```json
{
  "components": [
    {"path": "src/components/ui/Button.tsx", "content": "..."},
    {"path": "src/components/layout/Sidebar.tsx", "content": "..."}
  ],
  "pages": [
    {"path": "src/app/page.tsx", "content": "..."},
    {"path": "src/app/dashboard/page.tsx", "content": "..."}
  ]
}
```

## Quando despachar
- `repo-scaffolder` gera UI após frontend plan aprovado

## Exemplo
```
Agent tool: ui-generator
Prompt: "Gere componentes React para landing page de hotel delivery"
```
