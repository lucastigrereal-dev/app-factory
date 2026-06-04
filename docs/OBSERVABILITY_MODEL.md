# OBSERVABILITY_MODEL.md

**Versão:** 1.0 | **Data:** 2026‑06‑04 | **Autoridade:** APPFACTORY_CONSTITUTION.md

---

## Visão Geral

O System Creation OS produz uma grande quantidade de eventos: entradas de ideias, geração de PRDs, criação de blueprints, validação de schemas, execução de ganchos e handoffs.  Para operar com confiabilidade e permitir debugging eficaz, precisamos de observabilidade estruturada.  Este modelo define o que, quando e como observar, além de como reportar essas informações ao Kratos (cockpit de monitoramento) e aos dashboards de custo/performance.

## Objetivos

1. **Rastreabilidade completa:** permitir que qualquer artefato produzido (arquivo, documento, schema) seja traçado de volta ao evento que o gerou.
2. **Detecção precoce de falhas:** alertar imediatamente ao detectar falhas de gate, violações de risco ou exceções de execução.
3. **Análise de performance:** medir tempo gasto e tokens consumidos por step, para otimizar modelos e pipelines.
4. **Conformidade e auditoria:** registrar todos os eventos significativos para inspeção pós‑mortem e auditorias de segurança.

## Estrutura de Eventos

Cada evento enviado ao Kratos deve ter o seguinte formato (exemplo simplificado):

```json
{
  "event_id": "evt‑20260604‑0001",
  "type": "PRD_CREATED",
  "timestamp": "2026‑06‑04T12:34:56Z",
  "agent": "prd‑generator",
  "wave_id": "wave‑42",
  "input_reference": "idea_intake.json",
  "output_reference": "prd.md",
  "duration_ms": 45000,
  "tokens_used": 15234,
  "model": "Claude‑3‑Sonnet",
  "cost_usd": 0.38,
  "status": "SUCCESS",
  "risk_level": "R1",
  "warnings": []
}
```

Campos importantes:

- **event_id:** identificador único gerado (pode usar `uuid4`) para rastrear.
- **type:** categoria do evento (ex: IDEA_INTAKE, PRD_CREATED, BLUEPRINT_VALIDATED, SCHEMA_SAFE_CHECK, GATE_FAILED).
- **agent:** qual agente/skill executou a ação.
- **wave_id:** identificador da missão/wave do produto; permite agrupar eventos de um mesmo ciclo.
- **duration_ms / tokens_used / cost_usd:** métricas para otimização de latência e custo.
- **risk_level:** nível de risco da ação (R0–R3) conforme `config/risk_policy.yaml`.
- **warnings:** lista de avisos (ex: `PII_detected`, `low_quality_prd`, `schema_overengineering`).

## Integração com Kratos e Langfuse

1. **Kratos Snapshot:** o evento acima é enviado ao `kratos_status.py` para atualização do cockpit.  O snapshot é um resumo do estado atual: wave, progresso, artefatos gerados e bloqueios.
2. **Langfuse/OpenTelemetry:** cada chamada de modelo (Claude, OpenAI) deve ser instrumentada com rastreamento de tokens e latência.  Use `langfuse` ou SDK similar para medir e enviar traces.
3. **Alerts:** para falhas críticas (ex: GATE‑08 falhou), dispare alertas via Slack, e‑mail ou PagerDuty.  O mapeamento de severity → canal é definido em `config/models.yaml`.

## Métricas Sugeridas

| Métrica | Descrição | Frequência | Responsável |
|---|---|---|---|
| `avg_prd_quality_score` | Média do quality score de PRDs gerados por wave | Por missão | prd‑generator | 
| `avg_blueprint_time_ms` | Tempo médio (ms) entre PRD aprovado e blueprint entregue | Por wave | blueprint‑generator |
| `gate_failure_rate` | % de gates que falharam nas últimas 10 execuções | Rolling window | risk_classifier |
| `secret_violation_count` | Número de violações detectadas pelo `no‑secret sentinel` | Por execução | security‑guardian |
| `cost_per_app` | Custo total em USD para gerar um app (incluindo tokens e cloud) | Por handoff | cost_tracking |

## Próximos Passos

1. Implementar instrumentação nos módulos Python usando `OpenTelemetry` para métricas de latência e tokens.
2. Definir e registrar todas as `event_types` em `config/event_taxonomy.yaml` para manter nomenclatura consistente.
3. Criar script de exportação de métricas para painéis externos (Grafana, Datadog ou similar).
4. Estabelecer alertas de severidade alta para falhas em `no‑secret sentinel` e `no‑destructive guard`.

---
*Gerado por: Aurora — Perfect Factory V6 | 2026‑06‑04*