# FILE: .claude/commands/appfactory-frontend-plan.md

## Objetivo
Elaborar o plano de interface (frontend) para o produto, mapeando telas, fluxos e componentes.

## Quando usar
Após o contrato de API estar definido (`appfactory-api-contract`) e antes de escrever o plano de testes.

## Inputs esperados
* PRD, blueprint e contrato de API.
* Templates de design (ex.: `templates/landing_page/`).

## Outputs esperados
* Um arquivo Markdown em `docs/` descrevendo as telas, fluxos e componentes.
* Um esboço de wireframe opcional em formato texto ou imagem.

## Paths permitidos
`/docs/*` e `/templates/*`.

## Risco
**R1** — Definição de documentação interna.

## Regras de segurança
* Não incluir imagens externas sem licença.
* Seguir guidelines de UX do projeto.
* Separar claramente o que é conteúdo estático e dinâmico.

## Critérios de aceite
* Todas as funcionalidades do PRD são mapeadas para telas.
* Há indicação de chamadas de API para cada ação do usuário.
* O documento serve de insumo para designers e desenvolvedores.

## Proibições
* Não criar componentes reais ou arquivos de código nesta etapa.
* Não modificar templates originais sem criar uma cópia.