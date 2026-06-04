---
name: market-researcher
type: subagent
squad: product
description: Pesquisa concorrência e tendencias de mercado para uma ideia de produto.
model: haiku
cost_estimate: "$0.002/run"
---

# Subagente: market-researcher

## Propósito
Pesquisa concorrentes, tendências Google Trends, dados de mercado e gaps de oportunidade para validar uma ideia de produto.

## Input
```json
{
  "intention": "App de delivery para hotéis em Natal",
  "market": "turismo, hotelaria, food delivery",
  "geo": "Natal/RN, Brasil",
  "time_range": "12 meses"
}
```

## Output
```json
{
  "competitors": [
    {"name": "iFood", "market_share": "70%", "threat": "alta", "gap": "não atende hotéis"},
    {"name": "Rappi", "market_share": "20%", "threat": "media", "gap": "custo alto"}
  ],
  "trends": [
    {"keyword": "delivery hotel", "growth": "+15% YoY"},
    {"keyword": "room service app", "growth": "+8% YoY"}
  ],
  "market_size": "R$ 2M/ano estimado em Natal",
  "opportunity_gaps": ["hotel-only", "integracao PMS", "multilingue"],
  "confidence": 0.75
}
```

## Quando despachar
- Skill `app-factory-discovery` precisa validar mercado
- Usuário pede "analisar concorrência"

## Exemplo de uso
```
Agent tool: market-researcher
Prompt: "Pesquise concorrência para 'app de delivery para hotéis em Natal/RN'"
```
