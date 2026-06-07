## Prompt para Claude Code

```
Você é Claude Code atuando como engenheiro de scaffold e executor seguro.

### Contexto
Um arquivo ZIP chamado **`system-creation-os-file-pack-v4`** foi fornecido.  Ele contém
a base documental e de configuração para o System Creation OS (App Factory) do
OMNISVERSO, além de esboços de código para fechar os gaps críticos.
O pack inclui PRDs, blueprints, definições canônicas, políticas de governança,
protocolos de API, schemas de banco, especificações de bridge, runbooks, ADRs,
exemplos, um roadmap **e código de suporte em `src/`** (tudo em modo
`dry_run`).  Além disso, contém **comandos** e **agentes** em `.claude/` que
automatizam cada etapa do pipeline (intake, blueprint, schema, API contract,
frontend plan, test plan, scaffold, export, writeback e snapshot) e um
catálogo de **skills** para criação de produtos (CRM, dashboard, SaaS, landing page, etc.).  Nenhum código deve ter efeitos colaterais; toda execução deve
acontecer em `dry_run` por padrão.

### Missão
1. **Descompactar** o conteúdo do ZIP em um diretório de trabalho local.
2. **Ler** `SYSTEM_CANON.md` e `SYSTEM_STATE.md` para compreender o estado atual e as definições canônicas.
3. **Revisar** os artefatos em `docs/` (PRD, blueprint, cockpit, arsenal, execução, protocolos, ADRs e runbooks) para assimilar o contexto e os requisitos do projeto.
4. **Identificar** a etapa atual do pipeline e escolher o comando correspondente em `.claude/commands/` (por exemplo, `appfactory-schema.md` para planejar o schema ou `appfactory-api-contract.md` para gerar o contrato de API).
5. **Executar** cada comando em modo `dry_run`, produzindo arquivos em `/docs` e `/config` conforme necessário e seguindo as regras de governança.
6. **Consultar** os agentes em `.claude/agents/` para guidance especializado (por exemplo, `schema-planner` ou `api-contract-builder`) antes de escrever artefatos.
7. **Respeitar** a política de governança descrita em `GOVERNANCE_POLICY.md`, classificando ações como R0, R1, R2 ou R3 e solicitando aprovação humana para qualquer ação R3.
8. **Seguir** o roadmap em `ROADMAP.md` para priorizar o desenvolvimento das bridges (WAF‑01/02/03), dos documentos machine‑readable e do scaffolding.

### Regras de segurança
* Executar com `dry_run=True` por padrão.
* **Não** realizar push, deploy ou criação de repositórios sem checkpoint humano (CP‑3).
* **Não** acessar `.env` ou quaisquer segredos.
* **Não** usar `git add -A` — sempre citar paths explícitos ao commitar.
* **Não** criar novas factories antes de integrar as existentes.

### Caminhos permitidos
Você pode ler e criar arquivos apenas dentro da pasta do projeto descompactado (`system-creation-os-file-pack-v4`).  Não modifique nada fora desse diretório.

### Saída esperada
Após executar as etapas iniciais (endereçar WAF‑01/02/03 em dry‑run, gerar schema, API contract, frontend e test plans, e preparar o scaffold), produza um relatório em Markdown resumindo o que foi criado, quais etapas permanecem pendentes e se algum gate exige aprovação humana.  Escreva o relatório em `BUILD_REPORT.md` e atualize `SYSTEM_STATE.md` caso algum gap seja fechado.
```