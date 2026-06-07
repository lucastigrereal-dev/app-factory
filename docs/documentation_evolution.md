# documentação de evolução exponencial do System Creation OS (FactoryOS IA)

Esta documentação complementa o **Product Requirements Document (PRD)** e o **Blueprint** de evolução exponencial do System Creation OS (FactoryOS IA). Ela consolida as principais melhorias identificadas durante a auditoria técnica e define diretrizes práticas para implementar essas mudanças de forma incremental e controlada.

## Visão Geral

O objetivo da evolução exponencial é transformar a App Factory em um **sistema operacional de criação de produtos** totalmente auditável, com rastreabilidade entre documentos e código, engine de risco, gates de qualidade executáveis e testes end‑to‑end. Esta visão se inspira em benchmarks como LangGraph, Lovable, v0, Replit Agent, Bolt.new e em guidelines de arquitetura empresarial.

Esta seção cobre três pilares:

1. **Governança Executável** – Converter documentação em políticas executáveis (YAML e código) para que a IA não viole regras como ordem das etapas, classificação de risco e aprovação humana.
2. **Rastreabilidade e Quality Gates** – Introduzir IDs de requisitos, matrizes de traceabilidade e rubricas de qualidade para PRD, blueprint e contratos. Os gates descritos no arquivo `ENTERPRISE_QUALITY_GATES.md` devem migrar para `config/gates.yaml`, permitindo validação automática e bloqueios programáticos para cada etapa.
3. **Testes e Observabilidade** – Criar skeletons de teste unitário, integração e E2E para a própria factory. Cada nova função deve vir acompanhada de testes automatizados e logs instrumentados, com métricas de custo/token por step.

## Documentos Canônicos e Hierarquia

Durante a auditoria, foram identificados diversos documentos canônicos já existentes (constituição, protocolos e registries) com nível de completude entre 65% e 90%. A hierarquia de autoridade recomendada é:

1. **APPFACTORY_CONSTITUTION.md** – Fonte principal de princípios, objetivos e restrições.
2. **PROTOCOL_APPROVAL_GATES.md** e **ENTERPRISE_QUALITY_GATES.md** – Definem quais gates são obrigatórios e suas métricas.
3. **PROTOCOL_*.md** (sector, squad, subagent, skill, workflow, MCP, memory) – Especificam papéis, responsabilidades e comunicação.
4. **Registros e Manifestos** – Mantêm inventário de documentos, skills, agentes, squads e decisões.
5. **Memória Akasha** – Armazena eventos e aprendizados de execuções anteriores.

Qualquer conflito entre documentos deve ser resolvido seguindo a ordem acima. Arquivos legados e notas devem ser arquivados em `99_LEGACY_NOTES` após migração.

## Machine‑Readable Configs

Para que a factory seja executável, vários arquivos Markdown precisam migrar para formatos consumíveis por código. É imperativo criar os seguintes YAML/JSON em `config/` e `schemas/`:

* **`config/gates.yaml`** – Lista de gates obrigatórios (IDEA INTAKE, DISCOVERY, PRD QUALITY, BLUEPRINT COHERENCE, SCHEMA SAFETY, etc.) com seus critérios automáticos, revisões humanas e pontuação mínima. Inspirado em `ENTERPRISE_QUALITY_GATES.md`.
* **`config/risk_policy.yaml`** – Define as ações permitidas por classificação de risco (R0–R3), se `dry_run` é obrigatório e quem precisa aprovar. Baseado nos protocolos de risco.
* **`config/skills.yaml`** – Registro de skills disponíveis, com campos como `allowed_tools`, `forbidden_tools`, `risk_level`, `execution_steps`, `validation_gates`, `generated_artifacts` e testes obrigatórios. Criar a partir do template em `PERFECT_STRUCTURE.md`.
* **`config/models.yaml`** – Permite roteamento entre modelos (e.g., Claude, GPT‑4, Ollama) definindo custos e perfis de uso para cada step.
* **`config/templates.yaml`** e **`config/factories.yaml`** – Catalogam templates por tipo de produto (landing page, CRM, SaaS, dashboard, automação) e mapeiam o pipeline de criação correspondente.
* **`schemas/idea_input_schema.json`**, **`schemas/prd_output_schema.json`**, **`schemas/handoff_report_schema.json`**, etc. – Devem ser utilizados como base para validação de entradas e saídas em cada etapa. Atualize estes schemas para incluir campos de qualidade (ex.: `quality_score`, `implementability_score`, `risk_flags`).

