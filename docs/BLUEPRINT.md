Tigrão, **postura de guerra**: coluna ereta, respiração baixa, e vamos construir isso como gente grande. 🐅⚙️

Aqui vai o **Blueprint Técnico Completo V1.0 da FactoryOS IA**, como eu desenharia sendo tua dev sênior especialista em integrações, automação, IA e produto B2B.

A base funcional vem do cockpit que consolidamos: diagnóstico, processos, rotinas, ferramentas, integrações, agentes de IA, n8n, ROI, backlog, documentação, monitoramento e governança. 

---

# BLUEPRINT TÉCNICO V1.0

# **FactoryOS IA**

## Cockpit da Fábrica de Automação Empresarial com IA

## 1. Decisão brutal de arquitetura

A FactoryOS IA **não começa como microserviços**.

Microserviço agora seria você querendo montar uma usina nuclear para esquentar pão de queijo. Bonito no LinkedIn, desastre na vida real.

## Arquitetura correta para V1

# **Modular Monolith + Integration Runtime**

Ou seja:

* um app web principal;
* um banco central;
* módulos bem separados internamente;
* n8n como motor de workflows;
* IA como camada cognitiva;
* filas para tarefas pesadas;
* logs e auditoria desde o primeiro dia;
* conectores plugáveis por ferramenta.

## Por quê?

Porque a FactoryOS precisa primeiro provar:

1. diagnóstico;
2. priorização;
3. ROI;
4. backlog;
5. documentação;
6. execução assistida;
7. automação real.

Depois escala.
Primeiro o bisturi. Depois o hospital. 🧠

---

# 2. Visão técnica em uma frase

> **A FactoryOS IA é uma aplicação SaaS B2B multiempresa que mapeia processos, classifica rotinas, prioriza automações, cria agentes de IA, registra integrações, orquestra workflows via n8n/API/webhooks, mede ROI e mantém governança, logs e documentação de ponta a ponta.**

---

# 3. Stack recomendado

## Stack MVP

| Camada             | Ferramenta recomendada                      | Função                            |
| ------------------ | ------------------------------------------- | --------------------------------- |
| Frontend           | Next.js + React + TypeScript                | App web                           |
| UI                 | Tailwind + shadcn/ui                        | Interface enterprise rápida       |
| Backend            | Next.js API Routes / Server Actions         | API inicial                       |
| Banco              | Supabase/PostgreSQL                         | Dados principais                  |
| Auth               | Supabase Auth ou Clerk                      | Login e organizações              |
| Segurança de dados | RLS no Postgres                             | Isolamento multiempresa           |
| Orquestração       | n8n                                         | Workflows, webhooks e integrações |
| IA                 | OpenAI + Claude + Gemini via provider layer | Agentes e análises                |
| Observabilidade IA | Langfuse                                    | Traces, prompts e avaliações      |
| Filas              | Redis + BullMQ, ou Supabase Queue depois    | Jobs assíncronos                  |
| BI inicial         | Metabase / Looker Studio                    | Dashboards                        |
| Arquivos           | Supabase Storage / Google Drive             | Documentos                        |
| Deploy MVP         | Vercel + Supabase + n8n Cloud/self-host     | Rapidez                           |
| Deploy controlado  | Coolify + Docker + VPS                      | Controle e margem                 |

Supabase com Postgres e Row Level Security faz sentido para SaaS multiempresa porque RLS permite regras granulares no banco, e a própria documentação recomenda habilitar RLS em tabelas expostas no schema público. ([Supabase][1])

n8n faz sentido como motor externo porque sua API pública permite interagir programaticamente com a plataforma por HTTP e executar tarefas que normalmente seriam feitas pela interface. ([n8n Docs][2])

Para IA com ações estruturadas, Function Calling conecta modelos a ferramentas e sistemas externos, e Structured Outputs com `strict: true` garante que os argumentos sigam o JSON Schema definido. ([OpenAI Help Center][3])

Para prompts, rastreio e qualidade, Langfuse permite versionar prompts fora do código e relacionar prompts com traces, métricas e avaliações. ([Langfuse][4])

---

# 4. Diagrama macro da arquitetura

```text
┌────────────────────────────────────────────────────────────┐
│                    FactoryOS IA Web App                    │
│           Next.js + React + TypeScript + Tailwind          │
└────────────────────────────┬───────────────────────────────┘
                             │
                             ▼
┌────────────────────────────────────────────────────────────┐
│                     Application Core                       │
│ Empresas | Diagnóstico | Rotinas | Processos | Backlog     │
│ Integrações | Agentes | Workflows | ROI | Docs | Logs      │
└───────────────┬──────────────────────┬─────────────────────┘
                │                      │
                ▼                      ▼
┌──────────────────────────┐   ┌─────────────────────────────┐
│ Supabase/PostgreSQL      │   │ AI Provider Layer            │
│ Dados, RLS, logs, ROI    │   │ OpenAI, Claude, Gemini       │
│ pgvector, documentos     │   │ Structured outputs, tools    │
└───────────────┬──────────┘   └──────────────┬──────────────┘
                │                             │
                ▼                             ▼
┌──────────────────────────┐   ┌─────────────────────────────┐
│ Queue/Workers            │   │ Langfuse                    │
│ jobs, relatórios, sync   │   │ prompts, traces, evals      │
└───────────────┬──────────┘   └─────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                         n8n Runtime                         │
│ Workflows | Webhooks | APIs | Transformações | Integrações  │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│             Ferramentas externas dos clientes               │
│ Google | RD | HubSpot | Bitrix24 | WhatsApp | ERP | CRM     │
│ ClickUp | Notion | Omie | Bling | Conta Azul | BI | etc.    │
└────────────────────────────────────────────────────────────┘
```

---

# 5. Camadas da FactoryOS IA

## 5.1 Camada 1: Interface

Responsável por:

* cockpit;
* diagnóstico;
* processos;
* rotinas;
* ferramentas;
* integrações;
* agentes;
* workflows;
* ROI;
* backlog;
* documentação;
* governança;
* monitoramento.

## 5.2 Camada 2: Domínio de produto

Regras internas:

* cálculo de score;
* maturidade operacional;
* priorização;
* ciclo da automação;
* aprovação humana;
* governança de IA;
* criação de relatórios;
* classificação de risco.

## 5.3 Camada 3: Dados

Responsável por:

* empresas;
* usuários;
* setores;
* ferramentas;
* rotinas;
* processos;
* workflows;
* logs;
* ROI;
* documentos;
* agentes;
* prompts;
* integrações;
* incidentes.

## 5.4 Camada 4: Integrações

Responsável por:

* APIs;
* webhooks;
* n8n;
* polling;
* import/export;
* Google;
* CRM;
* ERP;
* WhatsApp;
* BI;
* ferramentas internas.

## 5.5 Camada 5: IA

Responsável por:

* resumo;
* classificação;
* sugestão;
* geração;
* auditoria;
* extração;
* criação de SOP;
* geração de relatórios;
* agentes por setor;
* análise de logs.

## 5.6 Camada 6: Governança

Responsável por:

* permissões;
* logs;
* auditoria;
* aprovação;
* limites de agente;
* dados sensíveis;
* segurança de credenciais;
* trilha de decisão.

---

# 6. Módulos técnicos

## 6.1 Empresas

Entidade central do sistema.

```text
Company
├── Departments
├── Tools
├── Processes
├── Routines
├── Integrations
├── Workflows
├── Agents
├── Documents
├── Backlog
├── ROI
└── Logs
```

### Funções

* criar cliente;
* definir segmento;
* definir maturidade;
* associar responsáveis;
* selecionar plano;
* acompanhar status;
* ver economia estimada.

---

## 6.2 Diagnóstico

O diagnóstico é o motor comercial do produto.

### Fluxo

```text
Criar empresa
↓
Escolher setores
↓
Cadastrar ferramentas
↓
Mapear processos
↓
Levantar rotinas
↓
Identificar gargalos
↓
Calcular score
↓
Gerar relatório
↓
Gerar backlog
```

### Entradas

* formulário;
* entrevista;
* upload de documento;
* resposta manual;
* importação de planilha;
* reunião transcrita;
* observação operacional.

### Saídas

* relatório executivo;
* rotinas automatizáveis;
* matriz de prioridade;
* roadmap;
* backlog;
* estimativa de ROI.

---

## 6.3 Processos

Cada processo tem 3 versões:

```text
AS IS          Como funciona hoje
TO BE          Como deveria funcionar
AUTOMATIZADO   Como será com IA, n8n e integrações
```

### Estrutura técnica

```json
{
  "process_id": "proc_001",
  "company_id": "company_001",
  "name": "Cobrança de inadimplentes",
  "department_id": "dept_financeiro",
  "status": "mapped",
  "versions": [
    {
      "type": "AS_IS",
      "steps": []
    },
    {
      "type": "TO_BE",
      "steps": []
    },
    {
      "type": "AUTOMATED",
      "steps": []
    }
  ]
}
```

---

## 6.4 Rotinas

Rotina é o átomo do produto.

A FactoryOS não vende “integração”.
Ela vende **rotina automatizada com ROI**.

### Campos principais

```text
nome
setor
frequência
tempo por execução
volume mensal
ferramentas usadas
erro comum
risco
potencial de automação
potencial de IA
economia estimada
score
prioridade
status
```

### Status

```text
identified
under_analysis
automatable
do_not_automate_yet
designing
implementing
testing
active
monitoring
needs_review
```

---

## 6.5 Ferramentas

A FactoryOS precisa ter um catálogo interno de ferramentas.

### Categorias

```text
crm
erp
finance
marketing
support
google_workspace
project_management
documents
bi
database
ai
communication
signature
hr
legal
ecommerce
devinfra
security
```

### Tool Registry

```json
{
  "tool_id": "hubspot",
  "name": "HubSpot",
  "category": "crm",
  "has_api": true,
  "has_webhook": true,
  "auth_methods": ["oauth2", "private_app_token"],
  "objects": ["contact", "company", "deal", "ticket"],
  "integration_level": "high"
}
```

### Client Tool Instance

```json
{
  "id": "client_tool_001",
  "company_id": "company_001",
  "tool_id": "hubspot",
  "status": "active",
  "criticality": "high",
  "owner_department": "commercial",
  "credential_reference_id": "cred_001"
}
```

---

## 6.6 Integrações

Integração é sempre registrada como contrato técnico.

### Modelo mental

```text
Origem
↓
Evento/Gatilho
↓
Transformação
↓
IA opcional
↓
Destino
↓
Log
↓
Fallback
```

### Exemplo

```text
RD Station
↓ novo lead qualificado
n8n
↓ normaliza payload
IA
↓ classifica intenção
HubSpot
↓ cria contato e negócio
ClickUp
↓ cria tarefa para vendedor
Dashboard
↓ atualiza métrica
```

### Campos da integração

```json
{
  "id": "int_001",
  "company_id": "company_001",
  "name": "RD Station para HubSpot",
  "source_tool_id": "rd_station",
  "target_tool_id": "hubspot",
  "trigger_type": "webhook",
  "trigger_event": "new_qualified_lead",
  "action": "create_contact_and_deal",
  "middleware": "n8n",
  "requires_ai": true,
  "requires_human_approval": false,
  "risk_level": "low",
  "status": "mapped"
}
```

### Tipos de integração

```text
api
webhook
database
csv_import
csv_export
google_sheets
email_parser
rpa
native_connector
n8n_node
custom_script
manual_assisted
```

---

## 6.7 Agentes de IA

Agente não é “promptzão”.
Agente é função com escopo, dados, ferramentas e limite.

### Estrutura

```text
Agente
├── Objetivo
├── Dados permitidos
├── Ferramentas permitidas
├── Ações permitidas
├── Ações proibidas
├── Prompt versionado
├── Modelo
├── Saída estruturada
├── Aprovação humana
├── Logs
└── Avaliação
```

### Exemplo de agente financeiro

