# Product Requirements Document (PRD)

## Título
**FactoryOS IA — Evolução Exponencial**

## Objetivo
Entregar uma plataforma de automação empresarial capaz de mapear rotinas, arquitetar processos e construir integrações de ponta a ponta de forma semi‑autônoma. O sistema deve receber o contexto de uma empresa (setor, tamanho, ferramentas, gargalos) e propor automações com base em conhecimento acumulado, gerar blueprint técnico, construir e publicar workflows n8n, além de monitorar e se auto‑reparar quando houver falhas.

## Visão
Empresas brasileiras de pequeno e médio porte gastam tempo e dinheiro com processos manuais e uso de múltiplas ferramentas desconectadas. A FactoryOS IA propõe uma abordagem consultiva automatizada: entrevistando a empresa, identificando oportunidades de automação, priorizando por ROI e criando as integrações necessárias. O consultor se torna um supervisor, não um executor.

## Problema
1. Falta de organização e prioridade em oportunidades de automação;\
2. Necessidade de especialistas para desenhar integrações e fluxos;\
3. Manutenção manual de workflows quando APIs mudam ou falham;\
4. Ausência de aprendizado entre clientes semelhantes;\
5. Difícil acompanhar custos e resultados de automações.

## Usuário Alvo
Consultores de automação (usuários avançados) e donos de pequenas e médias empresas que desejam automatizar tarefas repetitivas. A plataforma deve disponibilizar uma interface amigável para o empresário monitorar resultados enquanto fornece um ambiente técnico robusto para o consultor.

## Metas e Métricas de Sucesso

| Métrica                       | Meta                                             |
|-------------------------------|--------------------------------------------------|
| Tempo de onboarding           | < 2 horas para novo cliente                      |
| Taxa de self‑healing          | > 80 % de erros transitórios resolvidos         |
| Custo mensal por cliente      | < R$ 50 em uso de IA                             |
| NPS do consultor              | > 70                                             |
| Automação implantada          | ≥ 3 rotinas automatizadas por cliente em 1 mês   |

## Escopo

### Incluído (Scope In)

- Discovery conversacional (entrevista guiada).\
- Classificação de processos e priorização por ROI.\
- Geração de blueprint com DB schema, API contracts e planos de frontend/back‑end.\
- Construção de workflows n8n para integrações (WhatsApp, CRM, ERP etc.).\
- Camada de memória (episódica, semântica e procedural) compartilhada entre clientes.\
- Orquestração multi‑agente com LangGraph.\
- Self‑healing (circuit breaker, retry, dead letter queue, recovery agent).\
- Event bus com Redis Streams para acoplar agentes de forma assíncrona.\
- Painel de custos e métricas por cliente.\
- Gate de aprovação humana em ações sensíveis.

### Excluído (Scope Out)

- Execução de deploy em produção sem staging aprovado.\
- Suporte a todas as integrações existentes — inicialmente, integrações BR prioritárias (Z‑API, Omie, RD Station, Google Workspace).\
- Desenvolvimento de UX customizado para cada cliente; a plataforma fornecerá interfaces padrão.\
- Automação de tarefas que exijam intervenção humana obrigatória (ex.: análise jurídica).

## Requisitos Funcionais

1. **Entrevista Inteligente:** O sistema deve conduzir conversa com o cliente para coletar dados (setor, tamanho, ferramentas, processos, problemas).\
2. **Mapeamento Automatizado:** A partir da entrevista, gerar relatório de oportunidades de automação com impacto, dificuldade e ROI estimado.\
3. **Blueprint Generator:** Criar blueprint técnico contendo fluxos de dados, schema, API contracts e planos de implementação.\
4. **Workflow Builder:** Produzir arquivos de workflow n8n (JSON) prontos para importação, baseando‑se em templates e casos anteriores.\
5. **Self‑healing:** Detectar falhas nos workflows e acionar recovery agent para corrigir ou reenfileirar tarefas.\
6. **Memory Layer:** Persistir conhecimento de casos de sucesso e falhas em memória vetorial para consulta futura.\
7. **Cost Tracking:** Registrar tokens, custo estimado e tempo por etapa para cada cliente e workflow.\
8. **Human Approval:** Solicitar aprovação via interface ou notificação quando uma ação com risco R2 ou R3 for identificada.\
9. **Audit Log:** Registrar todas as ações executadas, decisões e mudanças de estado para auditoria e LGPD.\
10. **Dashboard de Resultados:** Permitir ao usuário acompanhar métricas de automação (tempo economizado, ROI, status das integrações).

## Critérios de Aceite (Acceptance Criteria)

- **AC‑01:** Para cada cliente novo, a plataforma grava pelo menos 8 respostas da entrevista e produz relatório de oportunidades em menos de 5 minutos.\
- **AC‑02:** Para cada oportunidade de automação aprovada, a plataforma gera blueprint com pelo menos 5 seções: DB schema (ou None se não aplicável), API contract, fluxograma, plano de backend e plano de frontend.\
- **AC‑03:** A geração de workflows cria arquivos JSON válidos que podem ser importados e executados no n8n em um ambiente de staging.\
- **AC‑04:** O sistema detecta e se recupera automaticamente de falhas transitórias (ex.: HTTP 503) sem intervenção humana, e registra caso na Dead Letter Queue quando não consegue resolver.\
- **AC‑05:** Toda ação marcada como crítica (ex.: deletar dados, modificar permissões, deploy) exige aprovação explícita do proprietário.\
- **AC‑06:** O painel de custo exibe tokens e estimativa em reais para cada workflow executado.\
- **AC‑07:** O sistema registra todas as ações executadas (audit logs) e permite consulta por organização.\
- **AC‑08:** A taxa de self‑healing em ambiente de staging deve ser maior que 80 % nos testes de integração.

## Riscos e Mitigações

| Risco                       | Severidade | Mitigação                                                   |
|-----------------------------|------------|-------------------------------------------------------------|
| Falhas de integrações       | Alta       | Circuit Breaker + Retry + Dead Letter Queue                 |
| Ingestão de dados sensíveis | Alta       | Política de PII no DB schema; encriptação de campos        |
| Drift de stack              | Média      | Definir matriz de stack e atualizar templates periodicamente |
| Custo elevado de IA         | Média      | Usar LLMs de menor custo para tarefas simples; caching      |
| Dependência do consultor    | Baixa      | Interface simples com aprovador para clientes finais        |
| Compliance LGPD             | Média      | RLS por empresa; consentimento do cliente                   |

## Aprovação

Este PRD requer aprovação de Lucas Tigre (Product Owner) antes de iniciar a próxima etapa (Blueprint).