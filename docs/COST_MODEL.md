# COST_MODEL.md

**Versão:** 1.0 | **Data:** 2026‑06‑04 | **Autoridade:** APPFACTORY_CONSTITUTION.md

---

## Visão Geral

Nenhum sistema enterprise está completo sem medir e otimizar o custo de suas operações.  O System Creation OS consome recursos de computação, tokens de modelos proprietários, tempo de agentes e eventualmente serviços cloud (deploy, banco de dados, armazenamento).  Este modelo define como estimar, registrar e controlar o custo de cada etapa do pipeline de geração de aplicativos.

## Componentes de Custo

1. **Tokens de LLM:** cada chamada para Claude, GPT ou outro modelo tem um custo proporcional ao número de tokens.  Devemos capturar tokens usados e multiplicar pelo preço unitário para estimar o custo.
2. **Tempo de Execução:** processamentos longos consomem CPU e memória; em ambientes serverless (ex: Vercel, Replit) isso se traduz em custos.  Registrar `duration_ms` por step permite estimar valor nas faturas.
3. **Armazenamento:** artefatos gerados (PRDs, blueprints, schemas, código) ocupam espaço.  Monitorar tamanho dos artefatos para prever crescimento.
4. **Serviços Externos:** APIs de análise de código, RAG, busca, etc., podem ter custo por requisição.  Devem ser catalogadas em `config/models.yaml` com preço unitário.
5. **Mão de Obra Humana:** se um gate exige aprovação manual (R2 ou R3), estimar horas humanas usadas no processo para calcular TCO.

## Métrica Principal

`cost_per_app` — soma de todos os custos acima para uma ideia transformar‑se em handoff pronto, dividido pelo número de apps gerados.

## Registro de Custo

Cada evento de execução (vide `OBSERVABILITY_MODEL.md`) deve incluir:

```json
{
  "tokens_used": 15234,
  "duration_ms": 45000,
  "model": "Claude‑3‑Sonnet",
  "cost_usd": 0.38
}
```

Os componentes de custo são agregados por `wave_id` e por `app_type`.  O módulo `src/cost_tracking/cost_tracker.py` (a ser criado) consolida esses dados e gera relatórios periódicos (por exemplo, por semana ou por release).  Os relatórios alimentam o Kratos e podem ser exportados para planilhas ou dashboards.

## Estimativas Iniciais (exemplo fictício)

| Etapa | Tokens (média) | Custo (USD) | Duração (ms) |
|---|---|---|---|
| Ideia → Discovery | 5 000 | $0.10 | 10 000 |
| Discovery → PRD | 8 000 | $0.16 | 20 000 |
| PRD → Blueprint | 12 000 | $0.24 | 30 000 |
| Blueprint → Schema | 2 000 | $0.04 | 5 000 |
| Schema → API Contract | 3 000 | $0.06 | 8 000 |
| Blueprint → Scaffold Plan | 7 000 | $0.14 | 15 000 |
| **Total (média)** | 37 000 | **$0.74** | 88 000 |

*Observação:* valores ilustrativos; devem ser calibrados com dados reais durante a fase beta.

## Otimização de Custo

1. **Escolha de Modelos:** usar modelos menores (e.g., Claude Opus → Sonnet → Haiku) quando a tarefa não precisa de alta criatividade.  Configurado em `config/models.yaml`.
2. **Cache e Reutilização:** armazenar respostas de pesquisas ou funções intensivas e reusar nas fases seguintes para economizar tokens.
3. **Paralelização Inteligente:** executar etapas que não dependem umas das outras em paralelo reduz tempo total e, em ambientes serverless, custo de espera.
4. **Monitoramento Contínuo:** KRATOS e `cost_tracker.py` devem alertar quando o custo por app ultrapassar limites definidos.

## Próximos Passos

1. Criar o módulo `src/cost_tracking/cost_tracker.py` com funções para agregar tokens e duração, calcular custo estimado e gerar relatório.
2. Adicionar suporte a múltiplos provedores de LLM, cada um com preço unitário, em `config/models.yaml`.
3. Definir limites de custo (`budget_per_app`) que disparam alertas quando excedidos.

---
*Gerado por: Aurora — Perfect Factory V6 | 2026‑06‑04*