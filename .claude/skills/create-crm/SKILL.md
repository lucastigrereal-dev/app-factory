---
name: create-crm
description: Gera CRM completo (pipeline de vendas, contatos, tarefas) via orchestrator v2
action: run-script
task_type: code-gen
output: crm/
next_action: Rodar backend e abrir kanban no frontend
---

# Criar CRM

Gere um CRM com pipeline de vendas e gestao de contatos.

## Instrucao
Use o orchestrator v2:
python src/orchestrator_v2.py --idea "{{descricao}}" --app-name "{{app_name}}" --type crm

## Variaveis
- descricao: {{descricao}}
- app_name: {{app_name}}

## Exemplo
CRM para imobiliaria = app_name "crm-imob"
CRM para agencia de viagens = app_name "crm-viagens"