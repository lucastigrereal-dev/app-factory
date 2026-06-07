# System Creation OS — App Factory
> **O sistema operacional de criação de produtos digitais do OMNISVERSO.**

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Risk Policy](https://img.shields.io/badge/risk-R0--R3-orange)]()
[![dry_run](https://img.shields.io/badge/default-dry__run%3DTrue-blue)]()

## O Que É

O System Creation OS transforma qualquer intenção de produto digital num pacote completo:
ideia → PRD → blueprint → schema → API contract → scaffold → testes → handoff → memória.

Não é um gerador de código. É uma **esteira profissional** com documentos, contratos, gates e governança.

## Pipeline Canônico

```
Ideia → Intake → Discovery → PRD → Blueprint → Schema → API → Frontend Plan
     → Test Plan → Security Gate → Scaffold → Validation → Export → AKASHA → KRATOS
```

## Estrutura Principal

| Pasta | Conteúdo |
|---|---|
| `docs/` | Arquitetura, contratos, runbooks, ADRs |
| `config/` | YAMLs machine-readable (skills, models, gates, risk) |
| `src/` | Código dos bridges WAF-01/02/03 e governança |
| `templates/` | Templates por tipo de produto |
| `skills/` | Skills executáveis pelo Claude Code |
| `.claude/commands/` | Comandos `/appfactory-*` |
| `.claude/agents/` | Agentes especializados |
| `tests/` | Testes unitários e de integração |
| `examples/` | Exemplos JSON canônicos |

## Início Rápido

```bash
# Auditoria read-only (sem side effects)
python -m pytest tests/unit/ -v --dry-run

# Verificar estado atual
cat SYSTEM_STATE.md

# Rodar command de intake no Claude Code
/appfactory-intake
```

## Regras Invioláveis

- `dry_run=True` em todos os módulos por padrão
- Nenhum push/deploy sem GO explícito do Lucas
- Nenhum acesso a `.env` via agente
- R3 exige checkpoint humano obrigatório (CP-3)
- Ver `GOVERNANCE_POLICY.md` para regras completas

## Documentação

- [Arquitetura](docs/ARCHITECTURE.md)
- [Runbook Claude Code](docs/CLAUDE_CODE_RUNBOOK.md)
- [Política de Governança](GOVERNANCE_POLICY.md)
- [Gates de Validação](docs/VALIDATION_GATES.md)
- [ADR-0001 MVP](docs/ADR/ADR-0001-system-creation-os-mvp.md)

## Status

Ver [SYSTEM_STATE.md](SYSTEM_STATE.md) para estado atual atualizado.

---
*OMNISVERSO · System Creation OS v1.0 · 2026*
