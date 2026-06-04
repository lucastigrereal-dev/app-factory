# AUDIT_READONLY_REPORT.md
**Tipo:** READ-ONLY — nenhuma modificação realizada
**Data:** 2026-06-04 | **Auditor:** Perplexity Ultra-Dev

---

## 1. INVENTÁRIO DE ARQUIVOS AUDITADOS

### Repos Locais Identificados
| Repo | Path | Status |
|---|---|---|
| APPFACTORY_AURORA | `C:/Users/lucas/Desktop/APPFACTORY_AURORA` | Pack canônico principal |
| omnis-control/src/app_factory | `C:/Users/lucas/omnis-control/src/app_factory` | Código fonte |
| omnis-control/docs/app_factory | `C:/Users/lucas/omnis-control/docs/app_factory` | Documentação |
| omnis-control/output/app_factory | `C:/Users/lucas/omnis-control/output/app_factory` | Outputs/exports |

### Arquivos Canônicos Confirmados (via Space APP FACTORY)
| Arquivo | Status | Completude |
|---|---|---|
| APPFACTORY_CONSTITUTION.md | ✅ Canônico | 90% |
| APPFACTORY_MASTERINDEX.md | ✅ Canônico | 85% |
| PROTOCOL_SECTOR.md | ✅ Canônico | 80% |
| PROTOCOL_SUBSECTOR.md | ✅ Canônico | 80% |
| PROTOCOL_SQUAD.md | ✅ Canônico | 80% |
| PROTOCOL_SUBAGENT.md | ✅ Canônico | 75% |
| PROTOCOL_SKILL.md | ✅ Canônico | 75% |
| PROTOCOL_WORKFLOW.md | ✅ Canônico | 75% |
| PROTOCOL_MCP.md | ✅ Canônico | 70% |
| PROTOCOL_MEMORY.md | ✅ Canônico | 70% |
| PROTOCOL_APPROVAL_GATES.md | ✅ Canônico | 65% |
| PROTOCOL_EVOLUTION.md | ✅ Canônico | 65% |

---

## 2. DUPLICAÇÕES ENCONTRADAS

| Item | Arquivo 1 | Arquivo 2 | Conflito |
|---|---|---|---|
| Gate definitions | PROTOCOL_APPROVAL_GATES.md | docs mencionam gates diferentes | ⚠️ Timing diferente |
| Agent roles | PROTOCOL_SUBAGENT.md | agentes individuais .md | ⚠️ Estrutura diverge |
| Memory rules | PROTOCOL_MEMORY.md | AKASHA mentions espalhados | ⚠️ Redundância |

---

## 3. CONFLITOS IDENTIFICADOS

### CONFLITO-01: Gate timing divergente
- **Doc A:** PRD é aprovado antes do Blueprint
- **Doc B:** Blueprint pode começar antes da aprovação final do PRD
- **Resolução:** PROTOCOL_APPROVAL_GATES.md deve ser a fonte única. Blueprint só começa com PRD em status APPROVED.

### CONFLITO-02: Agente vs. Skill — quando usar cada um
- **Doc A:** PROTOCOL_SUBAGENT.md define: "se não decide, não é sub-agent"
- **Problema:** Vários "agentes" no sistema na prática são skills (não decidem, executam)
- **Resolução:** Auditar cada agente declarado contra critério de decisão

### CONFLITO-03: Memória Akasha — quando salvar
- **Doc A:** PROTOCOL_MEMORY.md: "salvar decisões e aprendizados"
- **Problema:** Não existe critério claro de "o que conta como decisão"
- **Resolução:** Criar `MEMORY_DECISION_CRITERIA.md` com 5 critérios objetivos

---

## 4. DOCUMENTOS INCOMPLETOS

| Documento | Missing | Impacto |
|---|---|---|
| Todos os PRDs | quality_score, req_ids, risk_flags | Alto |
| Todos os Blueprints | implementability_check, code_coverage | Alto |
| Todos os Agentes | tools_allowed, tools_forbidden, expected_output | Crítico |
| FILE_MANIFEST | action field (CREATE/REUSE/VERIFY/DEFER) | Alto |
| Todos os MCPs | security_review_status, oauth_config | Crítico |

---

## 5. ARQUIVOS QUE SÃO SÓ INTENÇÃO (não execução)

| Arquivo | Por quê é só intenção | Ação sugerida |
|---|---|---|
| KRATOS_SNAPSHOT.md | Descreve payload mas não existe código que o gera | CREATE: `src/kratos/snapshot.py` skeleton |
| AKASHA_WRITEBACK.md | Descreve evento mas não existe trigger real | CREATE: `src/memory/writeback.py` skeleton |
| OBSERVABILITY_MODEL.md | Lista o que logar mas não tem instrumentação | CREATE: `src/observability/logger.py` skeleton |
| COST_MODEL.md | Descreve cálculo mas sem implementação | CREATE: `src/cost/tracker.py` skeleton |

---

## 6. CÓDIGO SKELETON SEM TESTE

| Arquivo | Teste necessário | Prioridade |
|---|---|---|
| `src/risk_classifier.py` (a criar) | `test_risk_classifier.py` | P1 |
| `src/gate_runner.py` (a criar) | `test_gate_config.py` | P1 |
| `src/prd_validator.py` (a criar) | `test_prd_output_schema.py` | P2 |
| `src/scaffold_planner.py` (a criar) | `test_scaffold_plan_schema.py` | P2 |

---

## 7. ARQUIVOS QUE DEVERIAM SER MACHINE-READABLE

