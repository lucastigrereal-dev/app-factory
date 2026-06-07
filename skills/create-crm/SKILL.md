# SKILL: create-crm

## Nome
create-crm

## Descrição
Gera um pacote inicial (PRD, blueprint, plano de frontend, critérios de aceitação) para um CRM básico usando o System Creation OS.  Ideal para times que desejam construir um sistema de relacionamento com clientes com funcionalidades essenciais.

## Quando usar
Quando precisar iniciar a criação de um CRM simplificado para gestão de clientes, contatos e oportunidades de venda.

## Inputs
- Visão geral do negócio (em poucas frases).
- Lista de funcionalidades desejadas (ex.: cadastro de clientes, pipeline de vendas, integração com e‑mail).
- Requisitos não funcionais (multiplataforma, responsivo).

## Outputs
- PRD em Markdown estruturado.
- Blueprint em YAML definindo entidades Account, Contact, Opportunity, e relações.
- Plano de frontend em Markdown com telas para cadastro, listas e pipeline.
- Critérios de aceitação.

## Ferramentas permitidas
- Leitura de templates (`/templates/crm`)
- Escrita em `/docs` e `/config`

## Ferramentas proibidas
- Execução de comandos de rede.
- Escrita em sistemas externos.

## Risco
**R1** — Geração de documentação interna.

## Aprovação humana necessária
Apenas para sair de R2/R3; plano e PRD podem ser gerados diretamente.

## Etapas
1. Adaptar o PRD template com as informações fornecidas.
2. Preencher o blueprint YAML com entidades e relacionamentos.
3. Gerar o plano de frontend com as telas principais (Clientes, Contatos, Oportunidades).
4. Escrever critérios de aceitação baseados nos requisitos.

## Gates
- CP‑1: Revisão do PRD e blueprint.
- CP‑2: Revisão de planos e critérios.

## Artefatos gerados
- `/docs/CRM_PRD.md`
- `/templates/crm/product_blueprint.yaml` (copiado/adaptado)
- `/docs/CRM_frontend_plan.md`
- `/docs/CRM_acceptance_criteria.md`

## Testes esperados
- Validação de schema YAML.
- Revisão manual do PRD.

## Failure modes
- Requisitos ausentes.
- Entidades conflitantes.
- Falta de critérios de aceite claros.

## Exemplo de uso
Solicitar: “crie um CRM simples para controlar clientes e oportunidades de vendas” e seguir as etapas acima.