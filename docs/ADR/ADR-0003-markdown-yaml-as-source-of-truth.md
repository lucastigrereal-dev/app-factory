# ADR‑0003 — Markdown e YAML como fontes de verdade

*Status: Accepted*  
*Date: 2026‑06‑04*

## Contexto

Durante as fases iniciais do System Creation OS, foram utilizados Notion, planilhas e outros formatos dispersos para registrar requisitos e decisões.  Isso gerou inconsistências e perda de versionamento.

## Decisão

1. **Arquivos de texto legíveis** (Markdown) serão a **fonte de verdade** para requisitos, PRDs, blueprints, runbooks e políticas.  
2. **Arquivos YAML/JSON** serão a **fonte de verdade** para configurações, schemas e contratos legíveis por máquina.  
3. Nenhuma informação durável deve residir exclusivamente em ferramentas visuais (Notion, ClickUp); estes podem consumir os arquivos, mas não substituí-los.  
4. Todos os artefatos devem ser versionados via Git, com commits explícitos (sem `git add -A`).

## Consequências

* O workflow gira em torno de arquivos rastreáveis, revisáveis e passíveis de linting.
* Equipes podem automatizar validações (CI) para arquivos YAML e Markdown.
* A dependência de ferramentas SaaS para armazenamento de informação crítica diminui.

## Alternativas Consideradas

Manter Notion como fonte de verdade.  Rejeitada por falta de versionamento e risco de bloqueio de acesso.