```json
{
  "id": "agent_financeiro_001",
  "name": "Agente Financeiro",
  "company_id": "company_001",
  "department_id": "financeiro",
  "allowed_data": [
    "customer_name",
    "invoice_status",
    "due_date",
    "amount",
    "payment_link"
  ],
  "allowed_actions": [
    "generate_collection_message",
    "summarize_overdue_invoices",
    "classify_payment_risk"
  ],
  "forbidden_actions": [
    "approve_payment",
    "delete_invoice",
    "send_message_without_approval"
  ],
  "autonomy_level": 2,
  "requires_human_approval": true
}
```

### Níveis de autonomia

| Nível | Nome                   | Permissão                           |
| ----: | ---------------------- | ----------------------------------- |
|     0 | Leitura                | Só lê e resume                      |
|     1 | Sugestão               | Sugere próxima ação                 |
|     2 | Rascunho               | Gera texto/documento                |
|     3 | Execução com aprovação | Executa após humano aprovar         |
|     4 | Execução limitada      | Executa baixo risco                 |
|     5 | Autonomia avançada     | Apenas futuro, com governança forte |

A camada de agentes precisa ser conservadora porque agentes com ferramentas aumentam superfície de ataque. A OWASP GenAI Security Project mantém uma lista de riscos para aplicações LLM, e o documento 2025 existe justamente para orientar segurança em aplicações que incorporam LLMs em operações reais. ([OWASP Gen AI Security Project][5])

---

# 7. Arquitetura de IA

## 7.1 AI Provider Layer

Nunca chame OpenAI, Claude ou Gemini direto espalhado no código.
Cria uma camada única:

```text
/app/ai
├── providers/
│   ├── openai.ts
│   ├── anthropic.ts
│   ├── gemini.ts
│   └── router.ts
├── schemas/
├── prompts/
├── evaluators/
├── tools/
└── agents/
```

## 7.2 Interface padrão

```ts
type AIProvider = "openai" | "anthropic" | "gemini" | "local";

type AIRequest<TSchema> = {
  provider?: AIProvider;
  task: string;
  systemPrompt: string;
  userInput: string;
  schema?: TSchema;
  temperature?: number;
  metadata: {
    companyId: string;
    userId: string;
    module: string;
    entityId?: string;
  };
};

type AIResponse<T> = {
  output: T;
  model: string;
  provider: AIProvider;
  tokensIn?: number;
  tokensOut?: number;
  costEstimate?: number;
  traceId?: string;
};
```

## 7.3 Uso de IA por módulo

| Módulo      | Função da IA                        |
| ----------- | ----------------------------------- |
| Diagnóstico | resumir entrevista, extrair rotinas |
| Processos   | gerar AS IS e TO BE                 |
| Rotinas     | classificar potencial               |
| Matriz      | justificar score                    |
| Integrações | sugerir desenho técnico             |
| Agentes     | gerar prompt base                   |
| Workflows   | gerar checklist                     |
| Docs        | gerar SOP                           |
| Logs        | explicar falhas                     |
| ROI         | explicar economia                   |
| Backlog     | gerar critérios de aceite           |

---

# 8. RAG e base de conhecimento

## Quando usar RAG

Usar RAG para:

* documentos do cliente;
* SOPs;
* políticas internas;
* FAQs;
* contratos;
* manuais;
* base de atendimento;
* relatórios anteriores;
* histórico de automações.

## Stack

* Postgres + pgvector no MVP;
* Qdrant ou Weaviate se volume crescer;
* Supabase Storage para arquivos;
* tabela de embeddings;
* controle por empresa.

Supabase suporta pgvector, extensão do Postgres para armazenar embeddings e fazer busca por similaridade, útil para RAG com documentos e bases internas. ([Supabase][6])

## Pipeline de documento

```text
Upload do documento
↓
Extrair texto
↓
Dividir em chunks
↓
Gerar embeddings
↓
Salvar em document_chunks
↓
Associar company_id
↓
Aplicar permissão
↓
Disponibilizar para agente
```

## Tabela document_chunks

```sql
create table document_chunks (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  document_id uuid not null references documents(id),
  chunk_index int not null,
  content text not null,
  embedding vector(1536),
  metadata jsonb default '{}',
  created_at timestamptz default now()
);
```

---

# 9. n8n Runtime

## Papel do n8n

n8n é o motor de execução de workflow.

FactoryOS é o cérebro de produto.
n8n é o encanamento automatizado.

## Responsabilidades do n8n

* receber webhooks;
* chamar APIs;
* transformar payloads;
* acionar IA quando fizer sentido;
* criar registros externos;
* atualizar ferramentas;
* enviar notificações;
* executar rotinas;
* emitir logs para FactoryOS.

## Responsabilidades da FactoryOS

* decidir o que automatizar;
* versionar desenho;
* registrar integração;
* gerenciar risco;
* medir ROI;
* controlar status;
* criar documentação;
* auditar execução.

## Integração FactoryOS ↔ n8n

```text
FactoryOS cria IntegrationPlan
↓
FactoryOS cria WorkflowSpec
↓
Dev cria workflow no n8n
↓
n8n retorna workflow_id
↓
FactoryOS salva referência
↓
n8n executa
↓
n8n envia callback/log para FactoryOS
↓
FactoryOS atualiza execução, ROI e incidentes
```

## Dados de execução

n8n define uma execução como uma única rodada de um workflow, com modo manual para teste e produção para workflows ativos, além de listas de execução e redaction para proteger dados sensíveis. ([n8n Docs][7])

## Observação importante

Na V1, **não precisa construir editor visual de workflow próprio**.
Isso é armadilha.
A V1 precisa registrar, documentar, monitorar e apontar para o workflow no n8n.

Editor visual próprio só depois que a fábrica estiver imprimindo dinheiro.

---

# 10. Segurança de credenciais

## Regra sagrada

> A FactoryOS nunca deve salvar senha, token ou API key em texto aberto.

## Modelo

```text
CredentialReference
├── provider
├── label
├── environment
├── vault_provider
├── external_reference
├── owner_company_id
├── access_scope
└── status
```

## Opções

### MVP simples

* credenciais ficam no n8n;
* FactoryOS salva apenas referência;
* exemplo: `n8n_credential_id`.

### Produção séria

* Bitwarden Secrets;
* 1Password;
* AWS Secrets Manager;
* GCP Secrets Manager;
* Azure Key Vault;
* HashiCorp Vault.

