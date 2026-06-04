# REAUDIT REPORT — App Factory V7

## Contexto

Esta re‑auditoria foi conduzida após a entrega da **V6** do System Creation OS (App Factory) para avaliar em profundidade o que o pacote anterior conseguiu atender, o que permaneceu superficial ou ausente e quais melhorias foram implementadas nesta **V7**.  O objetivo é garantir que a fábrica de apps não seja apenas um conjunto de arquivos bonitos, mas uma plataforma empresarial aplicável, auditável, segura e pronta para integração com o **OMNIS** e execução pelo **Claude Code**.

## Metodologia de Auditoria

1. **Leitura completa** de todos os arquivos fornecidos pelo usuário (zips, markdowns, schemas), incluindo o pacote V6 (`app_factory_v6`), os pacotes anteriores (`system_creation_os`, `system-creation-os-file-pack-final`), relatórios de auditoria e documentos de melhoria.
2. **Pesquisa cruzada** com documentos do repositório interno `omnis-control` (via API GitHub), em especial o manual das waves do App Factory【800680552272303†L0-L55】 e o esqueleto determinístico definido em `P11_APP_FACTORY_SKELETON.md`.
3. **Comparação** entre as especificações originais presentes no prompt de upgrade (risk engine, gate matrix, command pack, agent hardening, skill template, rubricas de PRD/blueprint, etc.) e o que foi efetivamente entregue na V6.
4. **Classificação** de cada arquivo e diretório segundo as ações: **CREATE**, **REUSE**, **VERIFY**, **DEFER** ou **ARCHIVE**.
5. **Identificação de gaps** técnicos, de governança, de segurança e de implementação real.

## O que estava bom na V6

1. **Documentação canônica**: A V6 consolidou a visão do System Creation OS com `SYSTEM_CANON.md`, `SYSTEM_STATE.md`, `GOVERNANCE_POLICY.md`, `README.md` e vários protocolos.  Estes arquivos definem missão, pipeline obrigatório, princípios de segurança (dry_run por padrão, riscos R0‑R3), integrações com Akasha/Kratos e regras invioláveis.
2. **Novos modelos de custos e observabilidade**: A V6 adicionou `docs/COST_MODEL.md` e `docs/OBSERVABILITY_MODEL.md`, iniciando o rastreamento de tokens e custos, além de sugerir integração com OpenTelemetry e Langfuse.
3. **Rubrica de qualidade de PRD**: O arquivo `docs/PRD_QUALITY_RUBRIC.md` introduziu critérios objetivos para avaliar clareza, escopo, requisitos e riscos dos PRDs.
4. **Esquema de custos e CLI**: Foram incluídos módulos `src/cost_tracking/cost_tracker.py` e `src/cli/appfactory_cli.py`, além de testes iniciais garantindo o modo dry_run.
5. **Manifesto e arquivos machine‑readable**: `FILE_MANIFEST.yaml`, `config/gates.yaml`, `config/risk_policy.yaml` e `config/models.yaml` começaram a transformar a documentação em contratos legíveis por máquina.
6. **Estrutura de skills e agentes**: A V6 incluiu dezenas de skills e agentes organizados em `.claude/commands/` e `.claude/agents/`, além de templates iniciais, fornecendo uma base para orquestração.

## O que estava fraco ou incompleto

1. **Integração com pipeline real**: A V6 não incorporou o pipeline determinístico já implementado no repositório `omnis-control`, que possui classes `AppIdea`, `AppRequirement`, `AppBlueprint` e `AppArtifact` e um planner determinístico【800680552272303†L0-L55】.  A fábrica continuou conceptual sem código para extrair requisitos, desenhar blueprints ou gerar estruturas reais.
2. **Geração de UI e código**: Não havia nenhum mecanismo para gerar código real de frontend, backend ou banco.  A qualidade do blueprint ainda era “poesia técnica” sem vínculos a arquivos de template ou scaffolding.
3. **Pre‑commit e CI/CD**: O pack não incluía arquivos `.pre-commit-config.yaml`, workflows de GitHub Actions ou ganchos do Claude Code; portanto, nenhuma validação era aplicada antes de merges ou execuções.  O road‑map mencionava gates mas não fornecia automação.
4. **APPLY_ROOT e master prompt**: Faltava um script ou documento que explicasse como aplicar o pacote a um repositório real e um prompt mestre que orientasse o Claude Code a executar as fases com segurança.  Isto podia levar a erros de aplicação.
5. **Mapa de aplicação file‑by‑file**: O manifesto listava os arquivos, mas não informava claramente onde e como aplicá‑los num projeto de destino, nem quais eram obrigatórios ou opcionais.
6. **Testes insuficientes**: Havia testes básicos para risk classifier e cost tracker, mas faltavam verificações para schemas, manifestos, gates e demais contratos.  Não existia teste E2E que percorresse a pipeline de ponta a ponta.
7. **Observabilidade e custos práticos**: O modelo de custos era conceitual; faltava instrumentação real para capturar tokens, latência e eventos em cada módulo e expor via Langfuse ou Kratos.
8. **União com a arquitetura existente**: A V6 ignorava a distinção entre o App Factory determinístico do `omnis-control` e a abordagem agentic; não havia diretrizes sobre como combinar ambos (por exemplo, usar o planner determinístico como fallback para LLMs ou como verificador de consistência).

## O que faltou na V6

