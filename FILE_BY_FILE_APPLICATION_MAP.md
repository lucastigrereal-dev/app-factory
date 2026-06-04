# File‑by‑File Application Map — System Creation OS V7

Este documento serve como um guia operacional para aplicar os artefatos deste pacote em um repositório de destino.  Cada entrada indica o **caminho do arquivo/pasta**, seu **propósito**, a **ação recomendada** (Create, Reuse, Verify, Defer) e o **nível de risco** associado.  Consulte também `REAUDIT_REPORT.md` para entender as razões por trás de cada decisão.

| Path | Purpose | Action | Risk | Comments |
|---|---|---|---|---|
| `README.md` | Introdução geral ao System Creation OS, pipeline canônico, estrutura e regras de uso. | **Reuse** | R0 | Deve ser mantido e personalizado apenas com detalhes específicos do repositório alvo. |
| `SYSTEM_CANON.md` | Define missão, visão e pipeline obrigatório. | **Reuse** | R0 | Fonte de verdade; alterar somente via processos de evolução. |
| `SYSTEM_STATE.md` | Relata estado atual das implementações e pendências. | **Verify** | R1 | Atualize conforme evoluções; deve refletir a realidade do seu projeto. |
| `GOVERNANCE_POLICY.md` | Política de risco (R0‑R3), dry_run, gates e proibições. | **Reuse** | R0 | Respeitar sem modificações; apenas adicionar exceções documentadas. |
| `ROADMAP.md` | Roadmap em waves com blocos de trabalho. | **Verify** | R1 | Ajuste as datas e prioridades conforme sua disponibilidade. |
| `CHANGELOG.md` | Historial de versões. | **Reuse** | R0 | Deve ser atualizado a cada release. |
| `FILE_MANIFEST.yaml` | Inventário machine‑readable de todos os arquivos. | **Verify** | R1 | Atualize status (`CREATE`, `REUSE`, `VERIFY`, `DEFER`) quando adicionar ou modificar artefatos. |
| `REAUDIT_REPORT.md` | Relatório de re‑auditoria da V6. | **Reuse** | R0 | Serve como referência histórica; não deve ser editado. |
| `FILE_BY_FILE_APPLICATION_MAP.md` | Este próprio mapa de aplicação. | **Verify** | R0 | Atualize se adicionar ou mover arquivos. |
| `CLAUDE_CODE_MASTER_PROMPT.md` | Prompt mestre para execução no Claude Code. | **Reuse** | R0 | Usar como está; alterar apenas para refletir novas etapas ou comandos. |
| `__APPLY_ROOT__/apply_root.md` | Instruções de aplicação do pacote. | **Reuse** | R0 | Ajuste variáveis de ambiente e caminhos conforme necessário. |
| `.claude/commands/` | Comandos específicos para cada fase (audit, plan, validate, export). | **Create** | R1 | Se não existirem, crie conforme os modelos; devem corresponder às skills e agentes. |
| `.claude/agents/` | Agentes especializados com escopo, ferramentas permitidas e saídas. | **Create/Verify** | R1 | Reuse se equivalente no repositório; caso contrário, crie a partir dos modelos. |
| `config/risk_policy.yaml` | Política de risco legível por máquina. | **Verify** | R1 | Adapte regras e níveis conforme políticas internas. |
| `config/gates.yaml` | Definições de gates e verificações automáticas. | **Verify** | R1 | Ajuste para refletir a realidade (ex.: CI/CD, security scans). |
| `config/models.yaml`, `config/skills.yaml`, `config/templates.yaml` | Catálogos de modelos, skills e templates. | **Create/Verify** | R1 | Preencher conforme as skills e templates existentes; adicionar novos quando necessário. |
| `schemas/idea_input_schema.json`, `schemas/prd_output_schema.json` | Esquemas JSON para inputs e outputs. | **Reuse** | R0 | Use como base e versiona quando mudar o formato. |
| `schemas/blueprint_schema.json`, `schemas/scaffold_plan_schema.json` | (Novos) Esquemas para blueprint e scaffold plan. | **Create** | R1 | Preencher com requisitos reais à medida que os planos forem definidos. |
| `src/` | Pacote de código de suporte (governance, memory writeback, scaffold, events). | **Reuse/Verify** | R2 | Reuse o código existente como referência; adapte para o repositório alvo com atenção a `dry_run`.  Criação de novas funções deve seguir os padrões de segurança. |
| `docs/` | Documentação detalhada: PRD, Blueprint, Architecture, Observability, Security, Cost, Design document, etc. | **Reuse/Verify** | R0‑R1 | Reuse como referência; atualize exemplos e links para refletir seu contexto. |
| `tests/` | Testes unitários e integração. | **Create/Verify** | R1 | Adapte ou escreva testes para seu código real; mantê‑los atualizados garante confiabilidade. |
| `upgrade_reports/` | Relatórios de auditoria e evolução anteriores. | **Archive** | R0 | Referência histórica; não deve ser deletado nem modificado. |

> **Observação:** Para arquivos ou pastas não listados explicitamente, utilize o princípio geral: **reutilize quando o conteúdo se aplica diretamente**, **verifique quando precisa adaptar ao contexto**, **crie** quando não existir equivalente e **arquive** quando for obsoleto.  Todas as ações de criação ou modificação devem respeitar o modo `dry_run` e as regras de risco e segurança.