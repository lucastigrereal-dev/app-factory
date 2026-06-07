# FILE: .claude/commands/appfactory-api-contract.md

## Objetivo
Gerar o contrato de API (OpenAPI/Swagger) a partir do PRD, blueprint e schema planejado.

## Quando usar
Depois de planejar o schema (`appfactory-schema`) e antes de gerar o frontend e os testes.

## Inputs esperados
* Schema do banco como YAML (em `config/`)
* PRD e blueprint para contexto adicional
* Política de risco (`config/risk_policy.yaml`)

## Outputs esperados
* Um arquivo YAML/JSON em `config/` contendo a especificação da API.
* Um documento em Markdown resumindo endpoints e justificativas.

## Paths permitidos
`/config/*` e `/docs/*`.

## Risco
**R1** — Criação de especificações internas.

## Regras de segurança
* Não incluir URLs reais ou segredos.
* Seguir as diretrizes de `docs/API_CONTRACTS.md`.
* Validar a especificação com uma ferramenta de lint.

## Critérios de aceite
* Endpoints para cada recurso do schema.
* Métodos HTTP corretos e códigos de resposta.
* Descrições e exemplos incluídos.

## Proibições
* Não publicar o contrato em repositórios públicos sem aprovação.
* Não gerar código de cliente/servidor automaticamente (apenas contrato).