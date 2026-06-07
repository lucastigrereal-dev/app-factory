# App Factory v3.1 — Forja Enterprise

Fabrica de criacao de apps enterprise de ponta a ponta (backend + frontend + DB + tests + Docker).

## Stack
- **Orquestracao:** Python 3.12
- **Gateway LLM:** Router Ollama direto (porta 11434)
  - qwen2.5-coder:7b (primary), llama3.1:8b, llama3.2:3b (fallback)
- **Template Engine:** string.Template (stdlib, zero deps)
- **Backend Gerado:** FastAPI + Pydantic (fake in-memory DB, pronto para SQLAlchemy)
- **Frontend Gerado:** HTML + Tailwind CDN + JS vanilla
- **Tests:** pytest + FastAPI TestClient
- **Infra:** Docker + docker-compose.yml

## Pipeline E2E (12 passos)
Intake -> Schema (SQL + Pydantic) -> API (FastAPI CRUD) -> Frontend (Dashboard) -> Tests -> Scaffold -> Snapshot

## Quick Start (Windows)
```powershell
# 1. Verificar Ollama rodando
python src/llm/gateway.py

# 2. Rodar smoke tests
python tests/smoke_test.py
python tests/smoke_test_v2.py

# 3. Gerar app enterprise completo
python src/orchestrator_v2.py --idea "CRM para imobiliaria" --app-name "meu-crm" --type crm

# 4. Ou gerar dashboard
python src/orchestrator_v2.py --idea "Dashboard de vendas" --app-name "dash-vendas" --type dashboard

# 5. Ou gerar SaaS MVP
python src/orchestrator_v2.py --idea "SaaS de agendamento" --app-name "agenda-app" --type saas
```

## Estrutura
```
src/
  llm/gateway.py          # Gateway LLM (Ollama direct + fallback)
  generators/
    schema_generator.py   # Gera SQL + Pydantic via LLM + templates
    api_generator.py      # Gera FastAPI CRUD via templates
    frontend_generator.py # Gera HTML dashboard via templates
    test_generator.py     # Gera pytest via templates
  scaffold/renderer.py    # Cria arquivos fisicos no disco
  orchestrator_v2.py      # Pipeline E2E completo
tests/
  smoke_test.py           # 3/3 validacoes (gateway, landing, logs)
  smoke_test_v2.py        # 4/4 validacoes (schema, api, frontend, renderer)
templates/                # Templates Jinja2/string.Template
artifacts/                # Apps gerados (output)
  taskboard/              # Exemplo: dashboard
  crm-imob/               # Exemplo: CRM
  agenda-clinica/         # Exemplo: SaaS
.claude/skills/
  create-landing-page/    # Landing page (Fase 1)
  create-dashboard/       # Dashboard enterprise
  create-saas-mvp/        # SaaS MVP
  create-crm/             # CRM completo
```

## Status
✅ Fase 0 (Setup) — COMPLETA
✅ Fase 1 (Gateway + Skill Engine + Landing Page) — COMPLETA
✅ Fase 2 (Schema + API + Frontend + Tests + Scaffold) — COMPLETA
  - 3 apps enterprise gerados e validados
  - Smoke tests: 3/3 + 4/4 PASS

## Documentacao
- `APP_FACTORY_PRD_BLUEPRINT_V3.md` — PRD completo v3.1
- `go.bat` — Executa smoke tests + gera demo + abre browser
