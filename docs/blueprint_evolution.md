# Blueprint Técnico — FactoryOS IA Evolução Exponencial

## Visão Geral da Arquitetura

O sistema será construído sobre uma arquitetura de múltiplos agentes coordenados via grafo de estados (LangGraph). Cada agente é responsável por uma etapa do ciclo de automação (descoberta, arquitetura, integração, construção, testes, documentação, deploy). A orquestração é assíncrona, utilizando um event bus baseado em Redis Streams, e a memória compartilhada é persistida em Supabase com extensão pgvector.

### Diagrama de Componentes (Mermaid)

```mermaid
flowchart TD
    subgraph Supervisão
        orchestrator[Supervisor (LangGraph)]
    end
    subgraph Workers
        discovery_agent[Discovery Agent]
        architecture_agent[Architecture Agent]
        integration_agent[Integration Agent]
        builder_agent[Builder Agent]
        security_agent[Security Agent]
        qa_agent[QA Agent]
        doc_agent[Documentation Agent]
        recovery_agent[Recovery Agent]
    end
    orchestrator --> discovery_agent
    discovery_agent --> architecture_agent
    architecture_agent --> integration_agent
    integration_agent --> builder_agent
    builder_agent --> qa_agent
    qa_agent --> doc_agent
    doc_agent --> orchestrator
    security_agent --> orchestrator
    recovery_agent --> orchestrator
    subgraph Infra
        redis[Redis Streams]
        supabase[Supabase DB + pgvector]
        n8n[n8n Execution Engine]
        langfuse[Langfuse]
    end
    orchestrator <--> redis
    workers --> redis
    workers --> supabase
    workers --> n8n
    orchestrator --> langfuse
```

### Camadas Principais

- **Orquestração:** Grafo de estados definindo a sequência de execução dos agentes e as condições de branching. Implementado com `langgraph.StateGraph`.
- **Event Bus:** Baseado em Redis Streams. Cada evento (ex.: `discovery.completed`, `schema.generated`) dispara handlers em agentes subscritos. Permite escalabilidade horizontal e isolação por organização.
- **Memory Layer:** Camada de memória com três níveis:
  - Working memory: Redis, TTL de 24 h.
  - Episodic/Semantic: Tabela `factory_memory` no Supabase, com campo vetorial (1536D) para busca de casos similares via pgvector.
  - Procedural: Templates n8n versionados, armazenados em `supabase.storage`.
- **Self‑Healing:** Módulos implementando circuit breaker, retry exponencial e fila de mensagens para erros definitivos (Dead Letter Queue). O Recovery Agent analisa casos e propõe correção.
- **Security:** Políticas RLS no Supabase, encriptação de PII, e gate de aprovação humana para ações críticas. Agente de segurança executa checklists (OWASP Top 10) antes de permitir execuções.
- **Observabilidade:** Instrumentação via Langfuse e OpenTelemetry para cada agente e etapa, capturando tokens consumidos, latência e custos.
- **Pipeline de Geração:** Use `scaffold_plan_schema.json` para simular a criação de arquivos (dry‑run) e gerar diff antes de executar. Todos os scaffolds são versionados e necessitam aprovação.

## Componentes Detalhados

### Discovery Agent
Responsável por interagir com o usuário final via chat para coletar informações da empresa. Utiliza prompts dirigidos, valida coerência das respostas e produz um objeto `DiscoveryResult` que inclui oportunidades priorizadas. Este resultado gera eventos `discovery.oportunidades.identificadas` e `discovery.completed`.

### Architecture Agent
Recebe o `DiscoveryResult` e monta blueprint técnico: descreve fluxos de dados, identifica entidades e relacionamentos, propõe schema de banco (quando aplicável), define contratos de API preliminares e recomenda stack. Usa modelos `gpt‑4o` para raciocínio profundo e `gpt‑4o‑mini` para tarefas rápidas.

### Integration Agent
Analisa ferramentas citadas no discovery e define conectores apropriados (ex.: WhatsApp via Z‑API, Omie ERP, RD Station). Cria `integration_map.yaml` com endpoints, métodos de autenticação, limites de taxa e riscos. Aciona o Security Agent para revisão de credenciais e permissões.

### Builder Agent
Gera workflows n8n (JSON) a partir de templates e specs. Preenche parâmetros com base no `integration_map.yaml` e `blueprint`. Gera `workflow.plan.json` (dry‑run) e submete ao `Scaffold Plan Gate` para aprovação antes de ativar. Publica eventos `workflow.generated`.

