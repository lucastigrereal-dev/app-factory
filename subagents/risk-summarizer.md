---
name: risk-summarizer
type: subagent
squad: governance
description: Resume todos os riscos do projeto em ordem de severidade com mitigações.
model: haiku
cost_estimate: "$0.001/run"
---

# Subagente: risk-summarizer

## Propósito
Coleta riscos de todas as fases do pipeline e gera resumo executivo com mitigações.

## Input
```json
{
  "risks_by_phase": {
    "discovery": [{"level": "R1", "desc": "Mercado pequeno"}],
    "architecture": [{"level": "R2", "desc": "Stack complexa"}]
  }
}
```

## Output
```json
{
  "summary": "Projeto tem 3 riscos: 1 R1, 1 R2, 1 R3",
  "top_risks": [
    {"level": "R3", "desc": "Dependencia API externa", "mitigation": "Cache + fallback"}
  ],
  "recommendation": "Proceder com mitigações documentadas"
}
```

## Quando despachar
- `app-factory-handoff` resume riscos antes de entregar

## Exemplo
```
Agent tool: risk-summarizer
Prompt: "Resuma riscos: R1 mercado pequeno, R2 stack complexa, R3 API externa"
```
