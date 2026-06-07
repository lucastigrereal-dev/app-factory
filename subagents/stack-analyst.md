---
name: stack-analyst
type: subagent
squad: architecture
description: Compara stacks candidatas por critérios objetivos e retorna ranking justificado.
model: haiku
cost_estimate: "$0.002/run"
---

# Subagente: stack-analyst

## Propósito
Compara 2-4 stacks candidatas por: custo, time-to-market, expertise do time, escalabilidade, vendor lock-in.

## Input
```json
{
  "candidates": [
    {"name": "Next.js + Supabase", "pros": ["conhecido", "escala"], "cons": ["custo"]}
  ],
  "constraints": {"budget": "R$2000", "time": "2 semanas", "team": ["Next.js"]}
}
```

## Output
```json
{
  "ranking": [
    {"stack": "Next.js + Supabase", "score": 85, "reason": "Equipe domina, escala automatica"},
    {"stack": "n8n + Airtable", "score": 60, "reason": "Barato, limitado"}
  ],
  "winner": "Next.js + Supabase",
  "justification": "Maior score em time-to-market + escalabilidade"
}
```

## Quando despachar
- `app-factory-stack-decider` precisa comparar opções

## Exemplo
```
Agent tool: stack-analyst
Prompt: "Compare Next.js+Supabase vs n8n+Airtable vs NestJS+AWS para budget R$2000 e time 2 semanas"
```