n8n armazena credenciais criptografadas em seu banco e, em planos Enterprise, suporta external secrets com provedores como 1Password, AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager e HashiCorp Vault. ([n8n Docs][8])

---

# 11. Multiempresa e segurança

## Modelo recomendado

```text
company_id em todas as tabelas de negócio
organization_id para conta/fábrica
RLS por company_id
RBAC por papel
audit_logs para tudo
```

## Papéis

```text
factory_admin
factory_consultant
factory_automation_analyst
factory_ai_specialist
factory_developer
client_admin
client_manager
client_operator
viewer
```

## Política conceitual

```sql
create policy "users_can_access_company_data"
on routines
for select
using (
  company_id in (
    select company_id
    from memberships
    where user_id = auth.uid()
  )
);
```

## Regra brutal

Não confia em `company_id` vindo do frontend.

O backend e o RLS precisam validar se o usuário pertence à empresa.
Senão vira self-service de vazamento de dado, aquele buffet infernal onde um cliente pega o contrato do outro.

---

# 12. Modelo de dados completo V1

## Entidades principais

```text
companies
memberships
departments
tools
company_tools
processes
process_steps
routines
automation_opportunities
integrations
integration_mappings
ai_agents
prompts
knowledge_bases
documents
document_chunks
workflows
workflow_steps
workflow_executions
execution_logs
approval_requests
backlog_items
roi_records
dashboards
kpis
governance_rules
incidents
audit_logs
templates
```

---

## 12.1 companies

```sql
create table companies (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  segment text,
  size text,
  employee_count int,
  revenue_range text,
  sales_model text,
  status text default 'new',
  maturity_score numeric default 0,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```

---

## 12.2 memberships

```sql
create table memberships (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  user_id uuid not null,
  role text not null,
  status text default 'active',
  created_at timestamptz default now()
);
```

---

## 12.3 departments

```sql
create table departments (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  name text not null,
  leader_name text,
  people_count int default 0,
  pain_level int default 0,
  automation_potential int default 0,
  risk_level text default 'medium',
  notes text,
  created_at timestamptz default now()
);
```

---

## 12.4 tool_catalog

```sql
create table tool_catalog (
  id text primary key,
  name text not null,
  category text not null,
  has_api boolean default false,
  has_webhook boolean default false,
  auth_methods text[] default '{}',
  common_objects text[] default '{}',
  docs_url text,
  integration_level text default 'unknown',
  created_at timestamptz default now()
);
```

---

## 12.5 company_tools

```sql
create table company_tools (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  tool_id text references tool_catalog(id),
  custom_tool_name text,
  department_id uuid references departments(id),
  status text default 'active',
  criticality text default 'medium',
  usage_notes text,
  credential_reference_id uuid,
  created_at timestamptz default now()
);
```

---

## 12.6 processes

```sql
create table processes (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  department_id uuid references departments(id),
  name text not null,
  description text,
  status text default 'mapped',
  owner_name text,
  created_at timestamptz default now()
);
```

---

## 12.7 process_versions

```sql
create table process_versions (
  id uuid primary key default gen_random_uuid(),
  process_id uuid not null references processes(id),
  version_type text not null check (version_type in ('AS_IS', 'TO_BE', 'AUTOMATED')),
  version_number int default 1,
  notes text,
  created_at timestamptz default now()
);
```

---

## 12.8 process_steps

```sql
create table process_steps (
  id uuid primary key default gen_random_uuid(),
  process_version_id uuid not null references process_versions(id),
  step_order int not null,
  name text not null,
  responsible_role text,
  tool_id text,
  time_minutes int,
  input_data jsonb default '{}',
  output_data jsonb default '{}',
  pain_point text,
  risk_level text default 'medium',
  automation_candidate boolean default false,
  ai_candidate boolean default false
);
```

---

## 12.9 routines

```sql
create table routines (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  department_id uuid references departments(id),
  process_id uuid references processes(id),
  name text not null,
  description text,
  frequency text,
  time_per_execution_minutes int default 0,
  monthly_volume int default 0,
  monthly_time_minutes int generated always as (time_per_execution_minutes * monthly_volume) stored,
  responsible_role text,
  tools_used text[] default '{}',
  input_description text,
  output_description text,
  common_errors text,
  failure_risk text,
  is_repetitive boolean default true,
  has_clear_rules boolean default false,
  has_digital_data boolean default false,
  automation_potential int default 0,
  ai_potential int default 0,
  status text default 'identified',
  priority text,
  created_at timestamptz default now()
);
```

---

## 12.10 automation_opportunities

```sql
create table automation_opportunities (
  id uuid primary key default gen_random_uuid(),
  routine_id uuid not null references routines(id),
  company_id uuid not null references companies(id),
  frequency_score int default 0,
  volume_score int default 0,
  time_score int default 0,
  cost_score int default 0,
  error_score int default 0,
  customer_impact_score int default 0,
  financial_impact_score int default 0,
  technical_feasibility_score int default 0,
  data_availability_score int default 0,
  integration_availability_score int default 0,
  ai_potential_score int default 0,
  risk_score int default 0,
  complexity_score int default 0,
  roi_score int default 0,
  automation_score numeric default 0,
  estimated_hours_saved_month numeric default 0,
  estimated_money_saved_month numeric default 0,
  recommendation text,
  created_at timestamptz default now()
);
```

---

## 12.11 integrations

```sql
create table integrations (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  name text not null,
  source_tool_id uuid references company_tools(id),
  target_tool_id uuid references company_tools(id),
  integration_type text not null,
  trigger_type text,
  trigger_event text,
  action text,
  middleware text default 'n8n',
  object_name text,
  requires_ai boolean default false,
  requires_human_approval boolean default false,
  risk_level text default 'medium',
  status text default 'idea',
  n8n_workflow_id text,
  documentation_url text,
  created_at timestamptz default now()
);
```

---

## 12.12 integration_mappings

```sql
create table integration_mappings (
  id uuid primary key default gen_random_uuid(),
  integration_id uuid not null references integrations(id),
  source_field text not null,
  target_field text not null,
  transform_rule text,
  required boolean default false,
  validation_rule text,
  example_value text
);
```

---

## 12.13 ai_agents

