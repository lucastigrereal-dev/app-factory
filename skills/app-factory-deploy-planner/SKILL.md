---
name: app-factory-deploy-planner
version: "1.0"
description: "Gera plano de deploy completo: preview, CI/CD, produção, rollback. Vercel/Railway/Render/AWS."
wave: wave_2_core
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: devops
status: active
risk: medium
model: sonnet
cost_estimate: "$0.003/run"
depends_on: [blueprint-generator, app-factory-stack-decider]
next_skill: app-factory-handoff
---

# Skill: app-factory-deploy-planner

## Role
Input: Blueprint + stack decision + ambiente alvo
Output: Deploy plan + GitHub Actions + Dockerfile + env vars + rollback plan

## Input Contract
```json
{
  "blueprint_path": "artifacts/blueprint/output.md",
  "stack": {"frontend": "Next.js 14", "backend": "Supabase", "hosting": "Vercel"},
  "environment": "preview",
  "rollback_required": true,
  "custom_domain": "meuapp.com.br"
}
```

## Output Contract
```json
{
  "deploy_plan": "1. Push para branch preview\n2. GitHub Actions roda build\n3. Vercel deploy preview\n4. Testes E2E no preview\n5. Merge → production\n6. Vercel deploy prod",
  "github_actions": "artifacts/deploy/.github/workflows/deploy.yml",
  "dockerfile": "artifacts/deploy/Dockerfile",
  "vercel_json": "artifacts/deploy/vercel.json",
  "env_vars": [
    {"name": "NEXT_PUBLIC_SUPABASE_URL", "required": true, "source": "Supabase dashboard"},
    {"name": "SUPABASE_SERVICE_ROLE_KEY", "required": true, "secret": true}
  ],
  "rollback_plan": "1. Vercel → Rollback to previous deployment\n2. Supabase → Restore from backup\n3. DNS → Revert CNAME",
  "estimated_time": "15 min para preview, 5 min para prod",
  "next_action": "Prosseguir para app-factory-handoff"
}
```

## Execution
1. Analisa stack → identifica plataformas (Vercel, Railway, Render, AWS)
2. Gera GitHub Actions workflow (build + test + deploy)
3. Gera Dockerfile se necessário
4. Gera vercel.json / railway.json / render.yaml
5. Lista env vars obrigatórias com source
6. Define rollback plan passo a passo
7. Estima tempo de deploy

## Guardrails
- Sem testes = não deploya produção
- Preview obrigatório antes de prod
- Env vars secretas = nunca commitadas
- Rollback plan obrigatório para prod
- SEMPRE dry-run primeiro

## Next Skill
→ app-factory-handoff
