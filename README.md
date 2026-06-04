# System Creation OS — App Factory
> **O sistema operacional de criação de produtos digitais do OMNISVERSO.**

Este repositório contém um **pacote completo** de arquivos que definem e operacionalizam o System Creation OS (também chamado internamente de App Factory).  O objetivo deste pack é oferecer um conjunto plug‑and‑play de documentação, contratos, templates e código de suporte para que qualquer pessoa possa explorar, auditar e estender o System Creation OS sem acesso a infraestrutura privada ou a contextos ocultos.

## O que é

O **System Creation OS** transforma qualquer intenção de produto digital num pacote completo de construção:
ideia → PRD → blueprint → schema → API contract → plano de front‑end → testes → scaffold → handoff → escrita na memória (AKASHA) → snapshot no cockpit (KRATOS).  Não é um gerador de código, mas sim uma **esteira profissional** com governança, checkpoints e contratos bem definidos.

## Pipeline Canônico

```
Ideia → Intake → Discovery → PRD → Blueprint → Schema → API
     → Frontend Plan → Test Plan → Security Gate → Scaffold
     → Validation → Export → AKASHA → KRATOS
```

## Estrutura Principal

| Pasta | Conteúdo |
|---|---|
| `docs/` | Documentação de alto nível (PRD, Blueprint, Cockpit, Arsenal, Execução), notas de especialista, ADRs, runbooks, **protocolos (API_CONTRACTS, DB_SCHEMA, KRATOS, AKASHA, BRIDGE)** e políticas. |
| `config/` | YAMLs legíveis por máquina (políticas de risco, gates, taxonomia de eventos, schemas de contratos, modelos e skills). |
| `src/` | Código‑fonte para bridges WAF‑01/02/03, governança, bus de eventos e integradores.  Todos os módulos operam em modo dry‑run por padrão. |
| `templates/` | Templates iniciais para PRDs e outros artefatos (expansível conforme novos produtos). |
| `skills/` | Catálogo de skills executáveis pelo Claude Code, incluindo intake, geração de PRD, blueprint, scaffolding, snapshot, writeback e criação de produtos como landing pages, CRMs, dashboards e SaaS. |
| `.claude/commands/` | Conjunto de comandos customizados do Claude Code correspondentes a cada etapa do pipeline (intake, plan, blueprint, schema, API contract, frontend plan, test plan, scaffold, export, writeback, snapshot). |
| `.claude/agents/` | Conjunto de agentes especializados (arquitetura, PRD writing, schema planning, API contract building, frontend planning, test guarding, scaffold guarding, bridge engineering, governance auditing, risk classification, writeback e snapshot). |
| `tests/` | Testes unitários e de integração garantindo que o código de suporte respeita o modo dry‑run e valida schemas. |
| `examples/` | Exemplos de objetos JSON e contratos que respeitam os schemas definidos em `config/`. |
| `SYSTEM_CANON.md` | Fonte de verdade canônica: define a missão, pipeline, tecnologias e integrações obrigatórias. |
| `SYSTEM_STATE.md` | Estado atual real: lista quais etapas do pipeline estão prontas e quais bridges faltam implementar. |
| `GOVERNANCE_POLICY.md` | Política de governança: define níveis de risco (R0–R3), checkpoints (CP‑0–CP‑3) e ações proibidas. |
| `ROADMAP.md` | Roadmap de alto nível para fechar os gaps identificados no estado atual. |
| `FILE_MANIFEST.yaml` | Inventário machine‑readable de todos os arquivos deste pack, com propósito, risco e dependências. |
| `PROMPT_FINAL_PARA_CLAUDE_CODE.md` | Prompt conciso para inicializar um projeto no Claude Code usando este pack. |
| `BUILD_REPORT.md` | Relatório explicando como este pack foi construído e quais melhorias foram aplicadas. |

## Início rápido

Para começar a utilizar este pack:

