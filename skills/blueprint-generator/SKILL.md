# Skill: blueprint-generator

**Descrição**

Cria um blueprint técnico detalhado com base no PRD e no plano aprovado. Define a arquitetura do sistema, módulos, integrações, banco de dados, API design, plano de UI e requisitos de testes.

**Quando usar**

Após a aprovação do PRD e antes de iniciar a prototipagem ou o scaffold do repositório. O blueprint funciona como contrato técnico.

**Inputs**

- ``docs/PRD.md`` aprovado.
- Especificações iniciais de arquitetura (quando disponíveis).

**Outputs**

- ``docs/BLUEPRINT.md`` completo.
- Atualização de ``config/system.yaml`` para refletir os módulos propostos.

**Ferramentas permitidas**

- Escrita e leitura de arquivos Markdown e YAML.
- Diagramas ASCII ou links externos embutidos.

**Ferramentas proibidas**

- Execução de migrações de banco.
- Instalação de dependências externas.

**Risco**

``R2`` — Define estrutura de código e arquivos de configuração; requer revisão.

**Aprovação humana necessária**

Sim. O blueprint deve ser aprovado por arquitetura e liderança técnica.

**Etapas**

1. Ler o PRD aprovado.
2. Identificar módulos, entidades e integrações.
3. Descrever a arquitetura e adicionar diagramas.
4. Atualizar ``config/system.yaml`` com módulos e flags.
5. Salvar o blueprint e marcá‑lo como ``DRAFT`` até aprovação.

**Gates**

Deve passar pelo gate CP‑2 (validação de blueprint) antes de seguir para o scaffold.

**Artefatos gerados**

- ``docs/BLUEPRINT.md``
- ``config/system.yaml`` atualizado.

**Testes esperados**

- Verificar se todos os módulos definidos no PRD aparecem no blueprint.
- Validar a sintaxe YAML após atualização.

**Failure modes**

- Omissão de dependências críticas.
- Inconsistência entre blueprint e PRD.

**Exemplo de uso**

```
from skills.blueprint_generator import generate_blueprint
generate_blueprint("docs/PRD.md", "docs/BLUEPRINT.md", "config/system.yaml")
```