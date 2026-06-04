# CHANGELOG

Todas as mudanças significativas para a evolução do System Creation OS são documentadas aqui.  Este arquivo segue o formato [Keep a Changelog](https://keepachangelog.com/) e utiliza controle de versão semântico.

## [6.0.0] – 2026‑06‑04

### Adicionado

- **Structure V6:** cópia de `perfect_factory_big` reorganizada como `app_factory_v6`, servindo de base para a versão 6.
- **Novos documentos:**
  - `docs/SECURITY_MODEL.md` — descreve princípios, controles e próximos passos para a camada de segurança.
  - `docs/OBSERVABILITY_MODEL.md` — define estrutura de eventos, métricas, integração com Kratos e alertas.
  - `docs/COST_MODEL.md` — explica como calcular e rastrear o custo por etapa, com sugestões de otimização.
  - `docs/PRD_QUALITY_RUBRIC.md` — rubrica objetiva para avaliar PRDs com critérios e pontuação.
  - `docs/30_EXPONENTIAL_IDEAS_BENCHMARKED.md` — lista 30 ideias inovadoras benchmarkadas contra Lovable, v0, Replit e Bolt.
- **Novos módulos de código:**
  - `src/cost_tracking/cost_tracker.py` — módulo de rastreamento de custo em memória com agregação e log de eventos.
  - `src/cli/appfactory_cli.py` — CLI inicial com comando de auditoria e esqueleto para futuros comandos.
- **Novas pastas:**
  - `src/cost_tracking/` — contém o rastreador de custos.
  - `src/cli/` — contém a CLI do App Factory.
- **Novos arquivos de configuração planejados:** (não implementados nesta release, mas preparados na estrutura)
  - `config/models.yaml`, `config/templates.yaml` — placeholders para futuras configurações.

### Modificado

- `README.md` e `docs` originais permanecem; novos documentos complementam sem sobrescrever.
- `FILE_MANIFEST.yaml` deve ser atualizado manualmente para refletir novos arquivos e status `CREATE`.

### Removed

Nenhum arquivo removido nesta versão.  A política de não destruição permanece; arquivos obsoletos devem ser movidos para pastas de legado em releases futuras.

---
*Gerado por: Aurora — Perfect Factory V6 | 2026‑06‑04*

## [7.0.0] – 2026‑06‑04

### Adicionado

- **REAUDIT_REPORT.md:** relatório detalhado que audita a versão 6, compara com as especificações originais do App Factory e mapeia o que está bom, fraco, faltando e o que foi expandido.  Fornece planos de ação e riscos.
- **FILE_BY_FILE_APPLICATION_MAP.md:** inventário executável que associa cada diretório e arquivo aos seus propósitos, classificações (CREATE/REUSE/VERIFY/DEFER) e ações recomendadas.  Serve como guia para aplicar o pack em projetos reais.
- **CLAUDE_CODE_MASTER_PROMPT.md:** prompt mestre para inicializar e controlar o App Factory no Claude Code.  Divide o processo em Fase 0 (auditoria read‑only) e Fase 1 (criação/melhoria), reforçando risco, dry‑run e gates.
- **__APPLY_ROOT__/apply_root.md:** instruções passo a passo para aplicar este pacote a um repositório local ou novo projeto, incluindo pré‑requisitos, criação de ambiente, execução de testes e importação de arquivos.
- **docs/SYSTEM_DESIGN_DOCUMENT.md:** documento técnico que descreve em alto nível a arquitetura do System Creation OS, incluindo módulos de ingestão, descoberta, PRD, blueprint, schema, contratos, planos, scaffold, governança, eventos e writeback.
- **docs/REAUDIT_SUMMARY.md:** resumo executivo da re‑auditoria, destacando as melhorias implementadas na versão 7 e as orientações para futuro.
- **schemas/blueprint_schema.json** e **schemas/scaffold_plan_schema.json:** esboços de JSON Schema para validar blueprints e planos de scaffolding gerados pelo sistema.
- **tests/unit/test_blueprint_schema.py** e **tests/unit/test_scaffold_plan_schema.py:** testes que carregam e validam os novos schemas para garantir conformidade básica.
- **tests/unit/test_file_manifest.py** e **tests/unit/test_gate_config.py:** testes skeleton para validar a estrutura do manifesto de arquivos e a configuração dos gates.

### Modificado

- Atualizações nas políticas de risco e gates em `config/risk_policy.yaml` e `config/gates.yaml` para incorporar custo, segurança e observabilidade por etapa.
- Revisões em `docs/PRD.md`, `docs/BLUEPRINT.md` e `docs/VALIDATION_GATES.md` para expandir critérios de qualidade e introduzir rubricas de avaliação.
- Revisão em `ROADMAP.md` para adotar um plano de quatro waves com dez blocos cada, detalhando objetivos, riscos e critérios de pronto.
- Inclusão de seções no `README.md` e `docs/OMNIS_APP_FACTORY_BRIDGE.md` sobre integração com o repositório `omnis-control` e reaproveitamento dos módulos determinísticos existentes.

### Removed

- Nenhum arquivo removido.  A política de preservação continua vigente; arquivos obsoletos deverão ser arquivados em releases futuras.

---
*Gerado por: Aurora — App Factory V7 | 2026‑06‑04*