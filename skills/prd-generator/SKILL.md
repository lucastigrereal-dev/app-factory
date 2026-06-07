# Skill: prd-generator

**Descrição**

Gera um Documento de Requisitos de Produto (PRD) a partir de um ``MissionPackage`` e de dados coletados de stakeholders. Estrutura o PRD em seções claras, seguindo o template fornecido, e garante que os objetivos e requisitos estejam documentados.

**Quando usar**

Depois que o intake foi concluído e é necessário formalizar o escopo do produto antes de iniciar o blueprint.

**Inputs**

- Arquivo ``mission_package.json``.
- Respostas a entrevistas com usuários e stakeholders.

**Outputs**

- ``docs/PRD.md`` atualizado seguindo o ``PRD_TEMPLATE.md``.

**Ferramentas permitidas**

- Leitura de JSON e Markdown.
- Escrita de arquivos Markdown em ``docs/``.

**Ferramentas proibidas**

- Acesso à internet.
- Execução de código externo.

**Risco**

``R1`` — Criação de documento sem efeitos colaterais externos.

**Aprovação humana necessária**

Sim. O PRD deve ser revisado e aprovado por stakeholders de negócio.

**Etapas**

1. Carregar o ``MissionPackage``.
2. Criar esqueleto do PRD com seções padrão.
3. Preencher cada seção usando informações do intake e das entrevistas.
4. Salvar ``docs/PRD.md``.
5. Marcar o PRD como ``DRAFT`` até revisão.

**Gates**

Este skill deve passar pelo gate de validação CP‑1 antes de avançar para a fase de blueprint.

**Artefatos gerados**

- ``docs/PRD.md``

**Testes esperados**

- Verificar que todas as seções obrigatórias estão presentes.
- Garantir que o Markdown gerado está bem formatado.

**Failure modes**

- Erros de parsing do JSON de entrada.
- Campos vazios ou não informados.

**Exemplo de uso**

```
from skills.prd_generator import generate_prd
generate_prd("examples/mission_package.json", "docs/PRD.md")
```