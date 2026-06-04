# System Design Document — App Factory V7

## Overview

O **System Creation OS** é a esteira de criação de produtos digitais do OMNISVERSO.  Sua função é receber uma ideia de produto e, de forma orquestrada e governada, gerar todos os artefatos necessários para construir o produto: documento de requisitos (PRD), blueprint técnico, planos de banco de dados, contratos de API, planos de frontend e backend, planos de teste, relatórios de validação, pacotes de scaffolding, eventos de memória e snapshots de status.  Diferente de plataformas de geração de código superficiais, o System Creation OS enfatiza documentação canônica, contratos machine‑readable, governança de risco, gates de aprovação e integração com sistemas internos como Akasha (memória), Kratos (cockpit) e OMNIS (controle central).

## Architectural Layers

O design é organizado em camadas para separar responsabilidades e facilitar manutenção:

1. **Intake & Discovery:** captam a ideia inicial e fazem perguntas de clarificação.  Produzem um registro estruturado (`idea_input_schema.json`) e um resumo de descoberta.
2. **PRD:** transforma o discovery em um documento estruturado de requisitos com objetivos, escopo, funcionalidades, critérios de aceitação e riscos.  Usa `docs/PRD_QUALITY_RUBRIC.md` para avaliar qualidade e `schemas/prd_output_schema.json` para validar formato.
3. **Blueprint:** converte o PRD em um blueprint técnico contendo módulos, data models, endpoints de API, árvores de componentes e stack recomendada.  Validação futura usará `schemas/blueprint_schema.json`.
4. **Schema & Contracts:** derivam modelos de banco de dados (SQLDDL ou Prisma), definem contratos de API em OpenAPI/JSON Schema e preparam planos de scaffolding.  Documentados em `docs/DB_SCHEMA.md` e `docs/API_CONTRACTS.md`.
5. **Planning Layers:** incluem planos de frontend (`docs/ARCHITECTURE.md` + geradores de UI), backend, testes e scaffolding.  Ligam as necessidades do blueprint a templates reais.
6. **Governance Layer:** implementa políticas de risco (`config/risk_policy.yaml`), gates (`config/gates.yaml`), cost tracking (`src/cost_tracking/`) e observabilidade (`docs/OBSERVABILITY_MODEL.md`).  A governança decide se uma etapa pode avançar ou se precisa de aprovação humana.
7. **Memory & Snapshot Layer:** registra decisões e artefatos em Akasha (memória vetorial) e envia snapshots de status ao Kratos (cockpit).  Protocolos em `docs/AKASHA_WRITEBACK_PROTOCOL.md` e `docs/KRATOS_SNAPSHOT_PROTOCOL.md`.
8. **CLI & Agents:** expõe comandos (via `.claude/commands/`) e agentes (`.claude/agents/`) para o Claude Code executar tarefas de intake, planning, validation, export e writeback.  Cada agente define escopo, inputs, outputs, ferramentas permitidas e regras de fallback.

## Data Flow

O pipeline canônico (veja `SYSTEM_CANON.md`) segue o fluxo: **Ideia → Intake → Discovery → PRD → Blueprint → Schema → Contracts → Plans → Scaffold → Validation → Export → Writeback → Snapshot**.  Em cada transição:

1. **Contracts & Schemas:** definem a estrutura de entradas e saídas.  Por exemplo, `idea_input_schema.json` garante que a ideia contenha título, descrição, público alvo, funcionalidades, restrições e nível de risco.
2. **Skills & Agents:** processam o input e produzem o output.  Cada skill utiliza templates e algoritmos determinísticos quando possível (reaproveitando o planner em `omnis-control`) ou chama modelos de LLM com prompts específicos.
3. **Gates & Policy:** antes de avançar, o artefato passa por verificações automáticas (lint, validação de schema, teste de segurança) e pode exigir aprovação humana se o risco for R3 ou se o gate definir.
4. **Event Bus:** durante a execução, eventos são publicados (por exemplo, `app.idea.created`, `prd.generated`, `scaffold.planned`) e podem acionar notificações, gravação em Akasha ou update no Kratos.

## Integration Points

* **OMNIS Planner:** Os módulos existentes em `omnis-control` fornecem classes `AppIdea`, `AppRequirement`, `AppBlueprint`, `AppArtifact` e um `AppFactoryPlanner` determinístico【800680552272303†L0-L55】.  Esta V7 recomenda integrar esses módulos como fallback ou verificador de consistência para outputs gerados por LLMs, garantindo que o resultado seja coerente com regras definidas.
* **Akasha (Memory):** Use `src/memory_writeback/akasha_writeback.py` para empacotar eventos de writeback.  O contract `akasha_writeback.schema.yaml` define campos obrigatórios como decision, context, artifacts e lessons.
* **Kratos (Cockpit):** O módulo `src/api/kratos_status.py` expõe um endpoint para publicar snapshots de progresso e custos.  O schema `kratos_snapshot.schema.yaml` regula a estrutura deste payload.
* **n8n & LiteLLM:** Na camada de execução, o blueprint pode incluir automações definidas em `docs/ARSENAL.md` (ex.: integração com n8n) e o uso de `LiteLLM/Ollama` para hospedar modelos customizados.

## Future Work

* **UI and Code Generation:** As camadas de blueprint e planning ainda não geram código real.  A evolução propõe a integração com bibliotecas como shadcn/ui e frameworks como v0 para produzir componentes React e rotas de API automaticamente.
* **CI/CD & Pre‑commit:** Incluir workflows GitHub Actions e ganchos pre‑commit para testar, lintar e verificar segredos antes de merges ou execuções.
* **Autonomous Agents:** Evoluir os agentes de prompts em `.claude/agents/` para servidores MCP reais (por exemplo, usando FastAPI) que possam ser chamados localmente pelo Claude Code ou integrados ao orchestrator.

Este documento serve como referência de alto nível para desenvolvedores e arquitetos que desejam entender como as peças se encaixam e onde expandir a fábrica no futuro.