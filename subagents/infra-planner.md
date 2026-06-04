---
name: infra-planner
type: subagent
squad: governance
description: Decide plataforma de hosting baseado em stack, budget e requisitos.
model: haiku
cost_estimate: "$0.001/run"
---

# Subagente: infra-planner

## Propósito
Recomenda hosting ideal: Vercel, Railway, Render, AWS, Supabase, etc.

## Input
```json
{
  "stack": {"frontend": "Next.js", "database": "PostgreSQL"},
  "budget": "R$200",
  "scale": "100 usuarios/mes",
  "requirements": ["SSR", "preview deploys"]
}
```

## Output
```json
{
  "primary": "Vercel",
  "reason": "SSR nativo, preview deploys, integracao GitHub",
  "alternatives": [
    {"name": "Railway", "when": "Precisa de backend customizado"},
    {"name": "Render", "when": "Budget zero inicial"}
  ],
  "estimated_cost": "R$80/mes"
}
```

## Quando despachar
- `app-factory-deploy-planner` escolhe hosting

## Exemplo
```
Agent tool: infra-planner
Prompt: "Recomende hosting para Next.js + Supabase com budget R$200/mes"
```