1. Leia `SYSTEM_CANON.md` para compreender a definição canônica e o pipeline obrigatório do System Creation OS.
2. Revise `SYSTEM_STATE.md` para ver o status atual (o que já está pronto e o que está faltando).
3. Explore os documentos em `docs/` (PRD, Blueprint, Cockpit, Arsenal, Execução, notas de especialista, runbooks, políticas e ADRs) para familiarizar‑se com o contexto e os requisitos.
4. Consulte `GOVERNANCE_POLICY.md` para entender o modelo de segurança (níveis de risco R0–R3, modo `dry_run` padrão e gates CP‑0–CP‑3).
5. Use `FILE_MANIFEST.yaml` como índice para localizar arquivos e entender se são criações novas ou reutilizações.
6. Antes de qualquer execução, leia `REAUDIT_REPORT.md` para entender o que foi auditado na versão 6 e quais são os principais gaps.  Consulte também `FILE_BY_FILE_APPLICATION_MAP.md` para saber como aplicar cada artefato.
7. Ao executar comandos no ambiente Claude Code, siga o prompt mestre em `CLAUDE_CODE_MASTER_PROMPT.md` (ou copie para `.claude/CLAUDE.md`), que descreve a Fase 0 (auditoria read‑only) e Fase 1 (criação/melhoria) com políticas de risco e gates.  Use `PROMPT_FINAL_PARA_CLAUDE_CODE.md` apenas como referência histórica.
8. Para aplicar o pacote a um repositório real, veja `__APPLY_ROOT__/apply_root.md` para instruções passo a passo (clonagem, ambiente virtual, pre‑commit, cópia de arquivos, execução de testes).  Lembre‑se de trabalhar sempre em modo `dry_run` e obter aprovação para ações R3.

## Regras invioláveis

* `dry_run=True` em todos os módulos por padrão.  Nenhum side effect deve ocorrer sem consentimento.
* Nenhum push/deploy sem aprovação explícita (Checkpoint CP‑3).
* Nunca ler ou escrever arquivos `.env` via agentes ou comandos.
* Proibido executar `git add -A` ou qualquer operação de staging global; sempre com caminhos explícitos.
* **R3 exige aprovação humana obrigatória.**

## Sobre este pack

Além de consolidar todos os documentos originais fornecidos pelo usuário (PRD, blueprint, cockpit, arsenal, execução e notas de especialista), este pack inclui melhorias significativas:

* **Novas documentações:** além das descritas na versão anterior (`docs/ARCHITECTURE.md`, `docs/CLAUDE_CODE_RUNBOOK.md`, `docs/VALIDATION_GATES.md`, `docs/ERROR_PLAYBOOK.md`, `docs/SECURITY_POLICY.md` e `docs/ADR/ADR‑0001-system-creation-os-mvp.md`), esta versão inclui diretrizes para **contratos de API** (`docs/API_CONTRACTS.md`), **schemas de banco** (`docs/DB_SCHEMA.md`), os protocolos de **writeback AKASHA** (`docs/AKASHA_WRITEBACK_PROTOCOL.md`) e **snapshot KRATOS** (`docs/KRATOS_SNAPSHOT_PROTOCOL.md`), a especificação da **bridge OMNIS↔App Factory** (`docs/OMNIS_APP_FACTORY_BRIDGE.md`) e duas novas ADRs (`docs/ADR/ADR‑0002-risk-gates-r0-r3.md` e `docs/ADR/ADR‑0003-markdown-yaml-as-source-of-truth.md`).
* **Configurações ampliadas:** `config/skills.yaml` e `config/models.yaml` listam os módulos e modelos suportados.  Schemas em `config/` definem os contratos machine‑readable (mission package, work order result, AKASHA writeback e snapshot KRATOS).
* **Código de suporte:** São fornecidos esboços (`src/api/kratos_status.py`, `src/bridge/omnis_bridge.py`, `src/bridge/mission_package.py`, `src/bridge/work_order_result.py`, `src/memory_writeback/akasha_writeback.py` e módulos adicionais em `src/events/` e `src/governance/`) em modo dry‑run para conectar o System Creation OS aos sistemas OMNIS, KRATOS e AKASHA.
* **Testes iniciais:** Testes em `tests/unit/` e `tests/integration/` asseguram que o modo dry‑run é respeitado, que riscos R3 são bloqueados sem aprovação e que os schemas podem ser carregados.  Testes adicionais cobrem mission packages, work order results e fluxos de bridge.

Este pacote é auto‑suficiente; basta descompactar a pasta `system-creation-os-file-pack-v4` em seu projeto ou fornecer o zip diretamente ao Claude Code.  Como o modo padrão é dry‑run, não há efeitos colaterais até que você os autorize explicitamente.

---
*© 2026 OMNISVERSO – System Creation OS v1.0*