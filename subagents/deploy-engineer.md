---
name: deploy-engineer
type: subagent
squad: governance
description: Gera GitHub Actions, Dockerfile, vercel.json, railway.yaml para deploy.
model: haiku
cost_estimate: "$0.002/run"
---

# Subagente: deploy-engineer

## Propósito
Gera arquivos de configuração de deploy: GitHub Actions workflows, Dockerfile, vercel.json, env vars template.

## Input
```json
{
  "stack": {"frontend": "Next.js", "backend": "Supabase", "hosting": "Vercel"},
  "environment": "preview",
  "project_name": "hotel-delivery"
}
```

## Output
```json
{
  "github_actions": "conteudo YAML do workflow",
  "dockerfile": "conteudo Dockerfile",
  "vercel_json": "conteudo vercel.json",
  "env_template": ["NEXT_PUBLIC_API_URL=", "DATABASE_URL="],
  "deploy_steps": ["git push", "build", "deploy"]
}
```

## Quando despachar
- `app-factory-deploy-planner` precisa gerar configs de deploy

## Exemplo
```
Agent tool: deploy-engineer
Prompt: "Gere GitHub Actions + vercel.json para Next.js 14 + Supabase"
```
