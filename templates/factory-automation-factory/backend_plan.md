# Backend Plan — Automation Factory

## Lógica
- **n8n workflows:** Nodes conectados visualmente
- **Custom nodes:** JavaScript/Python para lógica complexa
- **Webhooks:** HTTP endpoints para triggers externos

## API
| Endpoint | Método | Descrição |
|---|---|---|
| `/webhook/inbound` | POST | Recebe eventos externos |
| `/webhook/status` | GET | Health check |
| `/api/executions` | GET | Lista execuções recentes |

## Database
- **Airtable:** Tabelas para leads, logs, config
- **Supabase:** Se escalar para 1000+ registros/dia

## Segurança
- Webhook URLs com token UUID
- API keys em env vars
- Dados sensíveis mascarados nos logs
