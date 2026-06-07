# Claude Code Master Prompt — System Creation OS V7

## Objetivo

Esta instrução fornece um prompt unificado para executar o **System Creation OS (App Factory)** no contexto do **Claude Code**.  O objetivo é orientar o agente por duas fases iniciais: auditoria e geração, respeitando as políticas de risco, os gates e o modo `dry_run`.  Copie este arquivo para a pasta `.claude/` do seu repositório (ex.: `.claude/CLAUDE.md`) para que seja carregado automaticamente pelo Claude Code.

## Fase 0 — Auditoria Read‑Only

**Propósito:** Avaliar o estado atual do repositório sem modificar nada.  Identificar arquivos ausentes, conflitos, duplicações, gaps e riscos.

**Ações:**

1. **Carregue os manifests e políticas:** leia `FILE_MANIFEST.yaml`, `GOVERNANCE_POLICY.md`, `config/risk_policy.yaml` e `config/gates.yaml` para entender o escopo, regras de risco e gates.
2. **Liste todos os arquivos:** percorra o repositório com ferramentas do Claude Code (por exemplo, `list_files` ou `search`) e compare com o manifesto.  Marque arquivos desconhecidos ou ausentes.
3. **Identifique gaps:** registre arquivos prometidos na constituição que não estão presentes, módulos sem testes, docs superficiais, policies faltantes e riscos de segurança (por exemplo, existência de `.env` ou segredos).
4. **Gere um relatório:** crie um `AUDIT_READONLY_REPORT.md` no diretório `upgrade_reports/` contendo: inventário de arquivos, duplicações, conflitos, riscos, documentos incompletos, código skeleton sem teste, ferramentas proibidas encontradas, gaps contra as especificações e sugestões iniciais.  Não modifique nem crie arquivos além deste relatório.

**Regras:**

* **dry_run=True** deve ser aplicado em todas as operações de leitura e análise.  Nenhum arquivo pode ser editado, deletado ou criado fora da pasta `upgrade_reports/` nesta fase.
* **Ferramentas permitidas:** `read_file`, `list_files`, `search`, `run_tests`, `read_yaml`, `read_json` (conforme suportadas pelo Claude Code).  **Ferramentas proibidas:** `write_file`, `delete_file`, `commit`, `push`, `deploy`, execução de shell.
* **Risco:** Fase 0 é classificada como **R1** (leitura e análise).  Não requer aprovação humana pois não executa side effects.

## Fase 1 — Criação e Melhoria (dry‑run)

**Propósito:** Criar ou melhorar os artefatos canônicos (PRD, blueprint, schemas, docs, templates, configs) de forma controlada, sem alterar o repositório de destino até aprovação.  Esta fase é iterativa; cada artefato deve ser gerado em modo dry‑run e validado por testes antes de qualquer escrita.

**Ações:**

1. **Gerar/Atualizar artefatos**: Use as habilidades (`skills`) e agentes (`agents`) correspondentes para criar ou melhorar:
   - PRD: `skills/prd-generator`
   - Blueprint: `skills/blueprint-generator`
   - Schema: `skills/db-schema-planner`
   - API Contract: `skills/api-contract-builder`
   - Frontend Plan: `skills/frontend-plan-generator`
   - Backend Plan: `skills/backend-plan-generator`
   - Test Plan: `skills/test-plan-generator`
   - Validation Gates: `skills/validation-gate-runner`
   - Handoff Report: `skills/handoff-exporter`
   - Memory Writeback: `skills/memory-writeback`
2. **Valide contra schemas:** Antes de persistir qualquer artefato, valide os resultados contra os JSON Schemas (`schemas/`).  Em caso de falha, corrija o output ou atualize o schema com justificativa.
3. **Respeite os gates:** Consulte `config/gates.yaml` e `docs/ENTERPRISE_QUALITY_GATES.md` para verificar se cada etapa passou nos gates automáticos e se requer aprovação humana.  Não avance para etapas subsequentes quando um gate falhar.
4. **Testes:** Execute `pytest` após a geração de artefatos para garantir que testes skeleton e quaisquer novos testes criados passam.  Crie novos testes sempre que adicionar um módulo ou documento crítico.
5. **Reportar o plano:** Para cada artefato gerado, crie um diff ou plano de alteração (por exemplo, em `upgrade_reports/plan_draft.md`) listando arquivos criados, modificados ou removidos, com a justificativa, risco e verificação.  Não aplique o diff automaticamente.
6. **Obter aprovação:** Consolidar as mudanças em um relatório e aguardar aprovação humana (via checkpoint CP‑3) antes de executar qualquer comando que altere o repositório (por exemplo, `write_file`, `commit`, `merge`).

**Regras:**

* **dry_run=True** continua sendo obrigatório.  Para escrever arquivos, use flags específicas de simulação (por exemplo, `simulate_write`).
* **Ferramentas permitidas:** além das ferramentas de leitura, estão permitidas `generate_prd`, `generate_blueprint`, `plan_scaffold`, `validate_contract`, `run_tests` e `prepare_handoff`, desde que implementadas como skills com dry‑run.
* **Risco:** Fase 1 tem risco **R2** (criação de artefatos) e **R3** para qualquer comando que tente modificar o repositório.  Qualquer ação R3 exige aprovação explícita de um humano.

## Convenções e Boas Práticas

* **Use as rubricas de qualidade:** Consulte `docs/PRD_QUALITY_RUBRIC.md` e `docs/VALIDATION_GATES.md` para avaliar o output dos agentes e propor melhorias.
* **Traceabilidade:** Sempre que uma regra ou requisito for implementado, adicione referências aos arquivos ou testes correspondentes no PRD, blueprint ou contrato.  Isso facilita auditorias futuras.
* **Observabilidade:** Preencha os campos de custo e métricas (quando disponíveis) e utilize `src/cost_tracking/cost_tracker.py` para registrar eventos.
* **Segurança:** Nunca leia ou modifique `.env` ou segredos.  Nunca execute comandos de deploy ou push sem gate e aprovação.

## Exemplo de fluxo

1. **appfactory-audit (Fase 0):**
   ```bash
   /appfactory-audit
   ```
   O agente lê o repositório, gera `upgrade_reports/AUDIT_READONLY_REPORT.md` e encerra.

2. **appfactory-plan (Fase 1, parte 1):**
   ```bash
   /appfactory-plan idea_id="ideia-123" --dry-run
   ```
   Gera PRD, blueprint, DB schema, API contract, planos de front e back, testes e relatórios de custo em modo simulado.

3. **appfactory-validate (Fase 1, parte 2):**
   ```bash
   /appfactory-validate idea_id="ideia-123"
   ```
   Executa validações contra schemas, rodando `pytest` e aplicando gates.  Se um gate falhar, retorna erro e não permite avanço.

4. **appfactory-export (Fase 1, parte 3):**
   ```bash
   /appfactory-export idea_id="ideia-123" --dry-run
   ```
   Prepara pacote para handoff, gera evento de writeback Akasha e snapshot Kratos.  Este comando ainda não escreve arquivos; apenas cria relatório.

Siga estas fases e regras para evoluir a App Factory de maneira segura e auditável.  O objetivo deste prompt é fornecer um roteiro claro e executar cada etapa com disciplina, evitando regressões e criando valor real.