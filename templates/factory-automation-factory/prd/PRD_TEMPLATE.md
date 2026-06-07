# PRD Template — Automation Factory

## 1. Visão
Criar automação para [PROCESSO] usando n8n + [CANAL].

## 2. Problema
[Descrição da dor manual atual]

## 3. Solução
- Trigger: [evento inicial]
- Ação 1: [passo 1]
- Ação 2: [passo 2]
- Resultado: [output esperado]

## 4. Requisitos funcionais
| ID | Requisito | Prioridade |
|---|---|---|
| AF-1 | Receber mensagem de [CANAL] | P0 |
| AF-2 | Validar dados de entrada | P0 |
| AF-3 | Criar registro no CRM | P0 |
| AF-4 | Enviar notificação | P1 |
| AF-5 | Gerar relatório diário | P2 |

## 5. Requisitos não-funcionais
- Latência < 5s entre trigger e ação
- 99% uptime (n8n cloud)
- Retry automático em falhas

## 6. Integrações
| Sistema | Tipo | Dados |
|---|---|---|
| WhatsApp | Inbound | Mensagens |
| CRM | Outbound | Leads |
| Planilha | Outbound | Logs |

## 7. Critérios de aceite
- [ ] Fluxo n8n executa sem erro
- [ ] Mensagem teste gera registro no CRM
- [ ] Falha simulada dispara retry
- [ ] Relatório diário chega no email

## 8. Riscos e mitigações
| Risco | Mitigação |
|---|---|
| WhatsApp bloqueio | Fallback para email |
| API fora do ar | Fila + retry |
| Dados duplicados | Deduplicação por telefone |