```sql
create table ai_agents (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  department_id uuid references departments(id),
  name text not null,
  objective text not null,
  autonomy_level int default 1,
  model_provider text,
  model_name text,
  allowed_data text[] default '{}',
  allowed_actions text[] default '{}',
  forbidden_actions text[] default '{}',
  requires_human_approval boolean default true,
  fallback_human_role text,
  status text default 'draft',
  created_at timestamptz default now()
);
```

---

## 12.14 prompts

```sql
create table prompts (
  id uuid primary key default gen_random_uuid(),
  agent_id uuid references ai_agents(id),
  name text not null,
  version int default 1,
  type text default 'system',
  content text not null,
  output_schema jsonb,
  status text default 'draft',
  langfuse_prompt_id text,
  created_at timestamptz default now()
);
```

---

## 12.15 workflows

```sql
create table workflows (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  routine_id uuid references routines(id),
  integration_id uuid references integrations(id),
  name text not null,
  trigger_description text,
  status text default 'draft',
  environment text default 'dev',
  version int default 1,
  n8n_workflow_id text,
  n8n_url text,
  estimated_minutes_saved_per_run int default 0,
  created_at timestamptz default now()
);
```

---

## 12.16 workflow_executions

```sql
create table workflow_executions (
  id uuid primary key default gen_random_uuid(),
  workflow_id uuid not null references workflows(id),
  company_id uuid not null references companies(id),
  external_execution_id text,
  status text not null,
  started_at timestamptz,
  finished_at timestamptz,
  duration_ms int,
  error_message text,
  input_summary jsonb default '{}',
  output_summary jsonb default '{}',
  created_at timestamptz default now()
);
```

---

## 12.17 approval_requests

```sql
create table approval_requests (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  workflow_id uuid references workflows(id),
  agent_id uuid references ai_agents(id),
  requested_by text,
  approval_type text not null,
  payload jsonb not null,
  status text default 'pending',
  approved_by uuid,
  approved_at timestamptz,
  rejected_reason text,
  expires_at timestamptz,
  created_at timestamptz default now()
);
```

---

## 12.18 roi_records

```sql
create table roi_records (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  routine_id uuid references routines(id),
  workflow_id uuid references workflows(id),
  period_month date not null,
  hours_before numeric default 0,
  hours_after numeric default 0,
  hours_saved numeric default 0,
  cost_per_hour numeric default 0,
  estimated_savings numeric default 0,
  real_savings numeric default 0,
  confidence_level text default 'estimated',
  created_at timestamptz default now()
);
```

---

## 12.19 audit_logs

```sql
create table audit_logs (
  id uuid primary key default gen_random_uuid(),
  company_id uuid references companies(id),
  actor_user_id uuid,
  actor_type text,
  action text not null,
  entity_type text not null,
  entity_id uuid,
  before_data jsonb,
  after_data jsonb,
  ip_address text,
  user_agent text,
  created_at timestamptz default now()
);
```

---

# 13. API Blueprint

## 13.1 Padrão de API

```text
/api/v1/companies
/api/v1/companies/:id/departments
/api/v1/companies/:id/tools
/api/v1/companies/:id/processes
/api/v1/companies/:id/routines
/api/v1/companies/:id/opportunities
/api/v1/companies/:id/integrations
/api/v1/companies/:id/agents
/api/v1/companies/:id/workflows
/api/v1/companies/:id/roi
/api/v1/companies/:id/backlog
/api/v1/companies/:id/documents
/api/v1/companies/:id/audit-logs
```

## 13.2 Rotas principais

### Criar empresa

```http
POST /api/v1/companies
```

```json
{
  "name": "Cliente X",
  "segment": "Clínica",
  "employee_count": 32,
  "sales_model": "Leads via WhatsApp e indicação"
}
```

---

### Criar rotina

```http
POST /api/v1/companies/:companyId/routines
```

```json
{
  "department_id": "dept_001",
  "name": "Cobrança de clientes atrasados",
  "frequency": "daily",
  "time_per_execution_minutes": 120,
  "monthly_volume": 22,
  "tools_used": ["Omie", "WhatsApp", "Google Sheets"],
  "common_errors": "Cliente fica sem cobrança por esquecimento"
}
```

---

### Calcular oportunidade

```http
POST /api/v1/routines/:routineId/calculate-score
```

Resposta:

```json
{
  "automation_score": 87,
  "priority": "P0",
  "estimated_hours_saved_month": 40,
  "estimated_money_saved_month": 3200,
  "recommendation": "Automatizar primeiro com aprovação humana"
}
```

---

### Gerar relatório com IA

```http
POST /api/v1/companies/:companyId/reports/diagnostic
```

Resposta:

```json
{
  "report_id": "report_001",
  "status": "processing"
}
```

---

### Receber callback do n8n

```http
POST /api/v1/webhooks/n8n/executions
```

```json
{
  "workflow_external_id": "n8n_123",
  "execution_id": "exec_456",
  "status": "success",
  "started_at": "2026-06-03T10:00:00Z",
  "finished_at": "2026-06-03T10:00:08Z",
  "custom_data": {
    "company_id": "company_001",
    "routine_id": "routine_001"
  }
}
```

---

# 14. Lifecycle completo de automação

## Status macro

```text
Identificada
↓
Pontuada
↓
Priorizada
↓
Desenhada
↓
Aprovada
↓
Implementada
↓
Testada
↓
Homologada
↓
Ativa
↓
Monitorada
↓
Otimizada
```

## Detalhamento técnico

```text
Routine identified
↓
AutomationOpportunity generated
↓
BacklogItem created
↓
Process TO_BE designed
↓
Integration mapped
↓
Agent configured
↓
WorkflowSpec created
↓
n8n workflow built
↓
TestCase executed
↓
ApprovalRequest completed
↓
Workflow active
↓
Execution logs received
↓
ROI measured
```

---

# 15. Scoring Engine

## Fórmula V1

```text
ImpactScore =
frequency_score +
volume_score +
time_score +
cost_score +
error_score +
customer_impact_score +
financial_impact_score

FeasibilityScore =
technical_feasibility_score +
data_availability_score +
integration_availability_score +
ai_potential_score

PenaltyScore =
risk_score +
complexity_score

AutomationScore =
((ImpactScore * 0.45) + (FeasibilityScore * 0.35) + (roi_score * 0.20)) - PenaltyScore
```

