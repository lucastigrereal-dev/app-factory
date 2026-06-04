# Roadmap V7 — System Creation OS

Este roadmap organiza a evolução do App Factory em quatro **waves** (ondas), cada uma composta por dez blocos de trabalho.  Cada bloco descreve o objetivo, os arquivos ou módulos afetados, o nível de risco, as dependências e o critério de pronto.  Este planejamento reflete os gaps identificados na re‑auditoria e prepara o terreno para integrações futuras com o repositório `omnis-control` e com infraestruturas modernas de CI/CD.

## Wave 1 — Fundação e Auditoria

| Bloco | Objetivo | Artefatos Afetados | Risco | Dependências | Critério de Pronto |
|-----:|---|---|---|---|---|
| 1 | Reorganizar repositório de destino conforme `FILE_BY_FILE_APPLICATION_MAP.md` | Estrutura de pastas, `README.md` | R1 | Nenhuma | Estrutura replicada; manifesto atualizado |
| 2 | Executar auditoria read‑only com Claude Code e gerar `AUDIT_READONLY_REPORT.md` | `upgrade_reports/AUDIT_READONLY_REPORT.md` | R1 | Bloco 1 | Relatório gerado; lista de gaps e riscos |
| 3 | Atualizar `FILE_MANIFEST.yaml` com status CREATE/REUSE/VERIFY/DEFER | `FILE_MANIFEST.yaml` | R1 | Bloco 1 | Manifesto revisto e commit local em branch |
| 4 | Criar `CLAUDE_CODE_MASTER_PROMPT.md` e copiar para `.claude/CLAUDE.md` | `.claude/CLAUDE.md` | R1 | Bloco 1 | Prompt mestre em uso; revisado |
| 5 | Configurar ambiente Python e instalar pre‑commit com configurações básicas | `.pre-commit-config.yaml` | R2 | Nenhuma | Hooks instalados; verificação de segredos e lint |
| 6 | Gerar esboços de `schemas/blueprint_schema.json` e `schemas/scaffold_plan_schema.json` | Pastas `schemas/`, `tests/unit/` | R1 | Blocos 2, 3 | Schemas existem; testes passantes |
| 7 | Ajustar `config/risk_policy.yaml` e `config/gates.yaml` para incluir custo e observabilidade | `config/` | R2 | Nenhuma | YAMLs atualizados; testes de carga |
| 8 | Escrever `REAUDIT_REPORT.md` e `REAUDIT_SUMMARY.md` | `REAUDIT_REPORT.md`, `docs/REAUDIT_SUMMARY.md` | R0 | Bloco 2 | Documentos concluídos e revisados |
| 9 | Elaborar o mapa `FILE_BY_FILE_APPLICATION_MAP.md` | `FILE_BY_FILE_APPLICATION_MAP.md` | R0 | Blocos 2, 3 | Mapa completo, revisado |
| 10 | Atualizar `ROADMAP.md` com planejamento em waves | `ROADMAP.md` | R0 | Blocos 2–9 | Este roadmap publicado |

## Wave 2 — Geração e Qualidade

| Bloco | Objetivo | Artefatos Afetados | Risco | Dependências | Critério de Pronto |
|-----:|---|---|---|---|---|
| 11 | Implementar prompt `appfactory-plan` para gerar PRD e Blueprint em modo dry‑run | `.claude/commands/appfactory-plan.md`, `skills/prd-generator`, `skills/blueprint-generator` | R2 | Waves 1 Bloco 4 | Prompt funcional; outputs validados contra schemas |
| 12 | Criar `ENTERPRISE_QUALITY_GATES.md` com definições de gates por etapa | `docs/ENTERPRISE_QUALITY_GATES.md`, `config/gates.yaml` | R1 | Wave 1 Bloco 7 | Documento publicado; YAML revisado |
| 13 | Expandir `docs/PRD.md` e `docs/BLUEPRINT.md` com rubricas e exemplos detalhados | `docs/PRD.md`, `docs/BLUEPRINT.md` | R1 | Bloco 11 | Documentos reescritos; exemplos inclusos |
| 14 | Implementar prompts `appfactory-validate` e `appfactory-export` | `.claude/commands/appfactory-validate.md`, `.claude/commands/appfactory-export.md` | R2 | Bloco 11 | Comandos disponíveis e simulam validação/export |
| 15 | Criar testes unitários para schemas, manifestos e gates | `tests/unit/test_*` | R1 | Blocos 11–14 | Testes passam; cobertura mínima 60% |
| 16 | Adicionar `docs/SYSTEM_DESIGN_DOCUMENT.md` e integrar com planner determinístico do `omnis-control` | `docs/SYSTEM_DESIGN_DOCUMENT.md` | R0 | Bloco 13 | Documento revisto e aprovado |
| 17 | Gerar `docs/API_CONTRACTS.md` atualizado com exemplos de OpenAPI e contratos de eventos | `docs/API_CONTRACTS.md` | R1 | Bloco 11 | Contratos consistentes; validados |
| 18 | Refatorar `src/governance` para suportar cost tracking e segurança por etapa | `src/governance/`, `src/cost_tracking/` | R2 | Bloco 7 | Funções atualizadas; testes passantes |
| 19 | Criar templates iniciais para apps: `landing`, `dashboard` e `crm` com stack Next.js + Supabase + Tailwind | `templates/` | R2 | Blocos 13–17 | Templates prontos; validados por scaffolder |
| 20 | Atualizar `config/templates.yaml` e `config/skills.yaml` com os novos templates e skills | `config/templates.yaml`, `config/skills.yaml` | R1 | Bloco 19 | YAMLs atualizados sem erros |

## Wave 3 — Integração e CI/CD

