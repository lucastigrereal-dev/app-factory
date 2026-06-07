---
name: create-saas-mvp
description: Gera SaaS MVP completo (auth + DB + CRUD + frontend) via orchestrator v2
action: run-script
task_type: code-gen
output: saas/
next_action: Rodar docker-compose up e testar signup/login
---

# Criar SaaS MVP

Gere um SaaS MVP com multi-tenant basico.

## Instrucao
Use o orchestrator v2:
python src/orchestrator_v2.py --idea "{{descricao}}" --app-name "{{app_name}}" --type saas

## Variaveis
- descricao: {{descricao}}
- app_name: {{app_name}}

## Exemplo
SaaS de agendamento para clinicas = app_name "agenda-clinica"
SaaS de gestao de projetos = app_name "projectx"