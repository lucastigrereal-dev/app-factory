---
name: app-factory-api-contractor
version: "1.0"
description: "Constrói contratos de API OpenAPI a partir de schemas e requisitos. Define rotas, parâmetros, respostas, erros."
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
depends_on: [app-factory-schema-designer]
next_skill: app-factory-frontend-planner
---

# Skill: app-factory-api-contractor

## Role
Input: Schema YAML + PRD + blueprint
Output: OpenAPI contract YAML + relatório de endpoints

## Input Contract
```json
{
  "schema_yaml": "artifacts/schema/schema.yaml",
  "prd_path": "artifacts/prd/output.md",
  "product_name": "hotel-delivery-natal"
}
```

## Output Contract
```json
{
  "api_contract_yaml": "artifacts/api/hotel-delivery-natal_api_contract.yaml",
  "report": "artifacts/api/api-report.md",
  "endpoints": [
    {"method": "GET", "path": "/api/users", "auth": true, "status_codes": [200, 401]},
    {"method": "POST", "path": "/api/orders", "auth": true, "status_codes": [201, 400, 401]}
  ],
  "version": "1.0.0",
  "auth_scheme": "JWT Bearer",
  "dry_run": true,
  "next_action": "Prosseguir para app-factory-frontend-planner"
}
```

## Execution
1. Parse schema -> identifica recursos
2. Cria endpoints REST (GET, POST, PUT, DELETE, PATCH)
3. Mapeia schema -> objetos JSON
4. Documenta códigos de status e erros
5. Define autenticação por endpoint
6. Valida conformidade OpenAPI 3.0
7. Gera YAML e relatório

## Guardrails
- Endpoint sem autenticação onde deveria = rejeitado
- Falta versionamento = rejeitado
- Resposta sem schema = rejeitado
- SEMPRE inclui 400/401/404/500 nos status codes

## Next Skill
→ app-factory-frontend-planner