## Classificação

|    Score | Prioridade      | Interpretação               |
| -------: | --------------- | --------------------------- |
| 80 a 100 | P0              | Automatizar primeiro        |
|  60 a 79 | P1              | Alta prioridade             |
|  40 a 59 | P2              | Planejar                    |
|  20 a 39 | P3              | Baixa prioridade            |
|   0 a 19 | Não automatizar | Processo ruim ou risco alto |

## Regras extras

```text
Se risk_score >= 5 e requires_human_approval = false, bloquear.
Se has_digital_data = false, reduzir viabilidade.
Se has_clear_rules = false, exigir análise humana.
Se impact_score alto e effort baixo, marcar Quick Win.
Se ação toca dinheiro, contrato ou dado sensível, exigir ApprovalRequest.
```

---

# 16. Human-in-the-loop

## Quando exigir aprovação humana

```text
Enviar cobrança
Enviar proposta
Enviar contrato
Alterar status financeiro
Criar ou cancelar pagamento
Enviar mensagem sensível
Alterar dado de cliente
Acionar jurídico
Encerrar reclamação crítica
Excluir registro
Ativar workflow crítico
```

## Fluxo

```text
Agente gera ação
↓
FactoryOS cria ApprovalRequest
↓
Humano recebe card
↓
Humano aprova, rejeita ou edita
↓
Sistema registra decisão
↓
n8n executa ação
↓
FactoryOS salva log
```

## Card de aprovação

```text
Ação: Enviar cobrança
Cliente: João Silva
Valor: R$ 1.280,00
Vencimento: 02/06/2026
Mensagem gerada:
"Olá, João..."

Botões:
[Aprovar] [Editar] [Rejeitar]
```

---

# 17. Observabilidade

## Logs obrigatórios

```text
API request
AI call
prompt version
model used
tool called
workflow execution
approval decision
external API response
error
retry
human override
```

## Tracing de IA

Salvar:

```text
company_id
agent_id
prompt_id
prompt_version
input_hash
output_hash
model
provider
tokens
cost
latency
trace_id
evaluation_score
```

## Ferramenta recomendada

Langfuse para:

* traces;
* prompt management;
* versões;
* métricas por prompt;
* avaliações;
* datasets de teste.

---

# 18. Monitoramento de workflows

## Métricas

```text
workflows ativos
execuções por dia
falhas por workflow
tempo médio de execução
erro por API
credenciais expiradas
custo de IA
aprovações pendentes
mensagens não enviadas
retries
incidentes
```

## Alertas

```text
workflow falhou 3 vezes em 1 hora
API retornou 401
API retornou 429
webhook não recebido
custo de IA acima do limite
aprovação pendente há mais de X horas
execução crítica sem log
dashboard sem atualização
```

## Incidentes

```sql
create table incidents (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references companies(id),
  workflow_id uuid references workflows(id),
  severity text not null,
  title text not null,
  description text,
  status text default 'open',
  root_cause text,
  resolution text,
  created_at timestamptz default now(),
  resolved_at timestamptz
);
```

---

# 19. Documentação automática

Toda automação gera documentação.

## Templates obrigatórios

```text
SOP do processo
Mapa AS IS
Mapa TO BE
Mapa automatizado
Mapa de dados
Mapa de integração
Checklist de teste
Plano de rollback
Manual de uso
Critérios de aceite
Relatório de implantação
```

## Exemplo de SOP

```text
Título: Cobrança Inteligente de Inadimplentes

Objetivo:
Reduzir trabalho manual do financeiro e padronizar cobranças.

Gatilho:
Pagamento vencido há 1 dia.

Entrada:
Cliente, valor, vencimento, link de pagamento, histórico.

Processamento:
1. Buscar inadimplentes no ERP.
2. Validar status.
3. Gerar mensagem por IA.
4. Solicitar aprovação humana.
5. Enviar WhatsApp.
6. Registrar no CRM.
7. Atualizar dashboard.

Riscos:
Cobrança indevida, tom inadequado, dado incorreto.

Controles:
Aprovação humana, horário comercial, log obrigatório.

Rollback:
Pausar workflow no n8n e reverter status manualmente.
```

---

# 20. Integrações prioritárias por fase

## Fase 1: MVP sem integração profunda

```text
Google Sheets
Google Drive
n8n webhook
ClickUp
Notion
OpenAI/Claude/Gemini
Metabase/Looker Studio
```

## Fase 2: Comercial e atendimento

```text
RD Station
HubSpot
Pipedrive
Kommo
ManyChat
WhatsApp API
Z-API
Chatwoot
```

## Fase 3: Financeiro e ERP

```text
Omie
Bling
Conta Azul
Tiny
Asaas
Iugu
Pagar.me
Mercado Pago
```

## Fase 4: Operação e gestão

```text
ClickUp
Airtable
Monday
Trello
Google Calendar
Gmail
Slack/Google Chat/Telegram
```

## Fase 5: Enterprise

```text
Salesforce
SAP Business One
TOTVS
Sankhya
ServiceNow
Power BI
Azure/GCP/AWS Secrets
```

---

# 21. Estrutura de repositório

## Repositório único no começo

```text
factoryos-ia/
├── apps/
│   └── web/
│       ├── app/
│       ├── components/
│       ├── lib/
│       ├── modules/
│       └── api/
├── packages/
│   ├── database/
│   ├── ai/
│   ├── integrations/
│   ├── scoring/
│   ├── governance/
│   ├── templates/
│   └── shared/
├── supabase/
│   ├── migrations/
│   ├── functions/
│   └── seed/
├── n8n/
│   ├── workflows/
│   ├── templates/
│   └── docs/
├── docs/
│   ├── PRD.md
│   ├── BLUEPRINT.md
│   ├── API.md
│   ├── DATA_MODEL.md
│   └── SECURITY.md
└── tests/
```

## Módulos internos

