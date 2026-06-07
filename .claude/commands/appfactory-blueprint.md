# Command: appfactory-blueprint

**Objetivo**

Gerar um **Blueprint técnico** detalhado a partir do plano de alto nível. O blueprint especifica arquitetura, módulos, banco de dados, APIs, camadas de UI, integrações e plano de testes. Serve como contrato entre produto e engenharia.

**Quando usar**

Após o comando de planejamento (``appfactory-plan``) aprovar o escopo inicial. O blueprint deve preceder qualquer desenvolvimento ou contratação.

**Entradas esperadas**

- Documento ``docs/plan_overview.md``.

**Saídas esperadas**

- ``docs/BLUEPRINT.md`` contendo arquitetura modular, diagramas, dependências, requisitos técnicos e riscos.
- ``config/system.yaml`` atualizado com módulos e feature flags.

**Paths permitidos**

- Escrita em ``docs/BLUEPRINT.md`` e ``config/system.yaml``.

**Risco**

``R2`` — Alteração de documentos de arquitetura e configuração. Não executa código, mas exige validação humana.

**Regras de segurança**

1. Não sobrescrever arquivos existentes sem confirmação humana.
2. Incluir um aviso de ``DRAFT`` no blueprint até aprovação.
3. Respeitar limitações definidas em ``risk_policy.yaml``.

**Critérios de aceite**

- O blueprint cobre módulos (frontend, backend, banco, integrações, IA).
- Contém diagrama ascii ou link para diagrama externo.
- Declara limitações e riscos.

**Proibições**

- Não executar migrações de banco ou criar tabelas reais.
- Não alterar arquivos de código-fonte sem passar pela etapa de scaffold.