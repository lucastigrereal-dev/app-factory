Tigrão, fechou. Vou assumir que você quis dizer **PRD** mesmo, o documento-mãe do produto.
E aqui vai a primeira versão **completa**, já nascendo como base para depois virar **Blueprint técnico**, prompt de pesquisa no Perplexity/PerplexKit e execução em app.

A base vem da nossa consolidação da **FactoryOS IA: cockpit da Fábrica de Automação Empresarial com IA**, com diagnóstico, rotinas, ferramentas, integrações, IA, n8n, ROI, backlog e governança. 

---

# PRD V1.0

# **FactoryOS IA**

## Sistema Operacional da Fábrica de Automação Empresarial com IA

**Data:** 03/06/2026
**Produto:** FactoryOS IA
**Tipo:** SaaS B2B / Plataforma interna da Fábrica / Cockpit de automação empresarial
**Versão:** PRD V1.0
**Status:** Rascunho completo para pesquisa, validação e Blueprint
**Dono do produto:** Lucas Tigre / Fábrica de Automações
**Persona estratégica:** Aurora Tigre, Diretora de Produto, Operações e IA

---

# 1. Resumo executivo

A **FactoryOS IA** é uma plataforma para diagnosticar empresas, mapear processos, identificar rotinas repetitivas, priorizar oportunidades de automação, conectar ferramentas, criar agentes de IA, executar workflows e provar economia operacional.

Ela não é apenas um painel bonito.
Ela é o **sistema operacional da Fábrica de Automação Empresarial com IA**.

A plataforma deve permitir que consultores, analistas e operadores da fábrica entrem em uma empresa, descubram onde existe desperdício de tempo, dinheiro e energia humana, e transformem isso em automações com IA, integrações, n8n, dashboards, documentação e governança.

A lógica central:

> **Analisar processos → identificar rotinas automatizáveis → calcular impacto → priorizar → desenhar fluxo → integrar ferramentas → aplicar IA → executar workflow → medir economia → evoluir continuamente.**

A base metodológica se apoia em práticas de BPM, modelagem de processos, process mining, automação, agentes de IA e integração via APIs. BPMN, por exemplo, existe justamente para representar processos de negócio de forma compreensível para áreas de negócio e precisa o suficiente para times técnicos. ([OMG][1])

---

# 2. Problema

Empresas operam com processos espalhados, ferramentas desconectadas, dados duplicados e rotinas manuais demais.

Na prática, isso gera:

* perda de tempo;
* retrabalho;
* falhas humanas;
* leads esquecidos;
* cobranças atrasadas;
* dados perdidos em planilhas;
* atendimento sem histórico;
* relatórios manuais;
* gestão sem visão;
* dependência de pessoas-chave;
* processos que ninguém sabe explicar;
* ferramentas que não conversam entre si.

A empresa acha que tem “operação”.
Mas muitas vezes tem só um monte de gente copiando, colando, lembrando, perguntando no WhatsApp e torcendo para nada explodir.

Isso é caro.
Isso é frágil.
Isso é o famoso **castelo de planilha com telhado de print**.

---

# 3. Oportunidade

A oportunidade é criar uma plataforma que transforme a automação empresarial em um processo consultivo, técnico, mensurável e escalável.

Hoje, muitas automações são feitas de forma artesanal:

> “Me fala o que você quer automatizar que eu monto no n8n.”

Isso é fraco.

A FactoryOS IA inverte o jogo:

> “Eu descubro o que deve ser automatizado, provo o impacto, desenho o processo, conecto as ferramentas, aplico IA com segurança e mostro a economia.”

A automação deixa de ser gambiarra e vira método.

---

# 4. Visão do produto

## Visão

Transformar qualquer empresa em uma operação mais conectada, automatizada, mensurável e assistida por IA.

## Missão

Permitir que a Fábrica de Automação Empresarial com IA diagnostique, priorize, implemente e monitore automações em empresas de diferentes setores, começando pelas rotinas que mais economizam tempo e dinheiro.

## Promessa

> **A FactoryOS IA identifica onde a empresa perde tempo e dinheiro, transforma rotinas repetitivas em fluxos inteligentes e mede a economia gerada.**

---

# 5. Tese central

Empresas não precisam primeiro de “mais IA”.

Empresas precisam primeiro descobrir:

1. o que fazem repetidamente;
2. o que custa tempo;
3. o que gera erro;
4. o que depende de humano demais;
5. o que pode ser padronizado;
6. o que pode ser automatizado;
7. onde a IA pode ler, resumir, classificar, sugerir, responder ou executar com aprovação.

A IA entra como camada cognitiva.
O n8n entra como orquestrador.
As APIs entram como conectores.
O banco entra como memória.
O dashboard entra como visão.
A governança entra como freio de segurança.

Sem freio, automação vira cavalo doido no shopping.

---

# 6. Objetivos do produto

## Objetivos principais

1. **Diagnosticar empresas**

   * mapear setores, processos, rotinas, ferramentas e gargalos.

2. **Identificar rotinas automatizáveis**

   * encontrar tarefas repetitivas, manuais, caras, frequentes e com dados disponíveis.

3. **Priorizar por impacto**

   * classificar rotinas por ROI, esforço, risco, complexidade e potencial de IA.

4. **Planejar automações**

   * desenhar AS IS, TO BE e fluxo automatizado.

5. **Mapear integrações**

   * conectar CRM, ERP, WhatsApp, Google, RD Station, HubSpot, Bitrix24, n8n, bancos, BI, ferramentas internas e sistemas customizados.

6. **Criar agentes de IA**

   * agentes por área: comercial, atendimento, financeiro, operações, RH, jurídico, gestão e BI.

7. **Controlar workflows**

   * acompanhar automações, principalmente n8n, APIs e webhooks.

8. **Medir economia**

   * calcular horas economizadas, dinheiro recuperado, erros reduzidos e payback.

9. **Gerar documentação**

   * SOPs, mapas de processo, manuais, testes, plano de rollback e governança.

10. **Monitorar operação**

    * logs, falhas, incidentes, custos de IA, status de integrações e saúde dos workflows.

---

# 7. Não objetivos da V1

A V1 não deve tentar ser tudo.

## Fora da V1

* substituir ERP;
* substituir CRM;
* criar um n8n próprio;
* virar ferramenta universal de BI;
* executar automações críticas sem aprovação humana;
* manipular dados sensíveis sem governança;
* prometer automação total de qualquer empresa;
* criar agentes autônomos sem limites;
* depender de uma única IA;
* depender de uma única ferramenta de automação.

