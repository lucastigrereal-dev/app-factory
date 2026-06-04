# FILE: .claude/commands/appfactory-validate.md

## Objetivo
Executar validações automáticas e gates de qualidade nos artefatos gerados.
Este comando percorre cada etapa do pipeline (PRD, blueprint, schema,
API, scaffold plan, etc.) e verifica se os critérios definidos em
`config/gates.yaml` e `docs/ENTERPRISE_QUALITY_GATES.md` foram atendidos.

## Quando usar
Após gerar artefatos (Fase 1) e antes de solicitar aprovação final para
execução ou handoff.  Pode ser usado de forma incremental para validar
artefatos parciais.

## Inputs esperados
* Artefatos a serem validados (PRD, blueprint, schema, API contracts, etc.)
* Configuração de gates (`config/gates.yaml`)
* Risk policy (`config/risk_policy.yaml`)

## Outputs esperados
* Relatório de validação indicando:
  - Gates executados e se passaram ou falharam
  - Pontuações de qualidade (PRD, blueprint, etc.)
  - Lista de ações necessárias para correção

## Paths permitidos
`docs/`, `schemas/`, `config/`, `upgrade_reports/`.  Não criar ou
modificar código neste comando; apenas ler e relatar.

## Risco
**R0–R1** — Operação de leitura e cálculo.  Não há efeitos externos.

## Regras de segurança
* Validar cada artefato contra seu JSON schema correspondente.
* Verificar se quality_score ou implementability_score atendem ao mínimo.
* Bloquear avanço se encontrar falhas graves (R2+), exceto com aprovação.

## Critérios de aceite
* Todas as seções obrigatórias dos artefatos são verificadas.
* Relatório inclui recomendações de correção para cada falha.
* Os gates definidos são respeitados (não passar se falhar).

## Proibições
* Não ajustar ou reescrever artefatos automaticamente nesta fase.
* Não ignorar falhas críticas em nome da velocidade.