## Qualidade e Gates

O arquivo `ENTERPRISE_QUALITY_GATES.md` (incluído no pacote de upgrade) define 12 gates obrigatórios com critérios automáticos e revisões humanas. Essas regras devem ser transformadas em código para que a pipeline da factory faça bloqueios e warnings conforme a pontuação atingida. Recomenda‑se criar uma classe `GateRunner` que:

1. Recebe o nome do gate, o artefato de entrada e o contexto.
2. Executa checks automáticos (ex.: validação de esquema, presença de campos, escore mínimo) usando scripts e testes automatizados.
3. Solicita aprovação humana quando necessário (ex.: se o gate é WARN ou falha crítica).
4. Registra cada verificação e decisão em `AKASHA` e atualiza a memória com evento `gate_completed`.

Além disso, use a **rubrica de qualidade do PRD** e a **verificação de coherência do blueprint** como exemplos para criar funções de scoring automáticas em `src/quality/`. Cada PRD/blueprint gerado deve conter os campos `quality_score` ou `implementability_score` para permitir gating programático.

## Testes e Skeletons

Para garantir a confiabilidade da factory, a estrutura `tests/` deve ser populada com skeletons de:

* `test_risk_classifier.py` – Valida que a classificação de risco está de acordo com a política. Exemplo: uma ação de scaffolding sem `dry_run=True` deve ser classificada como R2 e bloqueada.
* `test_gate_config.py` – Garante que todos os gates definidos em `config/gates.yaml` têm os campos esperados e thresholds numéricos válidos.
* `test_prd_output_schema.py`, `test_blueprint_schema.py`, etc. – Verificam a conformidade dos schemas JSON.
* `test_golden_path.py` – Um teste end‑to‑end que simula a criação de um produto simples (idea → PRD → blueprint → scaffold plan → handoff) para detectar regressões rapidamente.

Inclua também fixtures como `sample_idea.json`, `sample_prd.json` e `sample_blueprint.json` para alimentar os testes. Observabilidade das execuções deve ser registrada via Langfuse ou outra solução, com logging de custo por step e IDs correlacionados ao Akasha.

## Observabilidade e Cost Tracking

Implemente um módulo `src/cost_tracking/` que intercepte cada chamada de agente ou skill, registre o número de tokens consumidos, modelo utilizado, tempo de execução e custo estimado. Esses dados devem alimentar um ledger consultável no cockpit KRATOS e ajudar a otimizar a factory. Combine com um módulo de observabilidade (`src/observability/`) que exporte traces via OpenTelemetry para ferramentas como Sentry ou Langfuse.

## Próximos Passos

1. **Consolidar a Estrutura de Pastas** – Use a árvore proposta em `PERFECT_STRUCTURE.md` e adapte conforme as necessidades do projeto real. Garanta que cada nova pasta ou arquivo adicione valor (CREATE), reutilize (REUSE), exija verificação (VERIFY) ou possa ser adiado (DEFER).
2. **Automatizar o Risk Engine e Gate Runner** – Crie os skeletons de `risk_classifier.py` e `gate_runner.py` em `src/governance/` e `src/validation/` para que a IA avalie risco e qualidade antes de executar ações.
3. **Converter Protocolos e Registros** – Migre trechos críticos de Markdown para YAML ou JSON e escreva loaders em `src/config/` para consumi‑los.
4. **Refatorar Agentes e Skills** – Adapte as definições de agentes e skills existentes para seguir o template oficial (incluindo `allowed_tools`, `forbidden_tools`, `risk_level`, `validation_gates` e `tests`).
5. **Implementar Memory Writeback e KRATOS Snapshot** – Crie skeletons de `memory_writeback.py` e `kratos_snapshot.py` para emitir eventos com dados estruturados (usando `schemas/akasha_writeback.schema.yaml` e `kratos_snapshot.schema.yaml` do pacote `system-creation-os-file-pack-final`).
6. **Planejar MVP Real** – Antes de tentar cobrir todos os cenários, priorize um produto real simples (e.g., landing page ou app para hotéis) que percorra o pipeline mínimo: ideação → PRD → blueprint → schema → API contract → scaffold plan → handoff.

Ao seguir estas diretrizes, a App Factory evoluirá de um conjunto de documentos e intenções para uma plataforma enterprise executável, capaz de gerar produtos digitais com governança, segurança e rastreabilidade.