Tapa simbólico: se tentar fazer tudo na V1, morre obeso igual software corporativo dos anos 2000, cheio de botão e sem alma.

---

# 8. Público-alvo

## Público inicial

Empresas pequenas e médias com operação minimamente estruturada, mas ainda muito manual.

### Segmentos prioritários

* clínicas;
* imobiliárias;
* turismo;
* agências;
* escolas;
* serviços B2B;
* multipropriedade;
* consultorias;
* e-commerces pequenos/médios;
* operações com WhatsApp forte;
* empresas com CRM mal utilizado;
* empresas com financeiro manual;
* empresas com equipe administrativa sobrecarregada.

## Usuários dentro da plataforma

### 1. Dono / CEO

Quer saber:

* onde perde dinheiro;
* o que automatizar primeiro;
* quanto economiza;
* quais riscos existem;
* qual área está travando.

### 2. Gestor operacional

Quer saber:

* onde o processo falha;
* quem faz o quê;
* quais tarefas atrasam;
* como padronizar execução.

### 3. Consultor da fábrica

Quer:

* conduzir diagnóstico;
* mapear processos;
* cadastrar rotinas;
* gerar relatório;
* montar backlog;
* vender implantação.

### 4. Analista de automação

Quer:

* entender regras;
* ver ferramentas;
* mapear integrações;
* construir workflow;
* testar fluxo;
* documentar.

### 5. Especialista de IA

Quer:

* definir agentes;
* criar prompts;
* configurar permissões;
* testar respostas;
* medir confiança;
* reduzir risco.

### 6. Desenvolvedor / integrador

Quer:

* ver APIs;
* webhooks;
* autenticação;
* objetos de dados;
* logs;
* payloads;
* erros;
* endpoints.

### 7. Cliente final / colaborador

Quer:

* usar automações sem sofrer;
* receber alertas claros;
* ter menos tarefa manual;
* consultar IA interna;
* seguir processos simples.

---

# 9. Proposta de valor

## Para o cliente

> “Nós mostramos onde sua empresa perde tempo e dinheiro, automatizamos as rotinas certas com IA e provamos a economia.”

## Para a fábrica

> “A FactoryOS IA transforma automação em método escalável, repetível e vendável.”

## Para o consultor

> “Você deixa de vender ferramenta e passa a vender clareza, economia e transformação operacional.”

---

# 10. Diferenciais do produto

## 1. Começa pelo processo, não pela ferramenta

A FactoryOS IA não começa perguntando “qual integração você quer?”.
Ela começa perguntando:

> “Qual rotina está drenando sua empresa?”

## 2. Calcula potencial de automação

Cada rotina recebe score de:

* impacto;
* frequência;
* tempo gasto;
* erro humano;
* custo;
* risco;
* viabilidade;
* potencial de IA;
* ROI.

## 3. Une diagnóstico e execução

A plataforma não fica só no consultivo.
Ela transforma diagnóstico em backlog, workflow, agente, integração e documentação.

## 4. Cria biblioteca reutilizável

Cada automação vira template para próximos clientes.

## 5. Tem governança nativa

IA não sai fazendo besteira com dado financeiro, jurídico ou pessoal sem limite.

## 6. Mede economia

A plataforma precisa provar:

* horas economizadas;
* custo reduzido;
* tempo de resposta menor;
* erros evitados;
* leads recuperados;
* cobranças executadas;
* relatórios automatizados.

---

# 11. Fundamentos técnicos validados

## BPM e modelagem de processos

A plataforma deve usar lógica de processos AS IS, TO BE e automatizado. BPMN é um padrão gráfico para representar processos de negócio de forma entendível por usuários de negócio e também útil para técnicos responsáveis por implementação. ([OMG][1])

## Process mining e task mining

Quando possível, a plataforma deve usar dados de sistemas para descobrir como processos realmente acontecem. Process mining analisa event logs de sistemas para revelar gargalos, variações e oportunidades de melhoria. ([OMG][1])

## n8n como orquestrador

O n8n usa nodes como blocos de workflow que iniciam fluxos, buscam/enviam dados e processam informações; isso sustenta a ideia de usar n8n como camada de orquestração de automações. ([n8n Docs][2])

O n8n também possui AI Agent node, que usa ferramentas e APIs externas para decidir ações conforme a tarefa, além de recurso de human review para tool calls sensíveis. Isso combina com a exigência do produto de agentes com aprovação humana em ações críticas. ([n8n Docs][3])

## APIs e integrações

RD Station, por exemplo, possui APIs distintas para Marketing, CRM e Conversas, com autenticação e endpoints próprios, o que reforça que a FactoryOS precisa tratar integrações por ferramenta, produto, escopo, autenticação e objeto de dados. ([RD Station Developers][4])

## IA com ferramentas e saídas estruturadas

Function Calling permite conectar modelos OpenAI a ferramentas e sistemas externos, e Structured Outputs permite exigir que argumentos sigam JSON Schema, o que é importante para agentes que criam tarefas, classificam rotinas, geram relatórios ou acionam automações com previsibilidade. ([OpenAI Help Center][5])

---

# 12. Jornada principal do produto

```text
1. Criar empresa
↓
2. Cadastrar setores
↓
3. Mapear ferramentas
↓
4. Rodar diagnóstico
↓
5. Mapear processos AS IS
↓
6. Levantar rotinas repetitivas
↓
7. Calcular score de automação
↓
8. Gerar ranking de oportunidades
↓
9. Desenhar TO BE
↓
10. Criar backlog
↓
11. Planejar integração
↓
12. Criar agente de IA
↓
13. Criar workflow
↓
14. Testar
↓
15. Documentar
↓
16. Ativar
↓
17. Monitorar
↓
18. Medir ROI
↓
19. Evoluir
```

Essa é a espinha dorsal.
Se alguém mexer nisso sem entender, leva chinelada conceitual.

---

# 13. Módulos do produto

## Módulo 1: Empresas

### Objetivo

Cadastrar e gerenciar empresas/clientes analisados pela fábrica.

### Funcionalidades

* criar empresa;
* editar empresa;
* selecionar empresa ativa;
* cadastrar segmento;
* cadastrar tamanho;
* cadastrar faturamento aproximado;
* cadastrar plano contratado;
* visualizar status do projeto;
* visualizar maturidade digital;
* visualizar economia estimada;
* visualizar próxima ação.

