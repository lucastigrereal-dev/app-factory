# FILE: .claude/commands/appfactory-scaffold.md

## Objetivo
Gerar a estrutura inicial do repositório (scaffold) do produto, incluindo pastas, arquivos básicos e dependências mínimas.

## Quando usar
Após o plano de testes ser aprovado (`appfactory-test-plan`) e quando todos os documentos anteriores estiverem validados (até CP‑2).

## Inputs esperados
* Todos os artefatos anteriores (PRD, blueprint, schema, contrato de API, frontend plan, test plan).
* Configurações padrão de projeto (linguagem, framework).

## Outputs esperados
* Pasta com a estrutura de diretórios e arquivos iniciais (README, package.json, etc.) dentro de `src/` ou em diretório separado.
* Relatório em Markdown descrevendo o scaffold.

## Paths permitidos
`/src/*`, `/docs/*` e `/templates/*`.

## Risco
**R2** — Criação de código interno (dry‑run).  Não faz push nem deploy.

## Regras de segurança
* `dry_run=True` — todas as ações são simulações.
* Não instalar dependências reais; gerar apenas arquivos com instruções.
* Seguir padrões de código (lint, estrutura modular).

## Critérios de aceite
* A estrutura segue os padrões definidos (monólito modular, etc.).
* Todos os arquivos essenciais estão presentes.
* Não há segredo ou código malicioso.

## Proibições
* Não executar `npm install` ou equivalente.
* Não inicializar repositórios remotos sem aprovação.