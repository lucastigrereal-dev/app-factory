---
name: db-migrator
type: subagent
squad: engineering
description: Gera SQL migrations up/down a partir de schema YAML.
model: haiku
cost_estimate: "$0.002/run"
---

# Subagente: db-migrator

## Propósito
Gera arquivos SQL de migração (up e down) baseado no schema YAML.

## Input
```json
{
  "schema_yaml": "artifacts/schema/schema.yaml",
  "dialect": "postgresql",
  "migration_name": "create_orders_and_users"
}
```

## Output
```json
{
  "up_migration": "... SQL CREATE TABLE ...",
  "down_migration": "... SQL DROP TABLE ...",
  "files": [
    {"path": "migrations/001_create_orders_and_users.up.sql", "content": "..."},
    {"path": "migrations/001_create_orders_and_users.down.sql", "content": "..."}
  ]
}
```

## Quando despachar
- `app-factory-schema-designer` gera migrations após schema validado

## Exemplo
```
Agent tool: db-migrator
Prompt: "Gere migration PostgreSQL para schema de delivery com users, orders, items"
```
