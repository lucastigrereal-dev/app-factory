# FILE: .claude/commands/appfactory-schema.md

## Objetivo
Gerar o plano de banco de dados (schema) para um produto digital com base no PRD e no blueprint.

## Quando usar
Após gerar o PRD (`appfactory-intake`) e o blueprint (`appfactory-blueprint`), e antes de definir o contrato de API.

## Inputs esperados
* PRD em Markdown (`docs/PRD.md` ou similar)
* Blueprint em Markdown/YAML (`docs/BLUEPRINT.md` ou arquivo sob `templates/`)
* Qualquer configuração extra em `config/system.yaml`

## Outputs esperados
* Um arquivo YAML no diretório `config/` descrevendo o schema (tabelas, colunas, tipos e relações).
* Um relatório em Markdown no diretório `docs/` explicando as decisões do schema.

## Paths permitidos
`/config/*`, `/docs/*` e `/templates/*`.  Não criar nada fora destes caminhos.

## Risco
**R1** — Criação de documentação e configuração interna (sem side effects externos).

## Regras de segurança
* `dry_run=True` por padrão; nunca aplica migrações diretamente.
* Nunca incluir segredos ou dados sensíveis no schema.
* Submeter o schema para revisão humana (CP‑1) antes de considerá-lo final.

## Critérios de aceite
* O arquivo YAML é válido e segue o padrão definido em `docs/DB_SCHEMA.md`.
* Todas as entidades do PRD são representadas.
* Não há campos indefinidos ou vazios.

## Proibições
* Não executar migrações no banco real.
* Não criar schemas para ambientes externos sem aprovação humana.