```text
modules/company
modules/diagnostic
modules/departments
modules/tools
modules/processes
modules/routines
modules/scoring
modules/integrations
modules/agents
modules/workflows
modules/roi
modules/backlog
modules/docs
modules/governance
modules/monitoring
modules/library
```

---

# 22. Ambientes

## Dev

* banco local ou Supabase dev;
* n8n dev;
* dados mockados;
* IA com baixo custo;
* logs verbosos.

## Staging

* banco separado;
* n8n staging;
* credenciais fake ou sandbox;
* testes de integração;
* simulação de workflows.

## Production

* banco produção;
* RLS ativo;
* backups;
* logs;
* rate limiting;
* monitoramento;
* secrets gerenciados;
* workflows aprovados.

Supabase Edge Functions podem servir como endpoints TypeScript para webhooks, integrações e pequenas orquestrações, com secrets via variáveis de ambiente e logs de invocação. ([Supabase][9])

---

# 23. Testes

## Testes obrigatórios

```text
unit tests
integration tests
RLS tests
API tests
AI schema tests
prompt regression tests
workflow dry-run tests
webhook signature tests
approval flow tests
permission tests
```

## Teste de integração

```text
Dado um lead novo no webhook
Quando o n8n receber o payload
Então deve normalizar o dado
E enviar para FactoryOS
E registrar execution_log
E atualizar routine metric
```

## Teste de IA

```text
Dado uma entrevista de diagnóstico
Quando a IA extrair rotinas
Então deve retornar JSON válido
E cada rotina precisa ter setor, frequência, tempo, dor e potencial
E nenhuma ação externa deve ser executada
```

---

# 24. Segurança

## Checklist mínimo

```text
RLS ativo
RBAC implementado
audit_logs em ações críticas
secrets fora do banco principal
aprovação humana para ações sensíveis
logs sem dados sensíveis completos
rate limit nas APIs
validação de payload
webhook signature quando disponível
prompt injection defense
output schema validation
least privilege para agentes
backup
rollback
```

## Defesa contra prompt injection

Regra de ouro:

> Conteúdo vindo de cliente, documento, site, e-mail ou ticket nunca é instrução confiável.

## Estratégias

```text
separar system prompt de dados
marcar conteúdo externo como não confiável
usar schema rígido
bloquear ações fora de escopo
human approval em ações críticas
registrar tool calls
não expor secrets ao modelo
não permitir que IA escolha credenciais
validar payload antes de executar
```

Pesquisas recentes sobre workflows agentic apontam risco de hijacking via entradas controladas por adversários em ambientes com agentes e ferramentas, inclusive em automações, então a FactoryOS deve tratar todo agente com tool access como superfície crítica. ([arXiv][10])

---

# 25. Deploy

## MVP rápido

```text
Frontend: Vercel
Banco: Supabase
Auth: Supabase Auth
n8n: n8n Cloud ou self-host em VPS
Observabilidade IA: Langfuse Cloud
BI: Metabase Cloud ou Looker Studio
```

## Produção com controle

```text
Frontend: Vercel ou Coolify
Backend: Next.js server
Banco: Supabase ou Postgres gerenciado
n8n: self-host Docker
Redis: Upstash ou Redis VPS
Langfuse: Cloud ou self-host
Storage: Supabase Storage ou Cloudflare R2
DNS/WAF: Cloudflare
Monitoring: Sentry + Uptime Kuma/Better Stack
```

## Deploy self-host

```text
Docker Compose
├── factoryos-web
├── postgres
├── redis
├── n8n
├── metabase
├── langfuse
└── reverse-proxy
```

---

# 26. MVP técnico recomendado

## O que construir primeiro

```text
1. Auth
2. Empresas
3. Setores
4. Ferramentas
5. Processos
6. Rotinas
7. Matriz de automação
8. ROI estimado
9. Backlog
10. Relatório diagnóstico com IA
```

## O que não construir ainda

```text
editor visual próprio de workflow
marketplace de templates
integração real com 50 ferramentas
agente autônomo avançado
billing SaaS complexo
BI customizado gigante
mobile app
```

O MVP deve vender diagnóstico e gerar backlog.
Sem isso, você constrói foguete sem saber se tem pista.

---

# 27. Roadmap 4x10 de execução

## Wave 1: Fundação do Produto

| Bloco | Entrega                          |
| ----: | -------------------------------- |
|     1 | Criar repo e arquitetura Next.js |
|     2 | Configurar Supabase/Postgres     |
|     3 | Criar Auth e RBAC básico         |
|     4 | Criar módulo Companies           |
|     5 | Criar módulo Departments         |
|     6 | Criar Tool Catalog               |
|     7 | Criar Company Tools              |
|     8 | Criar sidebar e cockpit base     |
|     9 | Criar audit_logs                 |
|    10 | Seed com dados mockados          |

## Wave 2: Diagnóstico e Rotinas

| Bloco | Entrega                 |
| ----: | ----------------------- |
|     1 | Wizard de diagnóstico   |
|     2 | Processos AS IS / TO BE |
|     3 | Process steps           |
|     4 | Rotinas                 |
|     5 | Filtros de rotinas      |
|     6 | Scoring engine          |
|     7 | Matriz de automação     |
|     8 | Prioridades P0/P1/P2/P3 |
|     9 | ROI estimado            |
|    10 | Relatório inicial       |

## Wave 3: Integrações, IA e Backlog

| Bloco | Entrega                     |
| ----: | --------------------------- |
|     1 | Módulo Integrations         |
|     2 | Integration mappings        |
|     3 | AI Provider Layer           |
|     4 | Prompt templates            |
|     5 | Agentes de IA               |
|     6 | Geração de relatório com IA |
|     7 | Backlog Kanban              |
|     8 | Approval Requests           |
|     9 | Docs/SOP generator          |
|    10 | Export Markdown             |

## Wave 4: Workflows, Monitoramento e Governança

| Bloco | Entrega                    |
| ----: | -------------------------- |
|     1 | Módulo Workflows           |
|     2 | Referência n8n_workflow_id |
|     3 | Webhook receiver n8n       |
|     4 | Workflow executions        |
|     5 | Execution logs             |
|     6 | Incidents                  |
|     7 | Monitoramento              |
|     8 | Governança de IA           |
|     9 | Langfuse tracing           |
|    10 | Release MVP piloto         |

