# Skill: create-landing-page

**Descrição**

Gera um conjunto de artefatos iniciais para uma landing page simples (marketing). Inclui blueprint básico, plano de frontend, critérios de aceitação e estrutura mínima para iniciar o desenvolvimento.

**Quando usar**

Quando um projeto precisa de uma página de marketing para validar interesse ou como entrada de leads antes de construir o produto completo.

**Inputs**

- Briefing da marca/produto.
- Elementos de design (cores, logos) opcionais.

**Outputs**

- Diretório ``templates/landing_page/`` preenchido com:
  - ``TEMPLATE_README.md`` explicando o template.
  - ``product_blueprint.yaml`` com uma estrutura de páginas e seções.
  - ``frontend_plan.template.md`` com instruções de implementação.
  - ``acceptance_criteria.md`` listando requisitos para aprovação.

**Ferramentas permitidas**

- Criação de arquivos Markdown e YAML.
- Uso de placeholders para imagens e conteúdo.

**Ferramentas proibidas**

- Deploy real da landing page.
- Integração com serviços de email sem aprovação.

**Risco**

``R1`` — Geração de template estático.

**Aprovação humana necessária**

Sim. O template deve ser revisto por marketing e design.

**Etapas**

1. Criar diretórios e arquivos em ``templates/landing_page/``.
2. Preencher blueprint YAML com seções (hero, features, call‑to‑action).
3. Escrever plano de frontend com tecnologias sugeridas (HTML, CSS, React).
4. Definir critérios de aceitação (responsividade, velocidade, acessibilidade).

**Gates**

O template deve passar pelo gate CP‑0 de validação de template antes de uso.

**Artefatos gerados**

- ``templates/landing_page/TEMPLATE_README.md``
- ``templates/landing_page/product_blueprint.yaml``
- ``templates/landing_page/frontend_plan.template.md``
- ``templates/landing_page/acceptance_criteria.md``

**Testes esperados**

- Verificação de presença dos arquivos.
- Validação da sintaxe YAML.

**Failure modes**

- Erro de escrita em diretório inexistente.
- Blueprint YAML com campos inválidos.

**Exemplo de uso**

```
from skills.create_landing_page import generate_template
generate_template(briefing="Nova Fintech para pagamentos")
```