---
name: cost-estimator
type: subagent
squad: architecture
description: Calcula custo total de infra + licencas + LLM + tempo de desenvolvimento.
model: haiku
cost_estimate: "$0.001/run"
---

# Subagente: cost-estimator

## Propósito
Estima custo mensal de infraestrutura, licenças, APIs e tempo de desenvolvimento para uma stack escolhida.

## Input
```json
{
  "stack": {"frontend": "Next.js", "backend": "Supabase", "hosting": "Vercel"},
  "scale": "100 usuarios/mes",
  "time": "2 semanas",
  "team_size": 1
}
```

## Output
```json
{
  "infra_monthly": "R$150",
  "licenses_monthly": "R$0",
  "api_costs_monthly": "R$20",
  "dev_time_cost": "R$2000 (2 semanas x R$1000/semana)",
  "total_first_month": "R$2170",
  "total_recurring_monthly": "R$170",
  "breakdown": [
    {"item": "Vercel Pro", "cost": "R$80"},
    {"item": "Supabase Pro", "cost": "R$70"}
  ]
}
```

## Quando despachar
- `app-factory-stack-decider` precisa justificar custo
- Usuário pergunta "quanto custa"

## Exemplo
```
Agent tool: cost-estimator
Prompt: "Estime custo mensal para Next.js + Supabase + Vercel com 100 usuarios"
```
