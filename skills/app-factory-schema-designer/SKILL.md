---
name: app-factory-schema-designer
version: "1.0"
description: "Planeja e valida schemas de banco de dados. Deriva entidades, atributos, relações e gera YAML + SQL migrations."
wave: wave_3_agents
author: Tigrão
installed_at: 2026-06-04
project: app_factory
sector: produto_tecnologia
type: arquitetura
status: active
risk: low
model: sonnet
cost_estimate: "$0.004/run"
depends_on: [blueprint-generator, app-factory-stack-decider]
next_skill: app-factory-api-contractor
---

# Skill: app-factory-schema-designer

## Role
Input: PRD + blueprint + stack decision
Output: Schema YAML + SQL migrations + relatório de decisões

## Input Contract
```json
{
  "prd_path": "artifacts/prd/output.md",
  "blueprint_path": "artifacts/blueprint/output.md",
  "stack": {"database": "PostgreSQL"},
  "product_name": "hotel-delivery-natal"
}
```

## Output Contract
```json
{
  "schema_yaml": "artifacts/schema/hotel-delivery-natal_schema.yaml",
  "migrations_sql": "artifacts/schema/migrations/",
  "report": "artifacts/schema/schema-report.md",
  "entities": [
    {"name": "users", "fields": ["id", "email", "role"], "relations": ["orders"]},
    {"name": "orders", "fields": ["id", "user_id", "status", "total"], "relations": ["users", "items"]}
  ],
  "normalization": "3NF",
  "sensitive_fields": ["email", "phone"],
  "dry_run": true,
  "next_action": "Prosseguir para app-factory-api-contractor"
}
```

## Execution
1. Parse PRD e blueprint -> identifica entidades de domínio
2. Define chaves primárias, foreign keys, índices
3. Normaliza até 3NF
4. Marca campos sensíveis
5. Gera YAML de schema
6. Gera SQL migrations (up/down)
7. Valida contra docs/DB_SCHEMA.md

## Guardrails
- Sem normalização = rejeitado
- Campos sensíveis sem proteção = rejeitado
- Schema conflitante com segurança = rejeitado
- SEMPRE gera migrations up + down

## Next Skill
→ app-factory-api-contractor
