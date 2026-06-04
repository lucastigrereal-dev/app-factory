# FILE: .claude/commands/appfactory-test-plan.md

## Objetivo
Gerar um plano de testes cobrindo unidades, integração e aceitação com base no PRD, blueprint, schema e contratos.

## Quando usar
Depois de definir o frontend plan (`appfactory-frontend-plan`) e antes de gerar o scaffold.

## Inputs esperados
* PRD, blueprint, schema e contrato de API.
* Política de validação (`docs/VALIDATION_GATES.md`).

## Outputs esperados
* Um arquivo Markdown em `docs/` listando casos de teste, dados de entrada e critérios de sucesso.
* Esboço de scripts de teste automatizado em pseudo‑código, se aplicável.

## Paths permitidos
`/docs/*`.

## Risco
**R1** — Planejamento e documentação.

## Regras de segurança
* Priorizar casos de erro e validações de segurança.
* Garantir cobertura dos critérios de aceite do PRD.
* Não executar testes reais nesta etapa.

## Critérios de aceite
* O plano cobre todas as funcionalidades críticas.
* Há distinção entre testes unitários, integração e E2E.
* Critérios de sucesso são mensuráveis e claros.

## Proibições
* Não implementar testes antes de o plano ser aprovado.
* Não interagir com serviços externos.