### Campos

```text
id
nome
segmento
tamanho
número de funcionários
faturamento aproximado
modelo de venda
responsável interno
responsável da fábrica
status do projeto
plano contratado
maturidade digital
data de início
observações
```

### Status

```text
Novo lead
Diagnóstico agendado
Diagnóstico em andamento
Raio-X entregue
Proposta enviada
Implantação em andamento
Automação ativa
Monitoramento
Pausado
Encerrado
```

---

## Módulo 2: Diagnóstico

### Objetivo

Conduzir o **Raio-X de Rotinas com IA**.

### Formato

Wizard em 10 etapas:

```text
1. Dados da empresa
2. Setores
3. Ferramentas
4. Processos principais
5. Rotinas repetitivas
6. Gargalos
7. Dados e documentos
8. Comunicação interna
9. Riscos e restrições
10. Priorização inicial
```

### Requisitos funcionais

* permitir salvar diagnóstico incompleto;
* permitir múltiplos respondentes;
* permitir anexar documentos;
* permitir registrar entrevistas;
* permitir gerar resumo por IA;
* permitir transformar respostas em rotinas;
* permitir gerar relatório automático;
* permitir marcar pontos críticos.

### Saídas do diagnóstico

* mapa de setores;
* inventário de ferramentas;
* lista de processos;
* lista de rotinas;
* gargalos;
* riscos;
* quick wins;
* score de maturidade;
* relatório executivo.

---

## Módulo 3: Setores

### Objetivo

Mapear áreas da empresa.

### Setores padrão

```text
Comercial
Marketing
Atendimento
Operações
Financeiro
Administrativo
RH
Jurídico
Compras
Estoque
TI
Diretoria
Produto
Suporte
Pós-venda
```

### Campos

```text
nome do setor
líder
número de pessoas
rotinas principais
ferramentas usadas
gargalos
indicadores existentes
nível de dor
potencial de automação
risco operacional
```

### Requisitos

* permitir setores customizados;
* associar ferramentas ao setor;
* associar rotinas ao setor;
* associar processos ao setor;
* calcular nota setorial.

---

## Módulo 4: Ferramentas

### Objetivo

Criar inventário de sistemas usados pelo cliente.

### Categorias

```text
CRM
ERP
Financeiro
Atendimento
Marketing
Google Workspace
Gestão de tarefas
Documentos
BI
Banco de dados
IA
Comunicação
Assinatura digital
RH
Jurídico
E-commerce
Dev/Infra
Segurança
```

### Ferramentas base

#### Orquestração

```text
n8n
Make
Zapier
Pipedream
Google Apps Script
Python
Node.js
Docker
```

#### IA

```text
OpenAI
ChatGPT
Claude
Gemini
Perplexity
DeepSeek
Qwen
Kimi
Mistral
OpenRouter
LiteLLM
LangChain
LlamaIndex
Langfuse
pgvector
Qdrant
Pinecone
Weaviate
```

#### Google

```text
Gmail
Drive
Docs
Sheets
Forms
Calendar
Meet
Chat
Tasks
Apps Script
AppSheet
Looker Studio
Gemini
NotebookLM
```

#### CRM

```text
HubSpot
RD Station CRM
RD Station Marketing
Pipedrive
Kommo
Bitrix24
Salesforce
Zoho CRM
Agendor
Moskit
```

#### Atendimento

```text
WhatsApp Business Platform
WhatsApp Cloud API
Twilio
Z-API
Evolution API
ManyChat
Chatwoot
Zendesk
Freshdesk
Intercom
Blip
Crisp
Telegram Bot API
```

#### Marketing

```text
RD Station Marketing
ManyChat
Meta Ads
Google Ads
GA4
Google Tag Manager
Search Console
Mailchimp
ActiveCampaign
Brevo
Klaviyo
Metricool
Publer
Buffer
Hootsuite
WordPress
Webflow
Framer
Typeform
Tally
Jotform
```

#### ERP e financeiro

```text
Omie
Bling
Tiny
Conta Azul
Nibo
QuickBooks
TOTVS
Sankhya
SAP Business One
Oracle NetSuite
Asaas
Iugu
Stripe
Mercado Pago
Pagar.me
PagSeguro
```

#### Gestão

```text
ClickUp
Notion
Airtable
Monday
Trello
Asana
Jira
Linear
Fibery
Coda
```

#### Dados e backend

```text
PostgreSQL
Supabase
BigQuery
Firebase
MySQL
Airtable
Baserow
NocoDB
Redis
S3
Cloudflare R2
MinIO
```

#### BI

```text
Metabase
Looker Studio
Power BI
Tableau
Grafana
Retool
Appsmith
```

### Campos da ferramenta

```text
nome
categoria
setor
status de uso
criticidade
tem API?
tem webhook?
tem exportação?
tipo de autenticação
responsável
dados principais
limitações
integrações desejadas
risco
documentação
```

### Status da ferramenta

```text
Em uso ativo
Usada parcialmente
Abandonada
Crítica
Substituível
Precisa integrar
Precisa auditar
```

---

## Módulo 5: Processos

### Objetivo

Mapear processos atuais e desejados.

### Abas obrigatórias

```text
AS IS
TO BE
AUTOMATIZADO
```

### Campos por etapa do processo

```text
ordem
nome da etapa
responsável
setor
ferramenta usada
tempo médio
entrada
saída
dado usado
dado gerado
problema
risco
observações
```

### Requisitos

* permitir criar fluxo visual;
* permitir fluxo textual;
* permitir associar rotinas;
* permitir associar ferramentas;
* permitir marcar gargalos;
* permitir marcar oportunidades de IA;
* permitir gerar TO BE com IA;
* permitir exportar processo como PDF/Markdown futuramente.

---

## Módulo 6: Rotinas

### Objetivo

Criar catálogo vivo de tarefas repetitivas.

### Campos da rotina

```text
nome
setor
responsável
frequência
tempo por execução
volume mensal
tempo mensal estimado
ferramentas usadas
entrada de dados
saída esperada
pessoas envolvidas
erros comuns
risco se falhar
é repetitiva?
tem regra clara?
usa dado digital?
automatização possível?
IA pode ajudar?
integrações necessárias
economia estimada
prioridade
status
```

### Frequências

