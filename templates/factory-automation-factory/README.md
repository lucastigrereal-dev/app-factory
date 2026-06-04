# Template: Automation Factory

## O que cria
Fábrica de automações: n8n + WhatsApp + CRM + webhooks + notificações.

## Quando usar
- Processos repetitivos manuais
- Integração entre sistemas sem API nativa
- Alertas e notificações automáticas
- Pipeline de lead qualificado

## Produtos típicos
- Bot WhatsApp para hotéis
- Pipeline n8n: lead → CRM → notificação
- Webhook bridge entre sistemas
- Automação de email marketing

## Stack recomendada
- **Orquestração:** n8n (self-hosted ou cloud)
- **Mensageria:** WhatsApp Business API
- **CRM:** Airtable / Notion / Supabase
- **Webhooks:** n8n webhooks + Node.js microservice
- **Hosting:** Railway / Render

## Dependências
- Número de WhatsApp Business verificado
- Conta n8n (cloud ou Docker)
- API keys dos sistemas integrados

## Riscos
- R1: WhatsApp pode bloquear número se spam
- R2: Rate limits de APIs externas
- R3: Dados sensíveis em webhooks públicos

## Checkpoints
- CP-1: Fluxograma aprovado?
- CP-2: n8n executando localmente?
- CP-3: Teste E2E com número real?