1. **Comandos e prompts finais**: O pacote não incluía prompts `appfactory-audit`, `appfactory-plan`, `appfactory-validate` e `appfactory-export` descritos nas melhorias, nem um `CLAUDE_CODE_MASTER_PROMPT.md` para orquestrar as fases.
2. **Docs ausentes listadas na roadmap**: Arquivos como `MANIFESTO_APP_FACTORY.md`, `APP_FACTORY_CONSTITUTION.md`, `PROTOCOL_SECTOR.md`, `AGENTS.md`, `.claude/settings.json` e `.pre-commit-config.yaml` foram mencionados mas não entregues.
3. **Quality Gates Enterprise**: O arquivo `ENTERPRISE_QUALITY_GATES.md` não existia, deixando os gates sem definição formal e sem mapeamento de entrada, saída, verificação automática, verificação humana e ações de correção.
4. **Schemas adicionais**: Faltavam `blueprint_schema.json` e `scaffold_plan_schema.json` para validar as saídas de blueprint e planos de scaffolding.
5. **Mapa de Aplicação**: Não existia `FILE_BY_FILE_APPLICATION_MAP.md` detalhando onde aplicar cada artefato e que risco representava.
6. **Integração OMNIS**: Não havia documentação concreta sobre como conectar a fábrica com os serviços reais do OMNIS, como reaproveitar as classes de planner e status tracker ou como sincronizar com a Akasha e o Kratos existentes.

## O que foi expandido na V7

1. **Reaudit e relatório completo**: Este documento (REAUDIT_REPORT.md) analisa a V6, compara com o manual de waves do App Factory【800680552272303†L0-L55】 e com o prompt de melhoria, registra onde a V6 acertou e errou e define ações para a V7.
2. **Mapa de aplicação**: Criamos `FILE_BY_FILE_APPLICATION_MAP.md` que associa cada pasta e arquivo a seu propósito, ação recomendada e risco.  Isso facilita a aplicação real do pacote e dá transparência sobre criação, reutilização ou verificação de artefatos.
3. **Master prompt**: Adicionamos `CLAUDE_CODE_MASTER_PROMPT.md`, que instrui o Claude Code a executar Fase 0 (auditoria read‑only) e Fase 1 (criação/melhoria) com respeito às políticas de risco e gates.  Ele documenta ferramentas permitidas, entradas esperadas e outputs.
4. **Script de aplicação**: O novo `__APPLY_ROOT__/apply_root.md` detalha como preparar o ambiente, executar testes e copiar arquivos para um repositório alvo.  Ele inclui comandos para instalar dependências, configurar pre‑commit e rodar o CLI.
5. **Novos schemas e testes**: Introduzimos `schemas/blueprint_schema.json` e `schemas/scaffold_plan_schema.json` com stubs básicos e testamos sua existência em `tests/unit/test_blueprint_schema.py` e `tests/unit/test_scaffold_plan_schema.py`.  Criamos testes skeleton para o manifesto e os gates.
6. **Documentação ampliada**: Criamos `docs/SYSTEM_DESIGN_DOCUMENT.md` e `docs/REAUDIT_SUMMARY.md`.  Atualizamos PRD e blueprint com rubricas de avaliação e referências cruzadas.  Ajustamos `ROADMAP.md` com quatro waves de dez blocos cada, alinhadas ao roadmap de evolução.
7. **Integração com OMNIS**: Inserimos notas no `README.md` e `docs/OMNIS_APP_FACTORY_BRIDGE.md` sobre como reaproveitar o planner determinístico (`AppFactoryPlanner`), as classes de modelo (`AppIdea` etc.) e o status tracker do repositório `omnis-control`.  Propomos tratá‑los como fallback ou verificadores de consistência para os resultados gerados por LLMs.
8. **Políticas revisadas**: Ajustamos `config/risk_policy.yaml` e `config/gates.yaml` para incluir verificação de custo, segurança e observabilidade em cada etapa.  O risco R3 agora exige revisão humana obrigatória mesmo em dry_run.

## Próximos Passos Recomendados

1. **Gerador de código**: Prototipar subagentes que usem os templates de scaffolding para gerar projetos Next.js + Supabase + tests.  Avaliar integração com frameworks como `v0` ou `shadcn/ui` para UI.
2. **CI/CD real**: Adicionar `.github/workflows/` com pipelines de lint, testes, scan de segurança e deploy preview.  Criar `.pre-commit-config.yaml` e ganchos para o Claude Code.
3. **Testes E2E**: Desenvolver um teste end‑to‑end que verifique a passagem da ideia até o handoff, comparando com o pipeline determinístico.
4. **Observabilidade real**: Integrar a coleta de métricas (custo, tokens, latência) com Langfuse ou OpenTelemetry, alimentando o Kratos.
5. **Upgrade de agentes**: Transformar os prompts dos agentes em sub‑modules de código, definindo escopos, inputs, outputs, ferramentas permitidas e validação automática.
6. **Constituição e Protocolos**: Redigir a `APP_FACTORY_CONSTITUTION.md` e os protocolos de setor, subsector, squad e skill, conforme listados em `APP_FACTORY_MDs_FALTANTES_ROADMAP.md`.  Esses documentos darão base formal para crescimento futuro.

---

*Esta re‑auditoria foi gerada em 04/06/2026 e deve acompanhar a entrega do pacote **APP_FACTORY_EXPONENTIAL_EVOLUTION_PACK_V7***.