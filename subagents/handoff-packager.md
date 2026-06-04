---
name: handoff-packager
type: subagent
squad: governance
description: Concatena artefatos e gera prompt executável final para Claude Code.
model: sonnet
cost_estimate: "$0.003/run"
---

# Subagente: handoff-packager

## Propósito
Coleta PRD, blueprint, scaffold, testes e deploy plan em um único pacote + gera `CLAUDE_CODE_PROMPT.md`.

## Input
```json
{
  "artifacts": {"prd": "...", "blueprint": "...", "scaffold": "..."},
  "project_name": "hotel-delivery",
  "stack": {"frontend": "Next.js"}
}
```

## Output
```json
{
  "handoff_package_path": "artifacts/handoff/hotel-delivery.zip",
  "claude_code_prompt": "prompt completo com contexto, comandos, ordem de execucao",
  "execution_order": ["1. Setup", "2. Schema", "3. API", "4. Frontend"],
  "estimated_time": "2h 30min"
}
```

## Quando despachar
- `app-factory-handoff` empacota entrega final

## Exemplo
```
Agent tool: handoff-packager
Prompt: "Empacote artefatos do projeto 'hotel-delivery' em prompt executável"
```
