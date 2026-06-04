---
name: problem-validator
type: subagent
squad: product
description: Valida se uma dor de usuário é real, frequente e paga.
model: haiku
cost_estimate: "$0.001/run"
---

# Subagente: problem-validator

## Propósito
Valida se o problema identificado é: (1) real, (2) frequente, (3) urgente, (4) paga por solução.

## Input
```json
{
  "problem_statement": "Hospedes querem pedir comida do quarto sem ligar na recepcao",
  "target_users": ["hospedes de hotel", "recepcionistas"],
  "alternatives": ["ligar recepcao", "iFood direto", "formulario papel"],
  "evidence": ["reviews mencionam demora", "recepcao sobrecarregada"]
}
```

## Output
```json
{
  "is_real": true,
  "is_frequent": true,
  "is_urgent": false,
  "pays_for_solution": true,
  "validation_score": 0.75,
  "evidence_strength": "media",
  "recommended_action": "proceder com MVP simples",
  "risks": ["urgencia baixa = adocao lenta"]
}
```

## Quando despachar
- `app-factory-discovery` valida dor antes de gerar PRD
- Go/no-go depende deste validador

## Exemplo
```
Agent tool: problem-validator
Prompt: "Valide se 'hospedes querem pedir comida do quarto sem ligar recepcao' é problema real"
```