```text
Diária
Semanal
Quinzenal
Mensal
Trimestral
Sob demanda
Evento específico
```

### Status

```text
Identificada
Em análise
Automatizável
Não automatizar agora
Em desenho
Em implementação
Ativa
Monitorando
Precisa revisão
```

---

## Módulo 7: Matriz de automação

### Objetivo

Priorizar rotinas por impacto, esforço, risco e ROI.

### Critérios

```text
Frequência
Volume
Tempo gasto
Custo operacional
Erro humano
Impacto no cliente
Impacto no financeiro
Facilidade técnica
Dados disponíveis
Integrações disponíveis
Potencial de IA
Risco
Complexidade
ROI esperado
```

### Escala

Cada critério deve ter nota de 1 a 5.

### Fórmula conceitual

```text
Score de Automação =
(Frequência + Volume + Tempo + Custo + Erro + Impacto + Potencial IA + Viabilidade + ROI)
-
(Risco + Complexidade)
```

### Classificação

```text
80 a 100: P0 - Automatizar primeiro
60 a 79: P1 - Alta prioridade
40 a 59: P2 - Médio prazo
20 a 39: P3 - Baixa prioridade
0 a 19: Não automatizar agora
```

### Requisitos

* permitir ajustar pesos;
* permitir ranking automático;
* permitir visualização impacto x esforço;
* permitir filtro por setor;
* permitir filtro por ferramenta;
* permitir gerar backlog a partir da matriz.

---

## Módulo 8: Integrações

### Objetivo

Planejar conexões entre ferramentas.

### Tipos de integração

```text
API
Webhook
Banco de dados
CSV import/export
Google Sheets
Email parser
RPA/browser automation
Conector nativo
Conector n8n
Script customizado
Manual assistido
```

### Campos

```text
nome
empresa
setor
origem
destino
objeto de dados
gatilho
ação
frequência
middleware
autenticação
credencial
endpoint
payload de entrada
payload de saída
transformação de dados
validação
fallback
logs
erros esperados
responsável
status
risco
documentação
```

### Status

```text
Ideia
Mapeada
Aguardando credenciais
Em desenvolvimento
Em teste
Aprovada
Ativa
Com erro
Pausada
Descontinuada
```

### Requisitos críticos

* não armazenar segredo em texto aberto;
* suportar referência de credencial;
* registrar logs;
* registrar erros;
* permitir checklist de teste;
* marcar se ação exige aprovação humana.

O n8n suporta vários métodos de autenticação em HTTP Request, incluindo Basic, Header, Bearer, OAuth1, OAuth2, Query e Custom Auth, então a plataforma precisa modelar autenticação de forma flexível. ([n8n Docs][6])

---

## Módulo 9: Agentes de IA

### Objetivo

Criar e controlar agentes especializados por área.

### Tipos iniciais

```text
Agente Comercial
Agente de Atendimento
Agente Financeiro
Agente Operacional
Agente RH
Agente Jurídico
Agente Executivo
Agente de BI
Agente de Documentação
Agente de Monitoramento
```

### Campos

```text
nome
objetivo
setor
usuários atendidos
dados que pode ler
ferramentas conectadas
ações permitidas
ações proibidas
modelo de IA
prompt base
base de conhecimento
formato de saída
nível de autonomia
exige aprovação humana?
fallback humano
logs
métricas
status
```

### Níveis de autonomia

```text
Nível 0: Apenas leitura
Nível 1: Sugere ação
Nível 2: Gera rascunho
Nível 3: Executa com aprovação
Nível 4: Executa ações de baixo risco
Nível 5: Autonomia avançada com governança
```

### Regras obrigatórias

* agente financeiro não aprova pagamento sozinho;
* agente jurídico não decide risco legal final;
* agente de atendimento não encerra reclamação crítica sozinho;
* agente comercial não altera contrato sem aprovação;
* agente executivo sugere decisão, mas não executa ação crítica sem humano.

O n8n permite agentes com ferramentas externas e também suporte a revisão humana para tool calls sensíveis, o que combina com a arquitetura de agentes com limites, permissões e aprovação. ([n8n Docs][7])

---

## Módulo 10: Workflows

### Objetivo

Controlar automações reais.

### Campos

```text
nome
rotina relacionada
integrações usadas
agentes usados
gatilho
passos
ferramentas
dados de entrada
dados de saída
ambiente
versão
status
última execução
erros
logs
tempo economizado
documentação
responsável
```

### Status

```text
Rascunho
Em desenvolvimento
Em teste
Homologado
Ativo
Pausado
Erro
Depreciado
```

### Requisitos

* registrar versão;
* registrar ambiente;
* permitir checklist de teste;
* permitir link para n8n;
* permitir link para documentação;
* permitir histórico de execução;
* permitir plano de rollback.

---

## Módulo 11: ROI e economia

### Objetivo

Provar valor financeiro.

### Métricas

```text
horas economizadas por mês
custo/hora médio
economia mensal estimada
economia real
erros reduzidos
tempo de resposta reduzido
leads recuperados
cobranças realizadas
relatórios automatizados
tarefas criadas automaticamente
payback
ROI
```

### Fórmulas

```text
Tempo mensal antes = tempo por execução x volume mensal

Tempo economizado = tempo mensal antes - tempo mensal depois

Economia mensal = horas economizadas x custo/hora médio

ROI = economia gerada / custo da implantação

Payback = custo da implantação / economia mensal
```

### Requisitos

* permitir custo/hora por setor;
* permitir custo/hora por colaborador;
* permitir estimativa antes;
* permitir medição depois;
* permitir comparação estimado x real.

---

## Módulo 12: Backlog

### Objetivo

Transformar diagnóstico em execução.

### Colunas padrão

```text
P0 - Crítico
P1 - Alto impacto
P2 - Médio prazo
P3 - Futuro
Não automatizar agora
Em desenho
Em implementação
Em teste
Ativo
```

### Campos do item

```text
título
rotina relacionada
setor
objetivo
impacto
esforço
risco
economia estimada
ferramentas
integrações
agente IA
responsável
prazo
status
critério de aceite
documentação
```

---

## Módulo 13: Documentação e SOPs

### Objetivo

Gerar documentação padronizada de processos, automações e agentes.

### Tipos de documento

```text
Relatório do diagnóstico
Mapa AS IS
Mapa TO BE
Manual do processo
Manual da automação
Manual do agente de IA
Mapa de dados
Mapa de integração
Checklist de teste
Plano de rollback
Manual do usuário
SOP do setor
Relatório de implantação
```

