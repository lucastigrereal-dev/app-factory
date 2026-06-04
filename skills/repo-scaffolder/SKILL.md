# Skill: repo-scaffolder

**Descrição**

Gera a estrutura inicial do repositório com base no blueprint aprovado. Cria diretórios, arquivos padrão, configurações iniciais e exemplos mínimos de código para cada módulo. Esta skill não implementa funcionalidades; apenas prepara o terreno.

**Quando usar**

Após a validação do blueprint (gate CP‑2) e antes da escrita de código de negócios. O scaffold assegura consistência estrutural para o desenvolvimento.

**Inputs**

- ``docs/BLUEPRINT.md`` aprovado.
- ``config/system.yaml``.

**Outputs**

- Diretório de projeto (por exemplo ``src/``) com subpastas criadas.
- Arquivos ``__init__.py`` para cada pacote.
- Placeholders de código em Python com docstrings.

**Ferramentas permitidas**

- Criação de arquivos e diretórios locais.
- Escrita de texto em Python, Markdown e YAML.

**Ferramentas proibidas**

- Execução de código gerado.
- Instalação de pacotes externos.

**Risco**

``R2`` — Criação de estrutura de código. Necessita revisão, mas não executa.

**Aprovação humana necessária**

Sim. O scaffolding final deve ser aprovado antes de commit no repositório real.

**Etapas**

1. Analisar ``docs/BLUEPRINT.md`` para listar módulos.
2. Criar diretórios e arquivos ``__init__.py``.
3. Gerar placeholders com documentação e anotações ``TODO``.
4. Atualizar ``FILE_MANIFEST.yaml`` com arquivos criados.

**Gates**

Deve passar pelo gate CP‑3 (validação de scaffold) antes da implementação.

**Artefatos gerados**

- Estrutura de diretórios e arquivos base.

**Testes esperados**

- Verificar existência de diretórios e arquivos conforme blueprint.
- Verificar que cada arquivo contém docstring e ``TODO``.

**Failure modes**

- Diretórios criados incorretamente.
- Faltam arquivos base em algum módulo.

**Exemplo de uso**

```
from skills.repo_scaffolder import scaffold_repo
scaffold_repo("docs/BLUEPRINT.md", base_dir="src/")
```