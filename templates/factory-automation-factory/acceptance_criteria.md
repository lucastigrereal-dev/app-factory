# Critérios de Aceite — Automation Factory

## Funcionais
- [ ] Fluxo n8n executa end-to-end sem erro manual
- [ ] Trigger responde em < 5 segundos
- [ ] CRM recebe dados formatados corretamente
- [ ] Notificação enviada no canal correto
- [ ] Retry funciona em falha simulada

## Não-funcionais
- [ ] Uptime > 95% em 7 dias
- [ ] Zero duplicatas em dedup test
- [ ] API keys nunca expostas em logs
- [ ] Fallback ativa quando primário falha

## Performance
- [ ] 10 execuções/minuto sem fila
- [ ] 50 execuções/minuto com fila
- [ ] Memory usage < 512MB
