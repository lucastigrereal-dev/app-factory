# ADR‑0002 — Risk Gates R0–R3

*Status: Accepted*  
*Date: 2026‑06‑04*

## Contexto

A política de governança do System Creation OS define quatro níveis de risco (R0–R3).  Decidiu‑se registrar formalmente como esses níveis determinam checkpoints (gates) e aprovações.

## Decisão

1. **R0 (Leitura / Documentação)**  
   - Abrange leitura de arquivos, navegação e criação de documentação sem efeitos externos.  
   - Pode ser executado automaticamente.  
   - Gate: **CP‑0**.

2. **R1 (Configuração e Código Interno)**  
   - Inclui criação ou modificação de arquivos locais (YAML, Markdown, Python dry‑run).  
   - Não aciona serviços externos.  
   - Pode ser executado automaticamente, mas requer revisão de PRs.  
   - Gate: **CP‑1**.

3. **R2 (Integração Interna)**  
   - Abrange execução de código dry‑run que poderia, em execução real, interagir com serviços externos.  
   - Requer validação de QA.  
   - Gate: **CP‑2**.

4. **R3 (Efeito Externo)**  
   - Inclui qualquer operação que gera side effects em serviços externos (deploy, push, AKASHA writeback, notificação real).  
   - **Sempre** requer aprovação humana explícita.  
   - Gate: **CP‑3**.

## Consequências

* O pipeline deve emitir eventos indicando quando um item atinge um gate.
* Automação só poderá prosseguir de R2 para R3 com aprovação registrada.
* Todas as ferramentas (CLI, Claude Code) devem reforçar essas regras.

## Alternativas Consideradas

Nenhuma.  Esta é uma formalização das práticas já adotadas.