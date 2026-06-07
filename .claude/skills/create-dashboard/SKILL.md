---
name: create-dashboard
description: Gera dashboard completo (backend + frontend + tests) via orchestrator v2
action: run-script
task_type: code-gen
output: dashboard/
next_action: Rodar backend e abrir frontend no browser
---

# Criar Dashboard

Gere um dashboard de analytics/metricas para o dominio descrito.

## Instrucao
Use o orchestrator v2 do App Factory:
python src/orchestrator_v2.py --idea "{{descricao}}" --app-name "{{app_name}}" --type dashboard

## Variaveis
- descricao: {{descricao}}
- app_name: {{app_name}}

## Exemplo
Dashboard de vendas para ecommerce = app_name "dash-vendas"
Dashboard de leads para imobiliaria = app_name "dash-leads"