| Bloco | Objetivo | Artefatos Afetados | Risco | Dependências | Critério de Pronto |
|-----:|---|---|---|---|---|
| 21 | Criar workflows GitHub Actions (`quality.yml`, `security.yml`, `test-backend.yml`, `test-frontend.yml`, `deploy-preview.yml`, `deploy-production.yml`) | `.github/workflows/` | R3 | Waves 1 Bloco 5, Wave 2 | Workflows presentes; rodando em CI dry‑run |
| 22 | Implementar `.pre-commit-config.yaml` com verificação de segredos, lint (Python/TS) e formatação | `.pre-commit-config.yaml` | R2 | Bloco 21 | Ganchos instalados; PRs são bloqueadas em caso de falha |
| 23 | Desenvolver `skills/mvp-builder` para gerar código real com templates (landing, CRM) | `skills/mvp-builder/` | R3 | Bloco 19 | Skill gera repositório de app em pasta temporária |
| 24 | Configurar deploy preview automático (Vercel ou Railway) para apps gerados | `.github/workflows/deploy-preview.yml`, `docs/DEPLOY.md` | R3 | Blocos 21, 23 | PR cria URL de preview automaticamente |
| 25 | Estabelecer Blue‑Green Deployment para produção | `.github/workflows/deploy-production.yml` | R3 | Bloco 24 | Deploy produz novas versões sem downtime |
| 26 | Documentar `docs/OBSERVABILITY_MODEL.md` com exemplos de métricas, logs e tracing | `docs/OBSERVABILITY_MODEL.md` | R1 | Bloco 21 | Documento atualizado e integrado com Kratos |
| 27 | Implementar integração com Akasha: gravação de eventos de decisão e aprendizado | `src/memory_writeback/`, `docs/AKASHA_WRITEBACK_PROTOCOL.md` | R2 | Blocos 11, 14 | Eventos são persistidos em dry‑run; schema validado |
| 28 | Implementar integração com Kratos: endpoint de snapshot real e dashboard | `src/api/kratos_status.py`, `docs/KRATOS_SNAPSHOT_PROTOCOL.md` | R2 | Blocos 21, 26 | Dashboard recebe snapshots; esquema validado |
| 29 | Criar `AGENTS.md` e `.claude/settings.json` para definir escopos, permissões e hooks do Claude Code | `AGENTS.md`, `.claude/settings.json`, `.claude/hooks/` | R2 | Blocos 21–23 | Arquivos criados; Claude Code reconhece agentes |
| 30 | Revisar e atualizar `SYSTEM_STATE.md` para refletir progresso | `SYSTEM_STATE.md` | R0 | Todos os blocos anteriores | Documento atualizado |

## Wave 4 — Autonomia e Self‑Healing

| Bloco | Objetivo | Artefatos Afetados | Risco | Dependências | Critério de Pronto |
|-----:|---|---|---|---|---|
| 31 | Transformar agentes de prompts em MCP servers executáveis com FastAPI | `.claude/agents/`, `src/mcp/` | R3 | Waves 2–3 | Servidores MCP respondem a chamadas locais |
| 32 | Criar circuito de self‑healing e retry em caso de falhas nas etapas | `src/governance/recovery.py`, `src/events/` | R3 | Blocos 21, 31 | Sistema detecta falhas e reexecuta etapas |
| 33 | Estabelecer Trust Factor dinâmico para cada agente e penalização em caso de violação | `config/risk_policy.yaml`, `src/governance/penalties.py` | R3 | Blocos 31–32 | Trust factor calculado e registrado |
| 34 | Desenvolver testes E2E do ciclo completo (ideia → deploy) | `tests/e2e/` | R3 | Blocos 23–25 | Teste gera app real e verifica URL de preview |
| 35 | Criar dashboards de custo/latência em Kratos com agregações por etapa | `src/api/kratos_status.py`, `docs/OBSERVABILITY_MODEL.md` | R2 | Blocos 26–28 | Dashboards mostram custos e tempos |
| 36 | Implementar fallback determinístico com `AppFactoryPlanner` para verificar outputs de LLMs | `src/planner_fallback.py` | R2 | Blocos 11–27 | Fallback compara blueprint/PRD com planner | 
| 37 | Criar auditoria automática de qualidade de PRD e Blueprint via heurísticas e AST | `src/quality/prd_audit.py`, `src/quality/blueprint_audit.py` | R2 | Blocos 13 | Scripts auditam e atribuem notas |
| 38 | Formalizar e publicar `APP_FACTORY_CONSTITUTION.md` e protocolos de setor, subsector, squad e skill | `docs/CONSTITUTION/` | R1 | Blocos 30 | Documentos escritos e aprovados |
| 39 | Escrever guias bilíngues (EN/PT) para devs e stakeholders | `docs/Guides/` | R1 | Todas as waves | Guias publicados |
| 40 | Lançar release V8 com gerador de UI e deploy automático – marco de prova | `CHANGELOG.md`, Release notes | R3 | Todos os blocos | Release publicado; app real gerado |

### Uso do Roadmap

* **Paralelismo seguro:** Blocos com risco R0–R1 podem ser executados em paralelo.  Blocos R2 requerem coordenação e revisão.  Blocos R3 exigem aprovação humana antes de merge/deploy.
* **Atualização contínua:** Este roadmap é uma base inicial; atualize conforme novas descobertas ou mudanças no contexto de negócio.  Ao concluir um bloco, revise as dependências das próximas etapas e ajuste o risco se necessário.
* **Versão controlada:** Registre mudanças significativas no `CHANGELOG.md` e, quando implementar novos artefatos, atualize `FILE_MANIFEST.yaml` e `FILE_BY_FILE_APPLICATION_MAP.md` para manter rastreabilidade.