### Requisitos

* gerar documento por template;
* permitir revisão humana;
* versionar documento;
* associar documento a workflow;
* associar documento a rotina;
* associar documento a integração;
* exportar em Markdown na V1;
* PDF pode entrar na V2.

---

## Módulo 14: Governança e segurança

### Objetivo

Proteger dados, pessoas, clientes e a própria fábrica.

### Requisitos

* controle de permissões;
* papéis por usuário;
* logs de execução;
* trilha de auditoria;
* ações que exigem aprovação;
* classificação de dados sensíveis;
* bloqueio de ações proibidas;
* referência segura a credenciais;
* plano de rollback;
* monitoramento de incidentes;
* governança de prompts;
* governança de agentes;
* avaliação de risco por workflow.

### Papéis iniciais

```text
Admin da fábrica
Consultor
Analista de automação
Especialista de IA
Desenvolvedor
Cliente admin
Cliente gestor
Cliente operador
Visualizador
```

### Ações críticas

```text
Enviar cobrança
Enviar proposta
Enviar contrato
Alterar status financeiro
Excluir dado
Enviar mensagem sensível
Tomar decisão jurídica
Comunicar cliente insatisfeito
Criar usuário
Alterar credencial
Ativar workflow crítico
```

---

## Módulo 15: Monitoramento

### Objetivo

Ver se tudo está funcionando.

### Métricas

```text
workflows ativos
execuções por dia
falhas por workflow
tempo médio de execução
APIs indisponíveis
mensagens não entregues
erros de autenticação
custo de IA
automações pausadas
pendências humanas
incidentes
```

### Alertas

```text
workflow falhou
API retornou erro
credencial expirou
custo de IA subiu
dashboard não atualizou
agente teve baixa confiança
ação humana pendente
integração pausada
```

---

## Módulo 16: Biblioteca da fábrica

### Objetivo

Escalar a operação com templates reutilizáveis.

### Bibliotecas

```text
Rotinas
Integrações
Agentes
Prompts
SOPs
Dashboards
Checklists
Relatórios
Mapas de processo
Pacotes comerciais
```

### Exemplos de rotinas

```text
Cobrança
Follow-up
Atendimento FAQ
Relatório executivo
Onboarding cliente
Onboarding funcionário
Contrato vencendo
Tarefa atrasada
Resumo de reunião
Organização de documentos
```

### Exemplos de integrações

```text
WhatsApp → CRM
Formulário → CRM
CRM → ClickUp
ERP → Cobrança
Drive → Base de conhecimento
E-mail → IA
Reunião → Tarefa
Pagamento → Status cliente
```

---

# 14. Requisitos de UX/UI

## Estilo

* SaaS B2B;
* cockpit operacional;
* limpo;
* denso;
* profissional;
* rápido de navegar;
* com cards, tabelas e filtros;
* visual inspirado em ferramentas como Linear, Retool, ClickUp, HubSpot e dashboards de BI.

## Layout

```text
Sidebar lateral
Topbar com empresa selecionada
Área principal modular
Cards de métricas
Tabelas com filtros
Badges de status
Kanban
Wizard
Fluxos visuais
Dashboards
```

## Menu lateral

```text
Cockpit Geral
Empresas
Diagnóstico
Setores
Processos
Rotinas
Ferramentas
Integrações
Agentes de IA
Workflows
Matriz de Automação
ROI e Economia
Backlog
Testes
Dashboards
Documentação
Governança
Monitoramento
Biblioteca
```

---

# 15. Telas principais

## Tela 1: Cockpit geral

### Componentes

* rotinas mapeadas;
* rotinas automatizáveis;
* automações ativas;
* economia estimada;
* horas economizáveis;
* riscos críticos;
* saúde por setor;
* top 5 rotinas;
* alertas inteligentes;
* próximos passos.

## Tela 2: Empresas

* lista de empresas;
* cards;
* status;
* segmento;
* maturidade;
* economia estimada;
* próxima ação.

## Tela 3: Diagnóstico

* wizard;
* progresso;
* respostas;
* anexos;
* IA para resumir;
* geração de relatório.

## Tela 4: Processos

* abas AS IS, TO BE, AUTOMATIZADO;
* etapas;
* responsáveis;
* ferramentas;
* gargalos;
* riscos.

## Tela 5: Rotinas

* tabela;
* filtros;
* score;
* prioridade;
* potencial de IA;
* potencial de automação;
* economia.

## Tela 6: Ferramentas

* inventário;
* categorias;
* status;
* API;
* webhook;
* autenticação;
* criticidade.

## Tela 7: Integrações

* origem;
* destino;
* gatilho;
* ação;
* middleware;
* risco;
* status;
* documentação.

## Tela 8: Agentes de IA

* agentes por setor;
* permissões;
* ações proibidas;
* modelo;
* base de conhecimento;
* fallback humano.

## Tela 9: Workflows

* automações;
* passos;
* n8n;
* logs;
* erros;
* versão;
* status.

## Tela 10: Matriz de automação

* pontuação;
* impacto x esforço;
* ranking;
* priorização;
* geração de backlog.

## Tela 11: ROI

* horas;
* economia;
* payback;
* ROI;
* impacto por rotina.

## Tela 12: Backlog

* kanban;
* P0/P1/P2/P3;
* status;
* responsável;
* critérios de aceite.

## Tela 13: Documentação

* SOPs;
* manuais;
* templates;
* versões;
* exportação.

## Tela 14: Governança

* permissões;
* dados sensíveis;
* regras de IA;
* aprovações;
* logs.

## Tela 15: Monitoramento

* workflows ativos;
* falhas;
* incidentes;
* custo IA;
* alertas.

## Tela 16: Biblioteca

* templates;
* rotinas;
* agentes;
* prompts;
* dashboards;
* integrações.

---

# 16. Modelo de dados inicial

## Entidades principais

```text
Company
Department
User
Role
Tool
Integration
Process
ProcessStep
Routine
AutomationOpportunity
Workflow
WorkflowStep
AIAgent
Prompt
KnowledgeBase
DataObject
CredentialReference
Dashboard
KPI
Document
TestCase
ExecutionLog
Incident
ROIRecord
BacklogItem
GovernanceRule
ApprovalRequest
```

## Company