### Security Agent
Avaliador de riscos. Executa checklist OWASP, identifica exposição de PII, valida RLS, revisa tokens e credenciais. Pode bloquear etapas subsequentes até correções. Produz relatório `security_review.md`.

### QA Agent
Gera plano de testes e scripts automatizados (pytest/Playwright) com base nos critérios de aceite do PRD e no blueprint. Executa testes em ambiente de staging, publica métricas de cobertura e reporte de falhas. Decide se a execução pode avançar.

### Documentation Agent
Consolida artefatos gerados (PRD, blueprint, schema, contracts, workflows) em relatório de handoff estruturado (`handoff_report.json`). Atualiza memória Akasha com decisões e resultados.

### Recovery Agent
Analisa falhas definitivas (DLQ) e consulta casos semelhantes na memória para sugerir correções. Classifica erros como transitórios, de configuração ou críticos e atua conforme recomendação (retry, alteração de config, alerta humano).

## Tarefas Críticas no Blueprint

| Módulo                | Ferramenta             | Descrição                                      |
|-----------------------|------------------------|------------------------------------------------|
| Orquestração          | LangGraph              | Definir fluxos, transições e callbacks         |
| Event Bus             | Redis Streams          | Criar tópicos por organização e evento         |
| Memória               | Supabase + pgvector    | Implementar tabelas de memória com embeddings  |
| Discovery Interface   | Frontend/Next.js       | UI conversacional e exibição de progresso      |
| Builder Workflow      | n8n                    | Criar templates e mapear passos automáticos    |
| Self‑Healing          | Python                 | Implementar circuit breaker + retry + DLQ      |
| Approvals             | Frontend + Supabase    | Interface para aprovar ou rejeitar ações       |
| Observability         | Langfuse               | Instrumentar agentes e funções de pipeline     |

## Stack Tecnológica

| Camada            | Tecnologia                                            |
|-------------------|-------------------------------------------------------|
| Frontend          | Next.js 14 (App Router) + TypeScript + Tailwind/shadcn |
| Orquestração      | LangGraph + Python 3.12                                |
| Back‑end API      | FastAPI (Python)                                       |
| DB                | Supabase (PostgreSQL + pgvector)                       |
| Queue/Event Bus   | Redis Streams                                          |
| Workflows         | n8n self‑hosted                                        |
| Observabilidade   | Langfuse + OpenTelemetry + Sentry                      |
| Agents Execution  | Claude 3.5 Sonnet/GPT‑4o via LiteLLM                   |

## Estimativa de Complexidade

| Componente             | Esforço (semana-homens) | Dependências Principais            |
|------------------------|-------------------------|------------------------------------|
| Base monorepo          | 1                       | Estrutura de pastas e pacotes       |
| Orquestração LangGraph | 2                       | StateGraph e handlers de eventos    |
| Sistema de memória     | 2                       | Migrações pgvector, embeddings      |
| Event bus              | 1                       | Configuração de Redis Streams       |
| Discovery conversacional| 2                      | Interface + LLMs                    |
| Blueprints/API/schema  | 2                       | Agents + módulos de validação      |
| Geração de workflows   | 2                       | Templates n8n + builder de JSON     |
| Self‑healing           | 2                       | Circuit breaker + retry + DLQ       |
| Painel de resultados   | 1                       | Dashboards + gráficos               |

Estes valores são aproximados e consideram equipe familiarizada com Python, Next.js e n8n.

## Considerações de Segurança

1. **Proteção de Dados:** Campo de informações pessoais (PII) devem ser encriptados no banco. RLS garante isolamento entre organizações.
2. **Segredos:** Não armazenar tokens de API no repositório; uso de vault seguro (Doppler/Infisical). O `no-secret-sentinel` deve bloquear qualquer commit que contenha secrets.
3. **Permissões de Agente:** Cada agente opera com escopo limitado e só pode acessar ferramentas explicitamente permitidas. Ações críticas exigem gate humano.
4. **Auditoria:** Todas as ações devem gerar log imutável para compliance.

## Próximas Etapas

1. **Aprovação do PRD e Blueprint** por Lucas Tigre (Product Owner).\
2. **Criação do Orquestrador** (LangGraph) e agentes base conforme blueprint.\
3. **Implementação do Event Bus** e memória pgvector.\
4. **Desenvolvimento da Interface Conversacional** e mapeamento inicial de oportunidades.\
5. **Construção de Templates** e scaffolds n8n, seguidos de testes de integração.\
6. **Instrumentação de Observabilidade** para captura de métricas e custos.

O blueprint deve ser revisto em ciclos semanais após feedback de implementações iniciais e testes em clientes piloto.