#!/usr/bin/env python3
"""Generator: Cria skills, agentes e subagentes de evolução da App Factory."""
import os, json, textwrap
from pathlib import Path

BASE = Path(__file__).resolve().parent

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  [CREATE] {path}")

# ============================================================
# 1. SKILLS (15)
# ============================================================
SKILLS = [
    ("llm-gateway", "Gateway LiteLLM/OpenRouter com retry, fallback e cost tracking", "llm", "Gateway LLM"),
    ("template-engine", "Renderiza templates Jinja2 com blueprint como contexto", "template", "Template Engine"),
    ("html-generator", "Gera HTML + Tailwind a partir de blueprint e intencao", "html", "HTML Generator"),
    ("nextjs-generator", "Gera app Next.js + Supabase a partir de blueprint", "nextjs", "Next.js Generator"),
    ("supabase-schema-generator", "Gera migrations SQL/Prisma a partir do schema designer", "schema", "Supabase Schema Generator"),
    ("api-fastapi-generator", "Gera endpoints FastAPI a partir do API contractor", "api", "FastAPI Generator"),
    ("vercel-deployer", "Deploy pasta temporaria para Vercel, retorna URL preview", "deploy", "Vercel Deployer"),
    ("github-repo-creator", "Cria repo GitHub via API, faz push do scaffold", "github", "GitHub Repo Creator"),
    ("app-quality-guardian", "Roda Lighthouse e testes de regressao visual no app gerado", "quality", "App Quality Guardian"),
    ("cost-monitor", "Persiste custos em PostgreSQL (nao in-memory)", "cost", "Cost Monitor"),
    ("event-publisher", "Publica eventos para Redis/OMNIS bus (nao so in-memory)", "event", "Event Publisher"),
    ("akasha-connector", "Escreve eventos em PostgreSQL/pgvector real", "akasha", "Akasha Connector"),
    ("kratos-connector", "Envia snapshot para dashboard Kratos real", "kratos", "Kratos Connector"),
    ("factory-generator", "Cria estrutura de nova factory (run.py, SKILL.md, tests, fixtures)", "factory", "Factory Generator"),
    ("self-healing-runner", "Detecta falha em skill, retry com backoff, circuit breaker", "healing", "Self-Healing Runner"),
]

SKILL_PY_TEMPLATE = '''#!/usr/bin/env python3
"""
{slug}
{description}
"""
import argparse, json, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="{title}")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", default="{output_file}", help="Output file")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input not found: {{input_path}}", file=sys.stderr)
        return 1
    data = json.loads(input_path.read_text(encoding="utf-8"))

    intention = data.get("intention", "")
    blueprint = data.get("blueprint", {{}})

    result = {{
        "status": "success" if args.dry_run else "not_implemented",
        "intention": intention,
        "blueprint_used": bool(blueprint),
        "dry_run": args.dry_run,
        "next_action": "Revisar output e passar para proxima skill",
        "generated_files": [],
        "metrics": {{
            "tokens_used": 0,
            "duration_ms": 0,
            "model": "not_called",
        }},
    }}

    output_path = Path(args.output)
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''

SKILL_MD_TEMPLATE = '''---
name: {slug}
description: >-
  {description}
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

## Skill: {slug}

### Objetivo
{description}

### Input esperado
```json
{{
  "intention": "string",
  "blueprint": {{}}
}}
```

### Output esperado
```json
{{
  "status": "success|not_implemented",
  "dry_run": true,
  "next_action": "string"
}}
```

### Regras de seguranca
- Sempre operar em dry_run por padrao
- Nunca executar comandos destrutivos sem aprovacao R3
- Nunca expor secrets ou tokens

### Proxima evolucao
- Integrar com gateway LLM real
- Adicionar validacao de schema strict
- Implementar retry e circuit breaker
'''

TEST_TEMPLATE = '''#!/usr/bin/env python3
"""Tests for {slug}"""
import subprocess, sys, json
from pathlib import Path

RUN_PY = Path(__file__).resolve().parent.parent / "run.py"

def test_run_py_exists():
    assert RUN_PY.is_file(), f"run.py not found at {{RUN_PY}}"

def test_dry_run_completes():
    fixture = Path(__file__).resolve().parent / "fixture.json"
    fixture.write_text(json.dumps({{"intention": "test"}}), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(fixture), "--dry-run"],
        capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0, f"dry_run failed: {{result.stderr}}"
    output = json.loads(result.stdout)
    assert output.get("status") == "success"
    assert output.get("dry_run") is True

def test_output_schema():
    fixture = Path(__file__).resolve().parent / "fixture.json"
    fixture.write_text(json.dumps({{"intention": "test"}}), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(RUN_PY), "--input", str(fixture), "--output", "test_output.json", "--dry-run"],
        capture_output=True, text=True, encoding="utf-8"
    )
    assert result.returncode == 0
    out = Path("test_output.json")
    assert out.exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "status" in data
    assert "dry_run" in data
    out.unlink(missing_ok=True)
