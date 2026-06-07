# FILE: .claude/commands/appfactory-audit.md

## Objetivo
Executar a auditoria inicial em modo read‑only (Fase 0) da App Factory.
Esta auditoria mapeia arquivos, identifica duplicações, conflitos de autoridade,
lacunas em testes e validações, e enumera riscos sem modificar nada.

## Quando usar
Sempre que uma nova wave ou pacote de arquivos for entregue e antes de
qualquer modificação no repositório.  Deve ser o primeiro comando a ser
executado no ciclo de vida de melhoria.

## Inputs esperados
* Diretório raiz da App Factory (o contexto do repositório).
* Manifesto de arquivos (`FILE_MANIFEST.yaml`, se existir).

## Outputs esperados
* Um relatório `upgrade_reports/AUDIT_READONLY_REPORT.md` contendo:
  - lista de arquivos e pastas;
  - conflitos entre documentos;
  - duplicações;
  - documentos incompletos;
  - código skeleton sem testes;
  - artefatos que deveriam ser machine‑readable;
  - faltas de comandos/agents/skills;
  - riscos de segurança e de overengineering;
  - menor MVP operacional recomendado.

## Paths permitidos
Somente leitura: todos os arquivos do repositório.  Nenhum arquivo deve
ser criado ou modificado nesta etapa.

## Risco
**R0** — Ação segura, sem efeitos colaterais.

## Regras de segurança
* Não executar scripts ou código; apenas ler arquivos.
* Não acessar `.env`, segredos ou arquivos fora do repositório.
* Não modificar o manifesto ou qualquer arquivo.

## Critérios de aceite
* O relatório lista todos os achados com clareza.
* Nenhum arquivo é alterado ou criado durante a auditoria.
* O risco de cada item é classificado (R0–R3).

## Proibições
* Não alterar o repositório.
* Não omitir riscos ou conflitos identificados.