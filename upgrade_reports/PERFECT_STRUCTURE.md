# PERFECT_STRUCTURE.md
**Árvore Canônica Final Proposta — App Factory**

```
APPFACTORY_ARCHITECTURE/
│
├── 00_CONSTITUTION/
│   ├── APPFACTORY_CONSTITUTION.md         [REUSE — canônico]
│   └── AMENDMENTS/                         [CREATE quando necessário]
│
├── 01_PROTOCOLS/
│   ├── PROTOCOL_SECTOR.md                 [REUSE]
│   ├── PROTOCOL_SUBSECTOR.md              [REUSE]
│   ├── PROTOCOL_SQUAD.md                  [REUSE]
│   ├── PROTOCOL_SUBAGENT.md               [REUSE]
│   ├── PROTOCOL_SKILL.md                  [REUSE]
│   ├── PROTOCOL_WORKFLOW.md               [REUSE]
│   ├── PROTOCOL_MCP.md                    [REUSE]
│   ├── PROTOCOL_MEMORY.md                 [REUSE]
│   ├── PROTOCOL_APPROVAL_GATES.md         [REUSE]
│   └── PROTOCOL_EVOLUTION.md              [REUSE]
│
├── 02_REGISTRIES/
│   ├── DOCUMENT_REGISTRY.md               [REUSE]
│   ├── SECTOR_REGISTRY.md                 [REUSE]
│   ├── SQUAD_REGISTRY.md                  [REUSE]
│   ├── SUBAGENT_REGISTRY.md               [REUSE]
│   ├── SKILL_REGISTRY.md                  [REUSE]
│   └── MCP_REGISTRY.md                    [REUSE]
│
├── config/                                [CREATE — machine-readable]
│   ├── gates.yaml                         [CREATE — entregue neste pacote]
│   ├── risk_policy.yaml                   [CREATE — entregue neste pacote]
│   ├── models.yaml                        [CREATE]
│   ├── skills.yaml                        [CREATE]
│   ├── templates.yaml                     [CREATE]
│   └── factories.yaml                     [CREATE]
│
├── schemas/                               [CREATE — JSON schemas]
│   ├── idea_input_schema.json             [CREATE — entregue]
│   ├── prd_output_schema.json             [CREATE — entregue]
│   ├── blueprint_schema.json              [CREATE]
│   ├── scaffold_plan_schema.json          [CREATE]
│   └── handoff_report_schema.json         [CREATE — entregue]
│
├── docs/
│   ├── PRD_SYSTEM_CREATION_OS.md          [REUSE]
│   ├── ARCHITECTURE.md                    [VERIFY — atualizar]
│   ├── CLAUDE_CODE_RUNBOOK.md             [CREATE]
│   ├── VALIDATION_GATES.md                [CREATE]
│   ├── ERROR_PLAYBOOK.md                  [CREATE — entregue]
│   ├── SECURITY_MODEL.md                  [CREATE]
│   ├── OBSERVABILITY_MODEL.md             [VERIFY]
│   └── COST_MODEL.md                      [VERIFY]
│
├── .claude/
│   ├── CLAUDE.md                          [CREATE/VERIFY]
│   ├── settings.json                      [CREATE/VERIFY]
│   ├── commands/
│   │   ├── appfactory-audit.md            [CREATE — entregue]
│   │   ├── appfactory-plan.md             [CREATE — entregue]
│   │   ├── appfactory-validate.md         [CREATE — entregue]
│   │   └── appfactory-export.md           [CREATE — entregue]
│   ├── agents/
│   │   ├── app-factory-architect.md       [CREATE — entregue]
│   │   ├── prd-writer.md                  [CREATE — entregue]
│   │   ├── security-guardian.md           [CREATE — entregue]
│   │   └── test-guardian.md               [CREATE — entregue]
│   └── hooks/
│       ├── pre-action-sentinel.md         [CREATE]
│       └── no-destructive-guard.md        [CREATE]
│
├── src/
│   ├── intake/
│   ├── prd/
│   ├── blueprint/
│   ├── schema/
│   ├── api_contracts/
│   ├── scaffold/
│   ├── validation/
│   ├── governance/
│   │   └── risk_classifier.py             [CREATE skeleton — entregue]
│   ├── memory_writeback/
│   ├── cost_tracking/
│   └── cli/
│
├── templates/
│   ├── prd/
│   ├── blueprint/
│   ├── api/
│   ├── db/
│   ├── landing_page/
│   ├── dashboard/
│   ├── crm/
│   ├── saas/
│   └── automation/
│
├── tests/
│   ├── unit/
│   │   ├── test_risk_classifier.py        [CREATE — entregue]
│   │   ├── test_gate_config.py            [CREATE — entregue]
│   │   └── test_prd_output_schema.py      [CREATE]
│   ├── e2e/
│   │   └── test_golden_path.py            [CREATE skeleton]
│   └── fixtures/
│       ├── sample_idea.json               [CREATE]
│       ├── sample_prd.json                [CREATE]
│       └── sample_blueprint.json          [CREATE]
│
├── APPFACTORY_MASTERINDEX.md              [REUSE — canônico]
├── SYSTEM_CANON.md                        [CREATE — define o que manda em tudo]
├── GOVERNANCE_POLICY.md                   [CREATE]
├── FILE_MANIFEST.yaml                     [UPDATE — entregue FILE_MANIFEST_UPDATED.yaml]
├── ROADMAP.md                             [REUSE]
└── CHANGELOG.md                           [CREATE]
```

## Legenda de Ações
- **CREATE** — arquivo novo, não existe
- **REUSE** — arquivo existe e está canônico
- **VERIFY** — arquivo existe mas precisa revisão
- **DEFER** — pode esperar, não é bloqueante agora
- **ARCHIVE** — mover para 99_LEGACY_NOTES

---
*Gerado por: Perplexity Ultra-Dev | 2026-06-04*
