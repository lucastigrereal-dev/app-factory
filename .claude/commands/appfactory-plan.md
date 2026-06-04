# FILE: .claude/commands/appfactory-plan.md

## Objetivo
Elaborar um plano de ação (Fase 1) para criação ou melhoria dos artefatos
necessários ao desenvolvimento de um produto.  Este comando toma como
entrada o resultado da auditoria e gera uma matriz de decisão indicando
quais artefatos devem ser criados, reutilizados, verificados, adiados ou
arquivados, e em que ordem.

## Quando usar
Após concluir a auditoria de Fase 0 e antes de iniciar qualquer criação
de arquivo ou código.  Este comando orienta a execução segura de novas
waves e ajuda a priorizar trabalho.

## Inputs esperados
* `upgrade_reports/AUDIT_READONLY_REPORT.md` — resultados da auditoria
* Política de risco (`config/risk_policy.yaml`)
* Definição de gates (`config/gates.yaml`)

## Outputs esperados
* `upgrade_reports/DECISION_MATRIX.md` — planilha com colunas:
  - item
  - tipo (doc, config, code, schema, test, etc.)
  - estado atual (exists, missing, outdated)
  - decisão (CREATE, REUSE, VERIFY, DEFER, ARCHIVE)
  - motivo
  - risco (R0–R3)
  - dono sugerido
  - arquivos afetados
  - teste necessário
  - critério de pronto
* Atualização do `upgrade_reports/FILE_MANIFEST_UPDATED.yaml` com ações sugeridas.

## Paths permitidos
`upgrade_reports/`, `config/`, `docs/`, `schemas/`.  Nenhum código ou
template deve ser criado nesta fase.

## Risco
**R0–R1** — O plano é gerado sem executar código ou criar arquivos em diretórios
de produção.  Pode modificar arquivos de planejamento dentro de
`upgrade_reports/`.

## Regras de segurança
* Classificar cada decisão com um nível de risco.
* Verificar se qualquer item de risco R2 ou R3 exige aprovação adicional.
* Não remover ou sobrescrever arquivos existentes; planejar antes de agir.

## Critérios de aceite
* Matriz de decisão cobre todos os itens relevantes.
* Cada linha tem motivo e critério de pronto claro.
* Ações com risco R2/R3 possuem `dry_run=True` e aguardam aprovação.

## Proibições
* Não criar arquivos de código ou modificar pastas fora de `upgrade_reports/`.
* Não prosseguir para execução sem aprovação do owner.