```json
{
  "id": "company_001",
  "name": "Cliente X",
  "segment": "Clínica",
  "size": "20-50 funcionários",
  "status": "diagnostico_em_andamento",
  "maturity_score": 48,
  "created_at": "2026-06-03"
}
```

## Department

```json
{
  "id": "dept_001",
  "company_id": "company_001",
  "name": "Financeiro",
  "leader": "Maria",
  "people_count": 3,
  "pain_level": 4,
  "automation_potential": 5
}
```

## Tool

```json
{
  "id": "tool_001",
  "company_id": "company_001",
  "name": "Omie",
  "category": "ERP/Financeiro",
  "status": "ativo",
  "has_api": true,
  "has_webhook": true,
  "risk_level": "medio"
}
```

## Routine

```json
{
  "id": "routine_001",
  "company_id": "company_001",
  "department_id": "dept_001",
  "name": "Cobrança de clientes atrasados",
  "frequency": "diaria",
  "time_per_execution_minutes": 120,
  "monthly_volume": 22,
  "human_error_risk": 4,
  "automation_potential": 5,
  "ai_potential": 4,
  "priority": "P0"
}
```

## AutomationOpportunity

```json
{
  "id": "opp_001",
  "routine_id": "routine_001",
  "impact_score": 5,
  "effort_score": 3,
  "risk_score": 3,
  "roi_score": 5,
  "automation_score": 87,
  "estimated_hours_saved_month": 40,
  "estimated_money_saved_month": 3200,
  "recommendation": "Automatizar primeiro com aprovação humana"
}
```

## Integration

```json
{
  "id": "int_001",
  "source_tool": "Omie",
  "target_tool": "WhatsApp API",
  "trigger": "Pagamento vencido",
  "action": "Enviar mensagem aprovada",
  "middleware": "n8n",
  "status": "em_desenho",
  "requires_human_approval": true
}
```

## AIAgent

```json
{
  "id": "agent_001",
  "name": "Agente Financeiro",
  "department": "Financeiro",
  "permissions": [
    "read_financial_status",
    "generate_message",
    "summarize_history"
  ],
  "forbidden_actions": [
    "approve_payment",
    "delete_record",
    "send_without_approval"
  ],
  "model": "openai_or_claude",
  "status": "em_teste"
}
```

---

# 17. Requisitos de IA

## Capacidades iniciais

A IA deve ajudar a:

* resumir diagnóstico;
* transformar entrevista em rotinas;
* sugerir processos AS IS;
* sugerir processos TO BE;
* classificar rotina por automatização;
* gerar relatório executivo;
* gerar SOP;
* gerar prompt de agente;
* gerar checklist de teste;
* resumir logs;
* sugerir causa de erro;
* criar plano de ação;
* gerar mensagem de cobrança com aprovação humana;
* gerar follow-up;
* resumir reunião;
* classificar lead;
* classificar ticket;
* identificar riscos.

## Saídas estruturadas

Sempre que uma IA gerar dados operacionais, deve retornar formato estruturado.

Exemplo:

```json
{
  "routine_name": "Cobrança de clientes atrasados",
  "department": "Financeiro",
  "automation_potential": 5,
  "ai_potential": 4,
  "risk_level": "medio",
  "requires_human_approval": true,
  "recommended_next_step": "Mapear integração com ERP"
}
```

Structured Outputs e Function Calling são relevantes para esse requisito porque ajudam a conectar modelos a sistemas externos e a exigir argumentos compatíveis com schemas definidos. ([OpenAI Help Center][5])

---

# 18. Requisitos não funcionais

## Performance

* carregamento inicial do cockpit em até 3s em condições normais;
* tabelas com paginação;
* filtros rápidos;
* busca por empresa, rotina, ferramenta e integração;
* processamento assíncrono para relatórios longos.

## Segurança

* autenticação obrigatória;
* papéis e permissões;
* segregação por empresa;
* logs de ações;
* credenciais nunca expostas em texto aberto;
* aprovação humana para ações críticas;
* auditoria de uso de IA;
* classificação de dados sensíveis.

## Escalabilidade

* multiempresa;
* multiusuário;
* módulos independentes;
* templates reutilizáveis;
* futura conexão com n8n API;
* futura conexão com ERPs/CRMs via conectores.

## Disponibilidade

* MVP pode começar simples;
* produção deve ter monitoramento;
* falhas de workflow devem gerar alerta;
* automações críticas precisam de fallback.

## Auditabilidade

* registrar quem criou;
* quem editou;
* quem aprovou;
* qual IA gerou;
* qual prompt foi usado;
* qual dado foi usado;
* quando executou;
* qual resultado.

---

# 19. MVP

## MVP 1: Diagnóstico e venda

Objetivo: vender e organizar a fábrica.

### Inclui

```text
Empresas
Setores
Ferramentas
Processos
Rotinas
Matriz de Automação
ROI estimado
Backlog
Relatório de diagnóstico
Biblioteca básica
```

### Não inclui ainda

```text
Execução real via n8n API
Monitoramento automático
Agentes autônomos
Integrações reais com todos os sistemas
```

## MVP 2: Execução assistida

Objetivo: transformar backlog em implementação.

### Inclui

```text
Integrações
Agentes de IA
Workflows
Documentação
Testes
Checklist de homologação
ROI real
```

## MVP 3: Operação e escala

Objetivo: monitorar e evoluir.

### Inclui

```text
Monitoramento
Logs
Incidentes
Dashboards
Governança avançada
Biblioteca avançada
Conexão real com n8n
```

---

# 20. Roadmap sugerido

## Fase 0: Documento e pesquisa

* PRD;
* pesquisa Perplexity;
* benchmark;
* validação técnica;
* definição de stack.

## Fase 1: Protótipo sem código

* Notion;
* Airtable ou Google Sheets;
* ClickUp;
* n8n para automação de relatório;
* templates de diagnóstico.

## Fase 2: MVP Web

* app web;
* Supabase/PostgreSQL;
* autenticação;
* CRUDs principais;
* diagnóstico;
* matriz;
* backlog;
* relatório.

## Fase 3: IA assistiva

* resumo de diagnóstico;
* geração de relatório;
* sugestão de rotina;
* sugestão de TO BE;
* geração de SOP;
* geração de prompts.

## Fase 4: Workflows e integrações

* cadastro avançado de integração;
* workflow builder textual;
* checklist técnico;
* links com n8n;
* logs manuais ou semi-automáticos.

