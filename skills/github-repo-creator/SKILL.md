---
name: github-repo-creator
description: >-
  Cria repo GitHub via API, faz push do scaffold
model: sonnet
tools:
  - Read
  - Write
  - Bash
disallowedTools:
  - Bash(rm*)
  - Bash(git push*)
  - Bash(deploy*)
---

## Skill: github-repo-creator

### Objetivo
Cria repo GitHub via API, faz push do scaffold

### Input esperado
```json
{
  "intention": "string",
  "blueprint": {}
}
```

### Output esperado
```json
{
  "status": "success|not_implemented",
  "dry_run": true,
  "next_action": "string"
}
```

### Regras de seguranca
- Sempre operar em dry_run por padrao
- Nunca executar comandos destrutivos sem aprovacao R3
- Nunca expor secrets ou tokens

### Proxima evolucao
- Integrar com gateway LLM real
- Adicionar validacao de schema strict
- Implementar retry e circuit breaker
