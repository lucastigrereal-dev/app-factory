# SKILL: create-dashboard

## Nome
create-dashboard

## Descrição
Produz o pacote inicial para um painel de análises, incluindo PRD, blueprint de métricas e layout de widgets.

## Quando usar
Quando for necessário visualizar indicadores de desempenho a partir de dados existentes (por exemplo, vendas, usuários, métricas de produto).

## Inputs
- Lista de métricas desejadas (ex.: visitantes, conversões, churn).
- Períodos de comparação.
- Requisitos de visualização (gráficos de barras, linhas, tabelas).

## Outputs
- PRD em Markdown definindo objetivos e indicadores.
- Blueprint YAML com definição de widgets e datasets.
- Plano de frontend com esquema das telas e componentes.
- Critérios de aceitação para cada métrica.

## Ferramentas permitidas
- Templates em `/templates/dashboard`
- Escrita em `/docs` e `/config`

## Ferramentas proibidas
- Acesso a bancos de dados reais.
- Geração de gráficos interativos.

## Risco
**R1** — Geração de documentação.

## Aprovação humana necessária
Não, até CP‑1.

## Etapas
1. Criar o PRD baseando-se nas métricas informadas.
2. Preencher o blueprint `product_blueprint.yaml` com widgets (gráfico de barras, linhas etc.).
3. Elaborar o plano de frontend com layout de dashboard.
4. Definir critérios de aceitação (valores máximos/mínimos e performance).

## Gates
- CP‑1: Aprovação do PRD e blueprint.
- CP‑2: Aprovação do frontend e critérios.

## Artefatos gerados
- `/docs/dashboard_PRD.md`
- `/templates/dashboard/product_blueprint.yaml` adaptado
- `/docs/dashboard_frontend_plan.md`
- `/docs/dashboard_acceptance_criteria.md`

## Testes esperados
- Verificação de formato do blueprint.
- Revisão da definição de métricas.

## Failure modes
- Métricas incorretas ou irrelevantes.
- Layout confuso.
- Critérios de sucesso não mensuráveis.

## Exemplo de uso
Solicitar: “crie um dashboard para acompanhar vendas mensais e churn”.