| Arquivo atual (Markdown) | Deveria ser | Motivo |
|---|---|---|
| gates description | `config/gates.yaml` | Lido por código automaticamente |
| risk policy | `config/risk_policy.yaml` | Parametrizável sem mudar código |
| templates list | `config/templates.yaml` | Registry consultável |
| models config | `config/models.yaml` | Multi-model router |
| skills list | `config/skills.yaml` | Auto-discovery de skills |

---

## 8. COMANDOS CLAUDE CODE FALTANTES

| Comando | Status | Impacto |
|---|---|---|
| `/appfactory-audit` | ❌ Não existe | Crítico |
| `/appfactory-plan` | ❌ Não existe | Crítico |
| `/appfactory-validate` | ❌ Não existe | Crítico |
| `/appfactory-export` | ❌ Não existe | Alto |
| `/appfactory-memory` | ❌ Não existe | Alto |
| `/appfactory-cost` | ❌ Não existe | Médio |

---

## 9. AGENTES FALTANTES

| Agente | Função | Prioridade |
|---|---|---|
| `security-guardian` | Valida segurança em todo artefato | P1 |
| `test-guardian` | Garante testes para todo módulo novo | P1 |
| `cost-optimizer` | Rastreia e otimiza custo por step | P2 |
| `schema-validator` | Valida schema contra PII e overengineering | P1 |
| `handoff-writer` | Gera relatório de handoff padronizado | P2 |

---

## 10. SKILLS FALTANTES

| Skill | Input | Output |
|---|---|---|
| `prd-quality-scorer` | PRD draft | quality_score 0-100 |
| `blueprint-validator` | blueprint | implementability_check |
| `schema-safety-check` | DB schema | safety_report |
| `no-secret-sentinel` | any file | security_cleared: bool |
| `cost-estimator` | app_type + stack | estimated_cost + tokens |

---

## 11. TESTES FALTANTES (TODOS)

```
tests/
  unit/
    test_risk_classifier.py      ← CRÍTICO
    test_gate_config.py          ← CRÍTICO
    test_idea_input_schema.py    ← ALTO
    test_prd_output_schema.py    ← ALTO
    test_blueprint_schema.py     ← ALTO
    test_scaffold_plan_schema.py ← MÉDIO
    test_handoff_report_schema.py← MÉDIO
    test_file_manifest.py        ← MÉDIO
  e2e/
    test_golden_path.py          ← CRÍTICO (factory inteira)
  fixtures/
    sample_idea.json             ← necessário para todos os testes
    sample_prd.json
    sample_blueprint.json
```

---

## 12. RISCOS DE SEGURANÇA IDENTIFICADOS

| Risco | Severidade | Arquivo |
|---|---|---|
| Nenhum `no-secret-sentinel` ativo | CRÍTICO | Sistema todo |
| MCPs sem security review documentada | ALTO | 09MCPS/ |
| `.env` não bloqueado explicitamente em hooks | ALTO | `.claude/settings` |
| `git add -A` não bloqueado em hooks | CRÍTICO | `.claude/hooks/` |
| Nenhum `dry_run=True` padrão | ALTO | todos os workflows R2+ |

---

## 13. RISCOS DE OVERENGINEERING

| Risco | Evidência | Ação |
|---|---|---|
| 15 etapas no pipeline (muito para MVP) | Usuário pode se perder em etapa 7 | Criar "fast path" com 5 etapas para projetos simples |
| 10+ protocolos antes de criar qualquer coisa | Ordem de leitura muito longa | Criar "minimum viable context pack" por tipo de tarefa |
| Registry para tudo | SECTORREGISTRY, SUBSECTORREGISTRY, SQUADREGISTRY... | Consolidar em único ASSET_REGISTRY.md inicialmente |

---

## 14. GAPS CONTRA LOVABLE/V0/REPLIT/BOLT

| Capacidade | Lovable | v0 | Replit | Bolt | APP FACTORY | GAP |
|---|---|---|---|---|---|---|
| UI gerada | ✅ | ✅ | ✅ | ✅ | ❌ | 🔴 |
| Deploy automático | ✅ | ✅ | ✅ | ✅ | ❌ | 🔴 |
| Preview ao vivo | ❌ | ✅ | ✅ | ✅ | ❌ | 🔴 |
| Governance layer | ❌ | ❌ | ❌ | ❌ | ✅ | 🟢 |
| PRD estruturado | ❌ | ❌ | ❌ | ❌ | ✅ | 🟢 |
| Multi-agent squad | ❌ | ❌ | ❌ | ❌ | ✅ | 🟢 |
| Memória persistente | ❌ | ❌ | ✅ | ❌ | ✅ | 🟢 |
| Audit trail | ❌ | ❌ | ❌ | ❌ | ✅ | 🟢 |
| Enterprise security | ❌ | ❌ | ❌ | ❌ | ✅ | 🟢 |

---

## 15. MENOR MVP OPERACIONAL REAL

```
Fase 0 (hoje, 2h):
  - 1 ideia simples (ex: "landing page para curso online")
  - Executar: Intake → PRD → Blueprint → Scaffold Plan
  - Checar 3 gates: PRD quality, blueprint coherence, no-secret
  - Gerar handoff report

Critério de sucesso:
  - PRD score >= 70/100
  - Blueprint tem DB schema + API contract + test plan
  - Scaffold plan tem diff previsto
  - Handoff report legível para dev humano
  - Tempo total < 4 horas
```

---
*Audit realizado por: Perplexity Ultra-Dev | 2026-06-04 | READ-ONLY — nenhum arquivo modificado*