---

# 28. Critérios de aceite do MVP

## Produto só está pronto quando:

```text
Usuário cria empresa
Usuário cadastra setores
Usuário cadastra ferramentas
Usuário registra processos
Usuário cadastra rotinas
Sistema calcula score
Sistema classifica prioridade
Sistema gera backlog
Sistema estima ROI
IA gera relatório diagnóstico
Sistema salva audit logs
Usuário consegue exportar relatório
```

## Critério brutal

Se não gerar uma proposta vendável para cliente real, ainda não é MVP.
É brinquedo caro com login.

---

# 29. Blueprint de uma automação exemplo

## Rotina

Cobrança de inadimplentes.

## AS IS

```text
Financeiro abre ERP
↓
Filtra clientes atrasados
↓
Copia dados
↓
Monta mensagem
↓
Manda WhatsApp
↓
Atualiza planilha
↓
Avisa gestor manualmente
```

## TO BE

```text
ERP identifica atraso
↓
n8n busca cliente
↓
FactoryOS valida regra
↓
IA gera mensagem
↓
Humano aprova
↓
WhatsApp envia
↓
CRM registra interação
↓
Dashboard atualiza
↓
ROI calcula tempo economizado
```

## Workflow Spec

```json
{
  "name": "Cobrança Inteligente",
  "trigger": "invoice_overdue",
  "source": "Omie",
  "middleware": "n8n",
  "steps": [
    "fetch_overdue_invoice",
    "validate_customer_status",
    "generate_ai_message",
    "create_approval_request",
    "wait_for_approval",
    "send_whatsapp_message",
    "log_crm_activity",
    "update_dashboard",
    "create_execution_log"
  ],
  "risk": "medium",
  "requires_human_approval": true
}
```

---

# 30. Prompt para Claude Code executar o Blueprint

```text
Você é um dev sênior full-stack especialista em SaaS B2B, integrações, IA, Supabase, PostgreSQL, Next.js, n8n e segurança.

Contexto:
Vamos criar o MVP da FactoryOS IA, uma plataforma para diagnosticar empresas, mapear processos, identificar rotinas repetitivas, priorizar automações por ROI, registrar integrações, criar agentes de IA, controlar workflows, gerar documentação e monitorar automações.

Siga o Blueprint Técnico V1.0.

Regras:
- Não fazer ações destrutivas.
- Não usar git add -A.
- Criar commits apenas com caminhos explícitos quando autorizado.
- Não expor secrets.
- Criar estrutura modular.
- Priorizar MVP: empresas, setores, ferramentas, processos, rotinas, scoring, ROI, backlog e relatório.
- Implementar RLS e RBAC desde o início.
- Criar seed com dados mockados realistas em português.
- Criar testes para scoring, permissões e schemas de IA.
- Não construir editor visual próprio de workflow na V1.
- n8n deve ser referenciado por workflow_id e callback webhook.

Stack:
Next.js, TypeScript, Tailwind, shadcn/ui, Supabase/PostgreSQL, RLS, AI provider layer, Langfuse opcional, n8n integration references.

Entrega:
1. Estrutura de pastas.
2. Schema SQL inicial.
3. Migrations.
4. Models/types.
5. CRUD Companies.
6. CRUD Departments.
7. CRUD Tools.
8. CRUD Processes.
9. CRUD Routines.
10. Scoring Engine.
11. ROI Engine.
12. Backlog.
13. Dashboard inicial.
14. Relatório diagnóstico básico.
15. Documentação técnica.
```

---

# 31. Decisões finais de engenharia

## Decisão 1

Começar com **modular monolith**, não microserviços.

## Decisão 2

n8n executa workflows. FactoryOS governa, documenta, mede e monitora.

## Decisão 3

IA nunca executa ação crítica sem ApprovalRequest.

## Decisão 4

RLS e audit_logs entram desde o primeiro commit.

## Decisão 5

ROI é feature central, não enfeite.

## Decisão 6

Biblioteca de templates é o caminho para escala.

## Decisão 7

A primeira versão vende diagnóstico. A segunda vende execução. A terceira vende operação contínua.

---

# 32. Síntese de dev sênior

Tigrão, o Blueprint verdadeiro é este:

> **FactoryOS IA é um SaaS multiempresa com núcleo em processos, rotinas e ROI, usando Supabase/Postgres como memória, Next.js como interface, n8n como executor de workflows, IA como camada cognitiva, Langfuse como observabilidade, RLS/RBAC como segurança, e bibliotecas de templates para escala.**

A frase de arquitetura:

> **Diagnóstico vira rotina. Rotina vira score. Score vira backlog. Backlog vira integração. Integração vira workflow. Workflow vira economia. Economia vira venda.**

Isso aqui é o osso de adamantium do projeto.
Agora sim dá para sair do “tive uma ideia” e entrar no “temos engenharia”. 🐅⚙️

[1]: https://supabase.com/docs/guides/database/postgres/row-level-security?utm_source=chatgpt.com "Row Level Security | Supabase Docs"
[2]: https://docs.n8n.io/api/?utm_source=chatgpt.com "n8n public REST API Documentation and Guides | n8n Docs"
[3]: https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com "Function Calling in the OpenAI API | OpenAI Help Center"
[4]: https://langfuse.com/docs/prompt-management/overview?utm_source=chatgpt.com "Open Source Prompt Management - Langfuse"
[5]: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ "OWASP Top 10 for LLM Applications 2025"
[6]: https://supabase.com/docs/guides/database/extensions/pgvector?utm_source=chatgpt.com "pgvector: Embeddings and vector similarity | Supabase Docs"
[7]: https://docs.n8n.io/workflows/executions/?utm_source=chatgpt.com "Executions | n8n Docs"
[8]: https://docs.n8n.io/external-secrets/?utm_source=chatgpt.com "External secrets | n8n Docs"
[9]: https://supabase.com/docs/guides/functions?utm_source=chatgpt.com "Edge Functions | Supabase Docs"
[10]: https://arxiv.org/abs/2605.11229?utm_source=chatgpt.com "Comment and Control: Hijacking Agentic Workflows via Context-Grounded Evolution"
