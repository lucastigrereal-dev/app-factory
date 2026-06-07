---
name: app-factory-stack-decider
version: "1.0"
description: "Escolhe stack ideal baseado em constraints (custo, time, expertise, escala). Next.js vs n8n vs low-code."
wave: wave_2_core
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: arquitetura
status: active
risk: medium
model: sonnet
cost_estimate: "$0.003/run"
depends_on: [prd-generator]
next_skill: blueprint-generator
---

# Skill: app-factory-stack-decider

## Role
Input: PRD aprovado + constraints (budget, time, skills, scale)
Output: Stack completo justificado (frontend + backend + db + hosting + CI/CD)

## Input Contract
```json
{
  "prd_path": "artifacts/prd/output.md",
  "budget": "R$2000",
  "team_skills": ["Next.js", "Supabase", "Tailwind"],
  "scale_estimate": "100 usuários/mês",
  "non_functional": ["SSR", "PWA", "notificações push"],
  "time_constraint": "2 semanas"
}
```

## Output Contract
```json
{
  "frontend": "Next.js 14 + Tailwind + shadcn/ui",
  "backend": "Supabase (PostgreSQL + Edge Functions)",
  "database": "PostgreSQL via Supabase",
  "hosting": "Vercel (frontend) + Supabase (db)",
  "ci_cd": "GitHub Actions → Vercel",
  "cost_estimate": "R$150/mês (Vercel Pro + Supabase Pro)",
  "justification": "Equipe já domina Next.js+Supabase. Escalabilidade automática. Menor custo operacional.",
  "alternatives": [
    {"stack": "n8n + Airtable + Bubble", "pros": "Zero código", "cons": "Limitado", "when": "Budget < R$500"},
    {"stack": "NestJS + PostgreSQL + AWS", "pros": "Enterprise", "cons": "Complexo", "when": "Scale > 10k users"}
  ],
  "next_action": "Prosseguir para blueprint-generator"
}
```

## Execution
1. Parse PRD → extrai requisitos técnicos (SSR? real-time? mobile?)
2. Mapeia constraints → budget, time, skills, scale
3. Compara stacks candidatas por critérios:
   - Custo (infra + licenças)
   - Time to market
   - Expertise do time
   - Escalabilidade futura
   - Vendor lock-in
4. Escolhe stack vencedora
5. Justifica em 1 parágrafo
6. Lista alternativas com "quando usar"

## Guardrails
- Budget < R$500 = low-code/n8n-first
- Scale > 10k users = PostgreSQL obrigatório (não SQLite)
- Time < 1 semana = no-code/low-code obrigatório
- Sem CI/CD = rejeitado
- SEMPRE justifica, nunca "porque sim"

## Next Skill
→ blueprint-generator
