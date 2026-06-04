---
name: app-factory-discovery
version: "1.0"
description: "Valida se a ideia é problema real antes de gerar PRD. Busca contexto Akasha + trends + competição."
wave: wave_2_core
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: produto
status: active
risk: low
model: sonnet
cost_estimate: "$0.005/run"
depends_on: [app-intake]
next_skill: prd-generator
---

# Skill: app-factory-discovery

## Role
Input: intenção do usuário + contexto de mercado
Output: go/no-go com confiança, competidores, riscos, alternativas

## Input Contract
```json
{
  "intention": "Criar um app de delivery para hotéis em Natal",
  "market_context": "Natal/RN, turismo, 6 meses de alta temporada",
  "budget": "R$2000",
  "timeline": "2 semanas",
  "target_users": ["hóspedes de hotel", "recepcionistas"]
}
```

## Output Contract
```json
{
  "go": true,
  "confidence": 0.82,
  "problem_statement": "Hóspedes querem pedir comida do quarto sem ligar na recepção",
  "competitors": [
    {"name": "iFood", "threat": "alta", "differentiator": "hotel-only"},
    {"name": "WhatsApp manual", "threat": "média", "differentiator": "app estruturado"}
  ],
  "risks": [
    {"level": "R1", "description": "Baixo budget limita funcionalidades"},
    {"level": "R2", "description": "Integração com restaurantes locais é manual"}
  ],
  "alternatives": [
    "Usar formulário Google + WhatsApp (R$0)",
    "Integrar com iFood Business (R$500/mês)"
  ],
  "next_action": "Prosseguir para prd-generator"
}
```

## Execution
1. Parse intenção → extrai dor + usuário + mercado
2. Busca Akasha por contexto similar (hotéis, delivery, turismo)
3. Analisa competição: Google + Akasha knowledge
4. Valida dor: a dor é frequente? é urgente? pagam por isso?
5. Gera go/no-go + confiança
6. Se go=false: sugere alternativas mais baratas/rápidas

## Guardrails
- Sem dados de mercado = confiança máxima 0.5
- Ideia sem dor clara = no-go obrigatório
- Budget < R$500 + timeline < 1 semana = sugerir no-code primeiro
- SEMPRE retorna alternativas, mesmo no go

## Next Skill
→ prd-generator (se go=true)
→ retorna ao usuário com alternativas (se go=false)
