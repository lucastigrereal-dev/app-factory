# PRD Template — Marketing Factory

## 1. Visão
Campanha de [OBJETIVO] para [PÚBLICO] via [CANAL].

## 2. Problema
[Descrição da dor de conversão/tráfego]

## 3. Solução
- Canal: [Meta Ads / Google Ads / Email]
- Público: [segmentação]
- Criativo: [formato e mensagem]
- Oferta: [CTA e landing]

## 4. Requisitos funcionais
| ID | Requisito | Prioridade |
|---|---|---|
| MF-1 | Criar campanha no [CANAL] | P0 |
| MF-2 | Segmentar público por [CRITÉRIO] | P0 |
| MF-3 | A/B test de [VARIÁVEL] | P1 |
| MF-4 | Pixel/tracking ativo | P0 |
| MF-5 | Relatório de ROAS | P1 |

## 5. Requisitos não-funcionais
- Latência de relatório < 1h
- Uptime do pixel > 99%
- GDPR/LGPD compliant

## 6. Integrações
| Sistema | Tipo | Dados |
|---|---|---|
| Meta Ads | Bidirecional | Campanhas, leads |
| Google Analytics | Inbound | Eventos |
| CRM | Outbound | Leads, atribuição |

## 7. Critérios de aceite
- [ ] Campanha publicada e ativa
- [ ] Público com > 1000 pessoas
- [ ] Pixel disparando eventos corretamente
- [ ] ROAS > 1.5 em 7 dias
- [ ] Custo por lead < R$50

## 8. Riscos e mitigações
| Risco | Mitigação |
|---|---|
| Conta suspensa | Backup de criativos e públicos |
| CAC alto | Pausar e resegmentar |
| Pixel falho | Teste com evento manual |