## Fase 5: Monitoramento real

* n8n API;
* logs de execução;
* alertas;
* incidentes;
* custos de IA;
* saúde dos workflows.

## Fase 6: Produto SaaS

* multiempresa;
* billing;
* permissões avançadas;
* marketplace de templates;
* biblioteca de agentes;
* white-label possível.

---

# 21. Critérios de sucesso

## Produto

* consultor consegue cadastrar empresa e gerar diagnóstico;
* sistema gera ranking de rotinas automatizáveis;
* relatório executivo sai com qualidade vendável;
* backlog é gerado a partir da matriz;
* ROI estimado é compreensível;
* documentação mínima é criada.

## Negócio

* diagnóstico vira proposta;
* proposta vira implantação;
* cliente entende economia;
* fábrica reduz tempo de entrega;
* templates são reutilizados.

## Operação

* menos retrabalho na fábrica;
* menos escopo perdido;
* menos automação feita sem prioridade;
* mais clareza para dev/integrador;
* mais documentação;
* mais segurança.

---

# 22. KPIs

## KPIs de diagnóstico

```text
Número de empresas diagnosticadas
Número de rotinas mapeadas
Número de rotinas automatizáveis
Tempo médio para gerar relatório
Taxa de conversão diagnóstico → proposta
Taxa de conversão proposta → implantação
```

## KPIs de automação

```text
Automações implantadas
Horas economizadas
Economia mensal estimada
Economia mensal real
Falhas por workflow
Tempo médio de resolução de erro
Ações com aprovação humana
Ações bloqueadas por governança
```

## KPIs de IA

```text
Chamadas por agente
Custo por agente
Taxa de aprovação humana
Taxa de rejeição humana
Erros de classificação
Confiança média
Prompts revisados
Incidentes de IA
```

---

# 23. Riscos

## Risco 1: Escopo grande demais

Mitigação: MVP começa com diagnóstico, matriz, ROI, backlog e relatório.

## Risco 2: Cliente quer automatizar processo bagunçado

Mitigação: rotina só vira automação após score e validação.

## Risco 3: IA executa ação sensível errada

Mitigação: níveis de autonomia e aprovação humana.

## Risco 4: Integração sem API

Mitigação: classificar integração como API, webhook, exportação, manual assistido ou RPA.

## Risco 5: Credenciais mal geridas

Mitigação: CredentialReference, nunca secret em texto aberto.

## Risco 6: Produto virar consultoria sem escala

Mitigação: biblioteca de templates, agentes, prompts, SOPs e integrações.

## Risco 7: Métrica de economia inventada

Mitigação: separar estimado, validado e real.

---

# 24. Pacotes comerciais ligados ao produto

## Pacote 1: Raio-X de Rotinas com IA

Entrega:

* diagnóstico;
* mapa de processos;
* matriz de automação;
* ranking de oportunidades;
* relatório executivo;
* roadmap.

## Pacote 2: Automação Essencial

Entrega:

* 3 a 5 rotinas automatizadas;
* n8n;
* integrações básicas;
* documentação;
* dashboard simples.

## Pacote 3: Setor Inteligente

Entrega:

* automação de um setor;
* agente de IA;
* integrações;
* dashboard setorial;
* SOPs;
* monitoramento.

## Pacote 4: Empresa Assistida por IA

Entrega:

* múltiplos setores;
* agentes por área;
* banco central;
* dashboards;
* governança;
* monitoramento;
* evolução mensal.

---

# 25. Perguntas abertas para pesquisa no Perplexity/PerplexKit

Agora vem a parte que você pediu da pesquisa. Aqui está o bloco de perguntas que a gente deve mandar para validar o PRD.

## Pesquisa 1: Benchmark de produto

```text
Pesquise ferramentas, plataformas e metodologias similares à FactoryOS IA: sistemas de process mining, task mining, BPM, RPA, iPaaS, automação com IA, workflow automation, enterprise automation platforms e AI operations platforms. Compare Celonis, UiPath, Microsoft Power Automate, Make, Zapier, n8n, Workato, Tray.io, Retool, Appsmith, ServiceNow, Monday, ClickUp, HubSpot Operations Hub e outras ferramentas relevantes.

Objetivo:
Identificar quais módulos da FactoryOS IA já existem no mercado, quais diferenciais são fortes, quais lacunas podemos explorar, quais features são essenciais para MVP e quais são enterprise demais para a primeira versão.

Entregar:
1. tabela comparativa;
2. funcionalidades comuns;
3. funcionalidades ausentes;
4. oportunidades de diferenciação;
5. riscos competitivos;
6. recomendações para MVP;
7. fontes citadas.
```

## Pesquisa 2: Metodologia de diagnóstico

```text
Pesquise as melhores práticas atuais para diagnóstico de processos empresariais antes de automação com IA. Incluir BPM, BPMN, process mining, task mining, Lean Six Sigma, RPA assessment, automation opportunity discovery e AI readiness assessment.

Objetivo:
Criar a metodologia oficial do Raio-X de Rotinas com IA.

Entregar:
1. etapas recomendadas;
2. perguntas de diagnóstico;
3. critérios para saber se uma rotina é automatizável;
4. critérios de risco;
5. matriz de priorização;
6. exemplos por setor;
7. fontes acadêmicas e oficiais.
```

## Pesquisa 3: Segurança e governança de agentes

```text
Pesquise melhores práticas para governança de agentes de IA conectados a ferramentas empresariais, incluindo human-in-the-loop, logs, permissões, approval gates, tool calling, function calling, structured outputs, RAG, prompt management, model evaluation, auditoria e compliance.

Objetivo:
Criar regras de segurança para agentes da FactoryOS IA.

Entregar:
1. arquitetura recomendada;
2. riscos;
3. padrões de permissão;
4. ações que exigem aprovação humana;
5. logs obrigatórios;
6. política de dados sensíveis;
7. referências oficiais.
```

## Pesquisa 4: Stack técnico

```text
Pesquise a melhor arquitetura técnica para criar um SaaS B2B chamado FactoryOS IA, com módulos de diagnóstico, rotinas, matriz de automação, integrações, agentes de IA, workflows, ROI, documentação e monitoramento.

Considere:
Next.js, React, Supabase/PostgreSQL, Prisma, Drizzle, n8n, Docker, Langfuse, OpenAI, Claude, Gemini, LiteLLM, pgvector, Metabase, GitHub, Cloudflare, Vercel, Railway, Render, Coolify.

Entregar:
1. arquitetura recomendada;
2. banco de dados;
3. autenticação;
4. RBAC;
5. integração com n8n;
6. observabilidade;
7. segurança;
8. trade-offs;
9. stack MVP;
10. stack enterprise.
```

