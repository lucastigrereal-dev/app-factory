# ENTERPRISE_QUALITY_GATES.md
**Versão:** 1.0 | **Data:** 2026-06-04
**Autoridade:** PROTOCOL_APPROVAL_GATES.md + APPFACTORY_CONSTITUTION.md

---

## VISÃO GERAL

Gates são checkpoints obrigatórios que impedem avanço sem validação.
Um gate FAILED bloqueia a esteira. Um gate WARN permite avançar com registro.
Nenhum gate pode ser pulado sem aprovação explícita do owner (Lucas Tigre).

---

## GATE-01: IDEA INTAKE

| Campo | Valor |
|---|---|
| **Input** | Ideia em linguagem natural |
| **Output** | `idea_intake.json` validado contra `idea_input_schema.json` |
| **Check automático** | Schema validation: todos os campos obrigatórios presentes |
| **Check humano** | Ideia está alinhada com missão da factory? |
| **Erro comum** | Ideia muito vaga ("quero um app de vendas") sem contexto |
| **Ação se falhar** | Retornar para refinamento com 5 perguntas de clarificação |
| **Risco** | R0 |
| **Critério de pronto** | `idea_intake.json` com score clareza >= 70/100 |

---

## GATE-02: DISCOVERY COMPLETO

| Campo | Valor |
|---|---|
| **Input** | `idea_intake.json` |
| **Output** | `discovery_report.md` com: problema, usuário, valor, concorrentes, riscos |
| **Check automático** | Todos os 5 campos presentes e com > 50 palavras cada |
| **Check humano** | Discovery faz sentido de negócio? |
| **Erro comum** | Discovery genérico sem dados reais |
| **Ação se falhar** | Perplexity research adicional sobre o domínio |
| **Risco** | R0 |
| **Critério de pronto** | 5 campos preenchidos + validação humana |

---

## GATE-03: PRD QUALITY GATE

| Campo | Valor |
|---|---|
| **Input** | `discovery_report.md` |
| **Output** | `prd.md` com quality_score >= 75/100 |
| **Check automático** | PRD Quality Rubric: clareza (20), escopo (20), critérios (20), riscos (20), métricas (20) |
| **Check humano** | Lucas aprova escopo antes de ir para blueprint |
| **Erro comum** | PRD sem critérios de aceite mensuráveis, sem métricas de sucesso |
| **Ação se falhar** | PRD Writer refina até score >= 75 |
| **Risco** | R1 |
| **Critério de pronto** | quality_score >= 75 + aprovação Lucas |

### PRD Quality Rubric (0-100):
```
Clareza (20 pts):
  - Objetivo em 1 frase: 5pts
  - Usuário alvo definido: 5pts
  - Problema real e não vago: 10pts

Escopo (20 pts):
  - O que está IN: 10pts
  - O que está OUT (Anti-Goals): 10pts

Critérios de Aceite (20 pts):
  - >= 3 critérios mensuráveis: 10pts
  - Cada critério testável: 10pts

Riscos (20 pts):
  - >= 2 riscos identificados: 10pts
  - Mitigação para cada risco: 10pts

Métricas (20 pts):
  - KPI principal definido: 10pts
  - Como medir o sucesso: 10pts
```

---

## GATE-04: BLUEPRINT COHERENCE GATE

| Campo | Valor |
|---|---|
| **Input** | `prd.md` aprovado |
| **Output** | `blueprint.md` com implementability_score >= 70/100 |
| **Check automático** | Blueprint tem: DB schema plan? API contract? Frontend plan? Backend plan? Test plan? |
| **Check humano** | Blueprint realmente vira código ou é "poesia técnica"? |
| **Erro comum** | Blueprint lindo mas sem schema de DB, sem auth definido, sem decisão de stack |
| **Ação se falhar** | Architect agent refina seções faltantes |
| **Risco** | R1 |
| **Critério de pronto** | 5 seções presentes + implementability_score >= 70 |

### Blueprint Quality Check:
```
✅ Tem stack decision com justificativa
✅ Tem DB schema (mesmo que rascunho)
✅ Tem pelo menos 3 endpoints no API contract
✅ Tem frontend component list
✅ Tem pelo menos 3 test cases identificados
✅ Tem security considerations
✅ Tem estimativa de tempo/complexidade
```

---

## GATE-05: SCHEMA SAFETY GATE

| Campo | Valor |
|---|---|
| **Input** | `db_schema.sql` ou `schema.prisma` |
| **Output** | `schema_safety_report.json` |
| **Check automático** | Nenhuma tabela sem PK; nenhum campo PII não encriptado; sem ambiguidade; sem overengineering |
| **Check humano** | Schema faz sentido para o domínio? |
| **Erro comum** | Tabela `users` sem campo `created_at`; campo `data` sem tipo específico |
| **Ação se falhar** | Schema planner corrige e re-submete |
| **Risco** | R2 |
| **Critério de pronto** | Zero violações críticas no safety report |

### Schema Safety Checklist:
```
🔴 BLOQUEANTES:
  - Tabela sem PRIMARY KEY
  - Campo com nome ambíguo (ex: "data", "info", "misc")
  - PII sem campo de encriptação (email, cpf, telefone)
  - Foreign key sem índice

🟡 WARNINGS:
  - Mais de 30 campos em uma tabela (overengineering?)
  - N+1 potential não documentado
  - Falta de soft delete (deleted_at) em entidades principais
```

---

