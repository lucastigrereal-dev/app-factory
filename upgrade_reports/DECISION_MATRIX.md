# DECISION_MATRIX.md
> Perfect Factory Upgrade — Matriz de Decisão
> Versão: 1.0 | Data: 2026-06-04 | Dono: Lucas Tigre / Aurora

---

## Legenda de Risco
| Nível | Significado |
|-------|-------------|
| R0 | Seguro — nenhuma consequência se falhar |
| R1 | Baixo — reversível, afeta só dev |
| R2 | Médio — afeta outros arquivos, precisa dry_run |
| R3 | Alto — irreversível ou afeta produção, exige aprovação humana |

---

## Legenda de Decisão
| Decisão | Ação |
|---------|------|
| CREATE | Criar do zero — não existe |
| REUSE | Já existe — aproveitar como está |
| VERIFY | Existe mas precisa de validação/ajuste |
| DEFER | Adiado para Wave posterior |
| ARCHIVE | Mover para pasta de arquivo, não deletar |

---

## Matriz

| # | Item | Tipo | Estado Atual | Decisão | Motivo | Risco | Dono Sugerido | Arquivos Afetados | Teste Necessário | Critério de Pronto |
|---|------|------|--------------|---------|--------|-------|---------------|-------------------|------------------|--------------------|
| 1 | SYSTEM_CANON.md | Doc | Referenciado, não existe | CREATE | Lei-mãe ausente — nenhum protocolo tem autoridade formal | R1 | Aurora + Lucas | Todos os .md | test_canon_references.py | Todos os docs apontam para o Canon sem conflito |
| 2 | APPFACTORY_CONSTITUTION.md | Doc | Ausente (crítico) | CREATE | Constituição da fábrica — sem ela os protocolos são sugestões | R1 | Aurora + Lucas | MASTERINDEX, todos os PROTOCOLs | test_constitution_sections.py | 8 seções obrigatórias presentes e válidas |
| 3 | AGENTS.md (raiz do repo) | Config | Ausente | CREATE | Claude Code não sabe nada sobre a fábrica sem esse arquivo | R1 | Aurora | .claude/settings.json | test_agents_format.py | Claude Code lê e responde com escopo correto |
| 4 | .claude/settings.json | Config | Ausente | CREATE | Sem ele Claude Code ignora políticas de segurança | R1 | Aurora | hooks, agents | test_settings_schema.json | Valida contra JSON schema, paths proibidos listados |
| 5 | .claude/hooks/pre-tool.py | Code | Ausente | CREATE | Sem gate pré-execução Claude pode escrever em paths proibidos | R2 | Aurora | todos os paths | test_pretool_hook.py | Bloqueia paths proibidos, dry_run=True funciona |
| 6 | .claude/commands/appfactory-audit.md | Command | Ausente | CREATE | Sem comando de auditoria o operador audita na mão | R0 | Aurora | AUDIT_READONLY_REPORT.md | manual | Executa auditoria read-only e gera relatório |
| 7 | .claude/commands/appfactory-plan.md | Command | Ausente | CREATE | Sem plano estruturado cada geração é ad-hoc | R0 | Aurora | DECISION_MATRIX.md | manual | Gera matriz de decisão a partir de input |
| 8 | .claude/commands/appfactory-validate.md | Command | Ausente | CREATE | Validação manual é esquecida | R0 | Aurora | gates.yaml | manual | Executa todos os gates e retorna score |
| 9 | .claude/commands/appfactory-export.md | Command | Ausente | CREATE | Handoff para dev/cliente é feito na mão | R0 | Aurora | handoff_report_schema.json | manual | Gera relatório de handoff completo |
| 10 | .claude/agents/aurora.md | Agent | Parcial (sem escopo formal) | VERIFY | Aurora existe como conceito, não como agente com restrições claras | R1 | Lucas | PROTOCOL_WORKFLOW.md | test_agent_scope.py | Scope, tools_allowed, tools_forbidden, output_format definidos |
| 11 | .claude/agents/omnis.md | Agent | Parcial | VERIFY | Executor sem escopo formal de segurança | R2 | Lucas | PROTOCOL_WORKFLOW.md | test_agent_scope.py | Não executa R3 sem aprovação explícita |
| 12 | .claude/agents/akasha.md | Agent | Parcial (config existe, uso não) | VERIFY | Memória configurada mas não integrada ao workflow | R1 | Aurora | PROTOCOL_MEMORY.md | test_akasha_writeback.py | Salva e recupera decisão com schema válido |
| 13 | .claude/agents/kratos.md | Agent | Ausente (só referência) | CREATE | Observabilidade zero sem KRATOS | R1 | Aurora | OBSERVABILITY_MODEL.md | test_kratos_snapshot.py | Gera snapshot com wave, risco, progresso, bloqueios |
| 14 | .claude/agents/guardian.md | Agent | Ausente | CREATE | Sem guardião qualquer ação R3 pode passar | R2 | Aurora | risk_policy.yaml | test_guardian_blocks.py | Bloqueia .env, git add -A, push, deploy direto |
| 15 | config/risk_policy.yaml | Config | Ausente | CREATE | Política de risco em prosa — não é máquina-legível | R1 | Aurora | all agents, hooks | test_risk_policy_schema.py | Valida R0-R3, dry_run default, approval_required |
| 16 | config/gates.yaml | Config | Ausente (PROTOCOL_APPROVAL_GATES existe) | CREATE | Gates em Markdown não são executáveis | R1 | Aurora | validation-gate-runner | test_gate_config.py | Cada gate tem input, output, check, action_on_fail |
| 17 | config/skills.yaml | Config | SKILLREGISTRY.md existe | CREATE | Registry em Markdown não é machine-readable | R1 | Aurora | skill scripts | test_skills_schema.py | Cada skill tem input_schema, output_schema, risco |
| 18 | config/models.yaml | Config | Ausente | CREATE | Seleção de modelo é hardcoded em prompts | R1 | Aurora | all agents | test_models_schema.py | Inclui fallback, custo estimado, contexto máximo |
| 19 | config/templates.yaml | Config | 11/TEMPLATES existe como pasta | CREATE | Templates sem metadata não são consultáveis por agentes | R1 | Aurora | scaffold planner | test_templates_schema.py | Cada template tem stack, use_cases, risks, files |
| 20 | schemas/idea_input_schema.json | Schema | Entregue nessa sessão | REUSE | Já criado — validar apenas | R0 | Aurora | intake module | test_idea_input_schema.py | JSONSchema válido, campos obrigatórios presentes |
| 21 | schemas/prd_output_schema.json | Schema | Entregue nessa sessão | REUSE | Já criado | R0 | Aurora | prd module | test_prd_output_schema.py | JSONSchema válido |
| 22 | schemas/blueprint_schema.json | Schema | Ausente | CREATE | Blueprint sem schema aceita qualquer coisa | R1 | Aurora | blueprint module | test_blueprint_schema.py | Campos obrigatórios: modules, apis, db_tables, risks |
| 23 | schemas/scaffold_plan_schema.json | Schema | Ausente | CREATE | Scaffold sem plano formal pode criar estrutura errada | R2 | Aurora | scaffold module | test_scaffold_schema.py | Inclui dry_run, file_tree, diff_preview, risk |
| 24 | schemas/handoff_report_schema.json | Schema | Entregue nessa sessão | REUSE | Já criado | R0 | Aurora | handoff exporter | test_handoff_schema.py | JSONSchema válido |
| 25 | GOVERNANCE_POLICY.md | Doc | Parcial (em OMNIS_CONTRATOS) | VERIFY | Governança existe mas espalhada em múltiplos docs | R1 | Lucas | todos os protocolos | manual review | Single-doc com 6 seções: princípios, riscos, gates, roles, violations, changelog |
| 26 | FILE_MANIFEST.yaml | Config | Ausente | CREATE | Sem manifesto vivo o sistema não sabe o que existe | R1 | Aurora | todos | test_file_manifest.py | Status CREATE/REUSE/VERIFY/DEFER por arquivo |
| 27 | docs/ERROR_PLAYBOOK.md | Doc | Ausente | CREATE | Falhas tratadas ad-hoc, sem procedimento | R0 | Aurora | runbook | manual | Cobre: PRD fraco, schema inválido, gate falhou, arquivo duplicado, agente travado |
| 28 | docs/OBSERVABILITY_MODEL.md | Doc | Parcial (KRATOS mencionado) | CREATE | Sem modelo de observabilidade logs são inúteis | R1 | Aurora | KRATOS agent | manual | Define: eventos, payload, alertas, SLAs |
| 29 | docs/COST_MODEL.md | Doc | Ausente | CREATE | Sem custo rastreado factory não tem ROI mensurável | R0 | Aurora | cost_tracking module | manual | Estimativa por wave, por tipo de app, por agente |
| 30 | tests/e2e/test_golden_path.py | Test | Ausente | CREATE | Sem E2E não tem como saber se a esteira completa funciona | R1 | Aurora | todos os módulos | CI pipeline | Passa: ideia → PRD → blueprint → scaffold_plan → handoff |
| 31 | PROTOCOL_SECTOR.md | Doc | Ausente (referenciado como N1) | CREATE | Setores existem no registry mas sem protocolo de ciclo de vida | R1 | Aurora | SECTORREGISTRY | manual | Descreve: criação, crescimento, inativação de setor |
| 32 | PROTOCOL_SQUAD.md | Doc | Ausente | CREATE | Squads sem protocolo operam sem regras | R1 | Aurora | SQUADREGISTRY | manual | Define: composição, responsabilidades, gates de squad |
| 33 | 07SKILLS/mvp-builder/SKILL.md | Skill | Ausente | CREATE | A skill mais crítica para superar o Lovable | R2 | OMNIS | scaffold module | test_mvp_builder.py | Gera estrutura Next.js + Supabase + shadcn válida |
| 34 | 07SKILLS/ui-component-generator/SKILL.md | Skill | Ausente | CREATE | Componentes hoje são feitos na mão | R1 | OMNIS | frontend plan | test_ui_generator.py | Gera componente React com types, stories, testes |
| 35 | .github/workflows/governance-check.yml | CI | Parcial (mencionado, incompleto) | VERIFY | CI existe mas não roda testes reais | R2 | Aurora | todos os pushes | CI runner | Executa lint, tests, secret-scan, schema-validation |
| 36 | Anti-Goal Document | Doc | Ausente | CREATE | Sem anti-goals a fábrica vira Frankenstein | R0 | Lucas | SYSTEM_CANON | manual | Lista explícita de 10+ itens fora de escopo |
| 37 | App Type Registry (config/app_types.yaml) | Config | Ausente | CREATE | Sem registry de tipos cada geração reinventa | R0 | Aurora | template registry | test_app_types.py | Cobre: landing, CRM, dashboard, SaaS, automation, API-only |
| 38 | Stack Decision Matrix | Doc | Ausente | CREATE | Stack escolhida no grito, sem critérios | R1 | Aurora + Lucas | all templates | manual | Matriz: prazo, complexidade, dados, auth, UI, escala |
| 39 | PROTOCOL_SUBAGENT.md | Doc | Ausente | CREATE | Agentes sem protocolo de ciclo de vida | R1 | Aurora | SUBAGENTREGISTRY | manual | Define: criação, escopo, deprecação de subagente |
| 40 | ROADMAP_2026_2027.md | Doc | Parcial (Wave structure existe) | CREATE | Roadmap em formato enterprise com métricas e gates | R0 | Lucas | WAVES folder | manual | Por trimestre: entregáveis, KPIs, responsáveis |

---

## Resumo por Decisão

| Decisão | Qtde |
|---------|------|
| CREATE | 28 |
| VERIFY | 7 |
| REUSE | 3 |
| DEFER | 2 |
| ARCHIVE | 0 |

---

## Próxima Ação
Executar Wave 1 (itens 1-9) antes de qualquer código novo.