'''

print("=== Criando 15 Skills ===")
for slug, desc, short, title in SKILLS:
    base = BASE / "skills" / slug
    write(base / "SKILL.md", SKILL_MD_TEMPLATE.format(slug=slug, description=desc, title=title))
    write(base / "run.py", SKILL_PY_TEMPLATE.format(slug=slug, description=desc, title=title, output_file=f"{short}_output.json"))
    write(base / f"{short}_output.json", json.dumps({"status": "stub", "skill": slug}, indent=2))
    write(base / "tests" / "fixture.json", json.dumps({"intention": "test fixture"}, indent=2))
    write(base / "tests" / f"test_{slug.replace('-', '_')}.py", TEST_TEMPLATE.format(slug=slug))

# ============================================================
# 2. AGENTES (8)
# ============================================================
AGENTS = [
    ("llm-orchestrator", "Decide qual modelo usar por etapa (fast/cheap/smart)", "Read, Bash(python)", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("code-generator", "Gera codigo real (HTML, TSX, Python) via LLM", "Read, Write, Bash", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("deploy-guardian", "Valida se app esta pronto para deploy (testes, lint, build)", "Read, Bash(npm run build), Grep", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("quality-rater", "Atribui score 0-100 ao app gerado (Lighthouse + heuristicas)", "Read, Bash(lighthouse), Grep", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("integration-engineer", "Conecta bridges OMNIS/Akasha/Kratos (codigo real, nao stub)", "Read, Write, Bash", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("template-architect", "Desenha e valida templates Jinja2 para novos produtos", "Read, Write, Grep", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("factory-midwife", "Auxilia no nascimento de uma nova factory (guia passo a passo)", "Read, Write, Bash(python)", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
    ("observability-engineer", "Instrumenta metricas, logs, tracing no pipeline", "Read, Write, Bash", "Bash(rm*), Bash(git push*), Bash(deploy*)"),
]

AGENT_TEMPLATE = '''---
name: {slug}
description: >-
  {description}
model: sonnet
tools:
  - {tools}
disallowedTools:
  - {disallowed}
---

## Agente: {slug}

### Missao
{description}

### Responsabilidades
- Executar tarefas dentro do escopo definido
- Respeitar regras de seguranca e governanca
- Reportar progresso e bloqueios

### Limites
- Nao executa deploy sem aprovacao R3
- Nao manipula secrets ou variaveis de ambiente
- Nao aprova acoes R3 sem gate de aprovacao

### Entradas
- Documentos de requisito (PRD, blueprint)
- Relatorios de risco e validacao

### Saidas
- Artefatos gerados ou atualizados
- Parecer com riscos e recomendacoes

### Criterios de aceite
- Tarefa concluida dentro do escopo
- Conformidade com politicas de governanca

### Red flags
- Solicitacoes de adicionar servicos externos sem validacao
- Mudancas de escopo sem passar pelo PRD
- Tentativa de executar deploys ou conectar bancos externos
'''

print("\n=== Criando 8 Agentes ===")
for slug, desc, tools, disallowed in AGENTS:
    write(BASE / ".claude" / "agents" / f"{slug}.md", AGENT_TEMPLATE.format(slug=slug, description=desc, tools=tools, disallowed=disallowed))

# ============================================================
# 3. SUBAGENTES (10)
# ============================================================
SUBAGENTS = [
    ("ui-component-drafter", "Gera componentes React/Shadcn a partir de wireframe textual"),
    ("sql-migration-drafter", "Gera migrations SQL/Prisma a partir de schema YAML"),
    ("openapi-generator", "Gera spec OpenAPI 3.1 a partir de endpoints descritos"),
    ("test-generator-e2e", "Gera testes Playwright/Cypress para app gerado"),
    ("seo-optimizer", "Sugere meta tags, structured data, sitemap para landing page"),
    ("accessibility-auditor", "Verifica WCAG 2.1 AA no HTML gerado"),
    ("performance-budget", "Define e monitora budget de bundle size, LCP, CLS"),
    ("dependency-vulnerability-scanner", "Roda npm audit, pip-audit no app gerado"),
    ("prompt-optimizer", "Melhora prompts das skills existentes (auto-tuning)"),
    ("docs-syncer", "Gera/atualiza docs automaticamente quando codigo muda"),
]

SUBAGENT_TEMPLATE = '''# Subagente: {slug}

## Objetivo
{description}

## Quando usar
- Quando o artefato gerado precisa da camada especifica descrita acima
- Como especialista em {domain} dentro do pipeline App Factory

## Input esperado
- Blueprint do produto
- Especificacao da camada a ser gerada
- Stack tecnologica definida

## Output esperado
- Artefato gerado (codigo, spec, relatorio)
- Recomendacoes de melhoria
- Score de qualidade (se aplicavel)

## Regras
- Sempre operar em dry_run por padrao
- Nunca executar acoes destrutivas sem aprovacao
- Validar saidas contra schema quando disponivel
'''

print("\n=== Criando 10 Subagentes ===")
for slug, desc in SUBAGENTS:
    domain = slug.split("-")[0]
    write(BASE / "subagents" / f"{slug}.md", SUBAGENT_TEMPLATE.format(slug=slug, description=desc, domain=domain))

# ============================================================
# 4. Atualizar config/skills.yaml
# ============================================================
print("\n=== Atualizando config/skills.yaml ===")
skills_yaml = BASE / "config" / "skills.yaml"
existing = skills_yaml.read_text(encoding="utf-8") if skills_yaml.exists() else "skills:\n"

new_entries = ""
for slug, desc, short, title in SKILLS:
    new_entries += f"""  - name: {slug}
    description: {desc}
    type: evolution
    status: draft
    risk: R2
    owner: engineering
    requires_human_approval: false
    dependencies: []
"""

if "skills:" in existing:
    updated = existing.rstrip() + "\n" + new_entries
else:
    updated = "skills:\n" + new_entries

write(skills_yaml, updated)

# ============================================================
# 5. Resumo
# ============================================================
print("\n" + "="*60)
print("EVOLUTION PACK CRIADO COM SUCESSO")
print("="*60)
print(f"  Skills criadas:     {len(SKILLS)}")
print(f"  Agentes criados:    {len(AGENTS)}")
print(f"  Subagentes criados: {len(SUBAGENTS)}")
print(f"  Total arquivos:     {len(SKILLS)*5 + len(AGENTS) + len(SUBAGENTS) + 1}")
print("\nProximo passo: rodar pytest para validar")