## GATE-06: API CONTRACT GATE

| Campo | Valor |
|---|---|
| **Input** | `blueprint.md` |
| **Output** | `api_contract.yaml` (OpenAPI 3.1) |
| **Check automático** | Todo endpoint tem: request schema, response schema, error codes, auth, exemplos |
| **Check humano** | Contratos fazem sentido para o frontend? |
| **Erro comum** | Endpoint sem error 400/401/500, sem auth definido, sem exemplos |
| **Ação se falhar** | API Contract builder completa seções faltantes |
| **Risco** | R1 |
| **Critério de pronto** | OpenAPI válido + todos os endpoints com 5 campos completos |

---

## GATE-07: SCAFFOLD DRY-RUN GATE

| Campo | Valor |
|---|---|
| **Input** | `blueprint.md` + `api_contract.yaml` + `db_schema` |
| **Output** | `scaffold.plan.md` com árvore de arquivos + diff previsto |
| **Check automático** | Scaffold plan NÃO executa — apenas gera plano |
| **Check humano** | Plano de scaffold aprovado pelo owner antes de qualquer criação |
| **Erro comum** | Scaffold executando diretamente sem dry-run |
| **Ação se falhar** | BLOQUEIO ABSOLUTO — scaffold nunca executa sem plano aprovado |
| **Risco** | R2 |
| **Critério de pronto** | Plan aprovado + `dry_run=True` explícito no relatório |

---

## GATE-08: NO-SECRET SENTINEL GATE

| Campo | Valor |
|---|---|
| **Input** | Qualquer arquivo antes de criação/commit |
| **Output** | `security_cleared: true/false` |
| **Check automático** | Scan por: .env, API keys, tokens, passwords, private keys, secrets |
| **Check humano** | N/A — automático e bloqueante |
| **Erro comum** | .env commitado, token hardcoded em código |
| **Ação se falhar** | BLOQUEIO ABSOLUTO — arquivo não é criado |
| **Risco** | R3 — exige aprovação explícita para override |
| **Critério de pronto** | `security_cleared: true` em todos os arquivos |

---

## GATE-09: NO-DESTRUCTIVE GUARD GATE

| Campo | Valor |
|---|---|
| **Input** | Qualquer ação antes de execução |
| **Output** | `safe_to_execute: true/false` |
| **Check automático** | Bloquear: DELETE, DROP TABLE, overwrite sem backup, push, deploy, git add -A |
| **Check humano** | N/A — automático e bloqueante |
| **Erro comum** | Scaffold sobrescrevendo arquivo existente |
| **Ação se falhar** | BLOQUEIO ABSOLUTO |
| **Risco** | R3 |
| **Critério de pronto** | `safe_to_execute: true` |

---

## GATE-10: TEST PLAN MINIMUM GATE

| Campo | Valor |
|---|---|
| **Input** | `blueprint.md` |
| **Output** | `test_plan.md` com mínimo de testes |
| **Check automático** | Tem: unit tests, integration tests, e2e happy path |
| **Check humano** | Test plan cobre os critérios de aceite do PRD? |
| **Erro comum** | Test plan com "será testado futuramente" |
| **Ação se falhar** | Test Guardian refina o plan |
| **Risco** | R1 |
| **Critério de pronto** | >= 5 test cases mapeados para critérios de aceite do PRD |

---

## GATE-11: SECURITY REVIEW GATE

| Campo | Valor |
|---|---|
| **Input** | `api_contract.yaml` + `blueprint.md` |
| **Output** | `security_review.md` |
| **Check automático** | OWASP Top 10 checklist automático |
| **Check humano** | Security Guardian aprova |
| **Erro comum** | Auth não definido, SQL injection não considerado, rate limiting ausente |
| **Ação se falhar** | Security Guardian lista vulnerabilidades + arquiteto corrige |
| **Risco** | R2 |
| **Critério de pronto** | Zero vulnerabilidades CRÍTICAS no report |

---

## GATE-12: HANDOFF COMPLETE GATE

| Campo | Valor |
|---|---|
| **Input** | Todos os artefatos anteriores |
| **Output** | `handoff_report.md` + `akasha_writeback.json` + `kratos_snapshot.json` |
| **Check automático** | handoff_report.json válido contra `handoff_report_schema.json` |
| **Check humano** | Lucas aprova handoff antes de passar para dev humano |
| **Erro comum** | Handoff sem lista de pendências, sem arquivos gerados, sem próximos passos |
| **Ação se falhar** | Handoff writer completa seções faltantes |
| **Risco** | R1 |
| **Critério de pronto** | Schema válido + aprovação Lucas + AKASHA escrito + KRATOS atualizado |

---

## RESUMO DA PIPELINE DE GATES

```
[IDEA] → GATE-01 → [DISCOVERY] → GATE-02 → [PRD] → GATE-03
       ↓
[BLUEPRINT] → GATE-04 → [SCHEMA] → GATE-05 → [API] → GATE-06
       ↓
[SCAFFOLD PLAN] → GATE-07 + GATE-08 + GATE-09 (sempre, em paralelo)
       ↓
[TEST PLAN] → GATE-10 → [SECURITY] → GATE-11
       ↓
[HANDOFF] → GATE-12 → ✅ ENTREGA
```

**Regra absoluta:** Nenhum gate pode ser pulado sem aprovação explícita em `11_APPROVALS/`.

---
*Gerado por: Perplexity Ultra-Dev | 2026-06-04*
