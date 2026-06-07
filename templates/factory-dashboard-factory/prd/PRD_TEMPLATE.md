# PRD — Dashboard Factory

## Visão
Dashboard de [MÉTRICA] para [PÚBLICO] com atualização [FREQUÊNCIA].

## Problema
[Dados dispersos, relatórios manuais, falta de visão em tempo real]

## Solução
- Integração: APIs e planilhas
- Visualização: Gráficos e KPIs
- Alertas: Thresholds configuráveis
- Exportação: PDF/Excel

## Requisitos
| ID | Requisito | Prio |
|---|---|---|
| DB-1 | Conectar fontes de dados | P0 |
| DB-2 | Visualizar KPIs | P0 |
| DB-3 | Filtros por período | P0 |
| DB-4 | Alertas por email | P1 |
| DB-5 | Exportar relatório | P1 |

## Aceite
- [ ] Dados atualizados em < 5min
- [ ] Dashboard carrega em < 2s
- [ ] Alerta dispara no threshold
- [ ] Export funciona em PDF e Excel