## Pesquisa 5: Modelo comercial

```text
Pesquise modelos comerciais para consultorias, agências e SaaS de automação empresarial com IA. Comparar diagnóstico pago, implantação, setup fee, mensalidade, suporte recorrente, revenue share, pacote por setor, pacote por automação e modelo híbrido SaaS + serviço.

Objetivo:
Definir como vender a FactoryOS IA e a Fábrica de Automação Empresarial com IA.

Entregar:
1. modelos de preço;
2. pacotes;
3. benchmarks;
4. riscos;
5. como apresentar ROI;
6. estrutura de proposta;
7. fontes citadas.
```

---

# 26. Prompt único para Perplexity/PerplexKit

Copia e manda essa marreta lá:

```text
Você é um pesquisador sênior de produto, automação empresarial, BPM, RPA, iPaaS, agentes de IA e SaaS B2B.

Contexto:
Estamos criando a FactoryOS IA, um sistema operacional para uma Fábrica de Automação Empresarial com IA. O produto diagnostica empresas, mapeia processos, identifica rotinas repetitivas, calcula potencial de automação, prioriza por ROI, conecta ferramentas, cria agentes de IA, planeja integrações, controla workflows, gera documentação, mede economia e monitora automações.

A FactoryOS IA não é apenas um app de automação. Ela é um cockpit para consultores e operadores de automação empresarial transformarem empresas comuns em operações conectadas, automatizadas e assistidas por IA.

Módulos planejados:
1. Empresas
2. Diagnóstico
3. Setores
4. Ferramentas
5. Processos AS IS / TO BE / Automatizado
6. Rotinas repetitivas
7. Matriz de automação
8. Integrações
9. Agentes de IA
10. Workflows
11. ROI e economia
12. Backlog
13. Documentação e SOPs
14. Governança e segurança
15. Monitoramento
16. Biblioteca da fábrica

Stack considerada:
n8n, APIs, webhooks, Google Workspace, RD Station, HubSpot, Bitrix24, Pipedrive, Kommo, Omie, Bling, Conta Azul, ClickUp, Notion, Airtable, Supabase/PostgreSQL, Metabase, Looker Studio, OpenAI, Claude, Gemini, Langfuse, LiteLLM, pgvector, Cloudflare, GitHub, Docker.

Quero uma pesquisa profunda e citada sobre:

1. Benchmarks:
Compare FactoryOS IA com Celonis, UiPath, Microsoft Power Automate, Make, Zapier, n8n, Workato, Tray.io, ServiceNow, Retool, Appsmith, ClickUp, Monday, HubSpot Operations Hub e outras plataformas relevantes.

2. Metodologia:
Quais são as melhores práticas para diagnosticar processos antes de automatizar? Incluir BPM, BPMN, process mining, task mining, Lean Six Sigma, RPA assessment e AI readiness assessment.

3. Produto:
Quais módulos são essenciais para MVP? Quais devem ficar para V2/V3? Quais features são críticas para vender valor rápido?

4. IA:
Como desenhar agentes de IA empresariais com segurança? Incluir human-in-the-loop, tool calling, structured outputs, RAG, logs, prompt management, avaliação, fallback humano e ações proibidas.

5. Integrações:
Como plataformas enterprise modelam integrações, credenciais, webhooks, APIs, logs, retries, erros, versionamento e monitoramento?

6. Segurança:
Quais práticas devem existir para RBAC, LGPD, dados sensíveis, auditoria, credenciais e aprovação humana?

7. Modelo comercial:
Quais modelos de precificação fazem sentido para uma fábrica que vende diagnóstico, implantação de automações, setor inteligente e operação assistida por IA?

8. Diferenciação:
Quais oportunidades existem para a FactoryOS IA se diferenciar como uma plataforma que começa pelo diagnóstico de rotinas e só depois vai para automação?

Formato da resposta:
- Resumo executivo
- Tabela comparativa de concorrentes
- Melhores práticas por tema
- Recomendações para MVP
- Recomendações para arquitetura
- Riscos e mitigação
- Oportunidades comerciais
- Perguntas que ainda precisamos responder
- Fontes citadas com links
```

---

# 27. Próximo documento depois deste PRD

Depois da pesquisa, a ordem certa é:

```text
1. PRD V1
2. Pesquisa Perplexity
3. PRD V2 refinado
4. Blueprint técnico
5. Modelo de dados completo
6. Wireframes
7. Prompt para Lovable/v0/Bolt/Claude Code
8. MVP em Notion/Airtable ou app web
9. Primeiro piloto com cliente real
```

---

# 28. Síntese brutal

A FactoryOS IA não é “mais uma plataforma de automação”.

Ela é:

> **um cockpit para descobrir onde uma empresa está sangrando tempo, transformar esse sangue em dados, priorizar o que automatizar, construir fluxos com IA e provar a economia.**

O ouro não está no n8n.
O ouro está no **diagnóstico + priorização + ROI + execução padronizada**.

n8n é motor.
IA é cérebro auxiliar.
PRD é mapa.
Blueprint é engenharia.
A FactoryOS IA é o quartel-general.

Agora a gente tem documento-mãe.
Sem isso, era só um polvo de ferramentas fazendo jazz no escuro. 🐅⚙️

[1]: https://www.omg.org/bpmn/?utm_source=chatgpt.com "Business Process Model & Notation™ (BPMN™) | Object Management Group"
[2]: https://docs.n8n.io/workflows/components/nodes/?utm_source=chatgpt.com "Nodes | n8n Docs"
[3]: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/?utm_source=chatgpt.com "AI Agent node documentation | n8n Docs"
[4]: https://developers.rdstation.com/reference/api-rd-station-doc?utm_source=chatgpt.com "Boas vindas"
[5]: https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com "Function Calling in the OpenAI API | OpenAI Help Center"
[6]: https://docs.n8n.io/integrations/builtin/credentials/httprequest/?utm_source=chatgpt.com "HTTP Request credentials | n8n Docs"
[7]: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent/?utm_source=chatgpt.com "Tools AI Agent node documentation | n8n Docs"
