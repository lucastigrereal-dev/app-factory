# SYSTEM_CANON.md — Fonte de Verdade Canônica
> **Versão:** 1.0 | **Status:** ATIVO | **Última revisão:** 2026-06-03

## Definição Oficial

**System Creation OS** é o sistema operacional de criação de produtos digitais do OMNISVERSO.
Ele converte qualquer intenção de produto em um pacote completo de construção, documentado,
governado e rastreável.

**Nome canônico:** `system-creation-os`
**Nome interno:** `app-factory`
**Namespace de eventos:** `app.*`, `prd.*`, `scaffold.*`, `factory.*`
**Repo principal:** `omnis-appfactory` (ou módulo dentro de `omnis-control`)

## Pipeline Canônico Obrigatório

```
1.  idea-intake            → idea_package.json         [R0]
2.  context-restore        → history_context.json       [R0]
3.  discovery              → discovery_brief.md         [R0]
4.  product-classification → classification.json        [R0]
5.  prd-generator          → PRD_[produto].md           [R1]
6.  blueprint-generator    → blueprint.yaml             [R1]
7.  db-schema-planner      → schema_plan.sql            [R1] dry_run
8.  api-contract-builder   → api_contracts.yaml         [R1]
9.  frontend-plan-generator→ frontend_plan.md           [R1]
10. test-plan-generator    → test_plan.md               [R1]
11. security-gate          → risk_report.md             [R2] CP-2
12. scaffold-planner       → file_tree.yaml             [R2] dry_run
13. repo-scaffolder        → GitHub repo criado         [R3] CP-3 obrigatório
14. validation-gate-runner → validation_report.md       [R1]
15. handoff-exporter       → handoff_[produto].md       [R1]
16. memory-writeback       → AKASHA event               [R0]
17. kratos-snapshot        → KRATOS update              [R0]
```

## Stack Canônica

| Camada | Tecnologia |
|---|---|
| API Backend | FastAPI + Python 3.12 |
| CLI | Typer + Rich |
| Frontend | React + Tailwind CSS |
| BD Relacional | PostgreSQL + pgvector |
| Cache/Queue | Redis |
| Vetor | Qdrant |
| LLM | LiteLLM + Claude (Sonnet/Haiku) |
| Automação | n8n |
| Observabilidade | Langfuse + OpenTelemetry |
| Testes | pytest + bun + tsc |
| Scaffold | GitHub API |

## Fontes de Verdade (Hierarquia)

1. `SYSTEM_CANON.md` — esta definição (mais alta autoridade)
2. `config/*.yaml` — configuração machine-readable
3. `docs/PRD_SYSTEM_CREATION_OS.md` — requisitos detalhados
4. `SYSTEM_STATE.md` — estado real atual
5. AKASHA — memória semântica persistida

## Produtos Suportados (Day 1)

- `landing_page` — landing pages institucionais e de produto
- `crm` — CRM básico com funil e entidades
- `dashboard` — dashboards analíticos e operacionais
- `saas_mvp` — MVPs de SaaS com auth, billing e CRUD
- `automation` — workflows n8n/Make
- `content_system` — sistemas de conteúdo e publicação
- `internal_tool` — ferramentas internas
- `research_product` — produtos de pesquisa e análise

## Integrações Obrigatórias

| Sistema | Integração | Status |
|---|---|---|
| OMNIS Core | Bridge WAF-01 | ❌ PENDENTE |
| KRATOS Cockpit | Snapshot WAF-02 | ❌ PENDENTE |
| AKASHA Memory | Writeback WAF-03 | ❌ PENDENTE |
| Event Bus | Eventos `app.*` | ❌ PENDENTE |

## Proibições Absolutas

- ❌ Deploy automático sem GO humano
- ❌ Acesso a `.env` via agente
- ❌ `git push` sem checkpoint CP-3
- ❌ `git add -A` (sempre explicit path commits)
- ❌ Criar nova factory antes de plugar as existentes
- ❌ Modificar dados de produção em dry_run

## Revisão

Este arquivo é revisado a cada major wave ou decisão arquitetural.
Mudanças requerem ADR correspondente em `docs/ADR/`.
