# How to Apply the System Creation OS Pack (V7)

Esta instrução descreve como aplicar o **APP_FACTORY_EXPONENTIAL_EVOLUTION_PACK_V7** a um repositório de destino ou projeto local.  O objetivo é integrar a esteira de criação de apps sem causar efeitos colaterais inesperados.

## Pré‑requisitos

1. **Git** instalado e configurado no ambiente local.
2. **Python 3.10+** com `virtualenv` ou `conda` disponível.
3. **Node.js 16+** se pretende usar os templates de front‑end.
4. Acesso ao repositório alvo (ex.: `lucastigrereal-dev/omnis-control`) com permissões de leitura/escrita.
5. Claude Code configurado para executar comandos locais em modo `dry_run`.

## Passos

1. **Clonar o repositório alvo** (ex.: `omnis-control`) em um diretório local separado.
   ```bash
   git clone git@github.com:lucastigrereal-dev/omnis-control.git
   cd omnis-control
   ```

2. **Extrair o pacote V7**.  Se você recebeu um arquivo zip (`APP_FACTORY_EXPONENTIAL_EVOLUTION_PACK_V7.zip`), descompacte‑o em um diretório temporário.
   ```bash
   unzip APP_FACTORY_EXPONENTIAL_EVOLUTION_PACK_V7.zip -d /tmp/app_factory_v7
   ```

3. **Criar um ambiente Python** para executar testes e scripts de apoio.
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r /tmp/app_factory_v7/requirements.txt  # se existir um arquivo de requirements
   ```

4. **Copiar arquivos e pastas** conforme o mapa de aplicação.
   - Reutilize `README.md`, `SYSTEM_CANON.md` e outros arquivos canônicos como referência.
   - Copie a pasta `config/` para o repositório alvo, preservando arquivos já existentes e mesclando políticas.
   - Copie `docs/` para dentro de uma pasta de documentação (`docs/app_factory_v7/`), mantendo histórico.
   - Copie a pasta `.claude/` para a raiz do repositório.  Ajuste `settings.json` (quando implementado) para refletir suas permissões.
   - Não sobrescreva arquivos sem revisar; use o `FILE_BY_FILE_APPLICATION_MAP.md` como guia.

5. **Instalar hooks de pre‑commit** (se ainda não instalados).
   ```bash
   pip install pre-commit
   pre-commit install
   ```

6. **Executar testes** para garantir que os artefatos foram aplicados corretamente.
   ```bash
   pytest -q
   ```
   Todos os testes devem passar antes de prosseguir; corrija falhas e atualize configurações conforme necessário.

7. **Rodar o CLI** de auditoria para validar a instalação (quando o CLI estiver implementado).
   ```bash
   python -m src.cli.appfactory_cli audit --dry-run
   ```

8. **Executar o Claude Code com o prompt mestre**.  Aponte o agente para o arquivo `CLAUDE_CODE_MASTER_PROMPT.md` e siga as instruções.  Comece com a Fase 0 (auditoria read‑only) antes de tentar criar ou modificar qualquer artefato.

## Observações Importantes

* **Modo Dry‑Run:** Por padrão, todos os comandos e scripts devem rodar em modo dry‑run, sem efeitos colaterais externos.  Somente depois de revisar a saída e obter aprovação humana (para riscos R3) é que você deve remover a flag `--dry-run`.
* **Não sobrescrever sem backup:** Se precisar modificar arquivos existentes, crie cópias de segurança ou use branches separados.  Não remova `.env` ou segredos; eles nunca devem ser lidos ou escritos por agentes.
* **Atualize o manifesto:** Após copiar novos arquivos ou modificar existentes, atualize `FILE_MANIFEST.yaml` com a ação correspondente (CREATE, REUSE, VERIFY ou DEFER).
* **Integração OMNIS:** Para aproveitar classes determinísticas existentes em `omnis-control` (como `AppFactoryPlanner`), considere integrar esses módulos como fallback para validação ou comparação.  Eles podem ajudar a verificar se PRDs, blueprints e scaffolds gerados por LLMs são coerentes com a lógica determinística.

Seguindo estes passos, você aplicará o pack V7 de forma segura, auditável e pronta para evoluir a App Factory em direção à geração de código real, CI/CD e governança enterprise.