# Template: Dashboard Factory

## O que cria
Dashboards internos: KPIs, relatórios, alertas, visualização de dados.

## Quando usar
- Dados dispersos em planilhas
- Necessidade de visão unificada
- Alertas automáticos por threshold
- Relatórios recorrentes para stakeholders

## Produtos típicos
- Dashboard de vendas para hotel
- Painel de métricas de Instagram
- Relatório de ocupação
- Alerta de meta não atingida

## Stack
- **Frontend:** Next.js + Recharts / Chart.js
- **Database:** Supabase / ClickHouse
- **ETL:** n8n / Python scripts
- **Auth:** NextAuth + Supabase

## Riscos
- R1: Dados desatualizados
- R2: Query lenta em grandes volumes
- R3: Acesso não autorizado a dados sensíveis
