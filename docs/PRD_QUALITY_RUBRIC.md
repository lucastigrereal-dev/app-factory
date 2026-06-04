# PRD_QUALITY_RUBRIC.md

**Versão:** 1.0 | **Data:** 2026‑06‑04

---

## Objetivo

Padronizar e quantificar a qualidade de cada Product Requirements Document (PRD) gerado pelo System Creation OS.  O objetivo do rubrica é oferecer uma métrica objetiva que determine se um PRD está pronto para avançar para as etapas seguintes (blueprint, schema, API).  O gate `PRD QUALITY` utiliza este rubrica para aprovar ou rejeitar PRDs.

## Estrutura da Rubrica (0–100 pontos)

| Categoria | Critério | Pontos Máximos |
|---|---|---|
| **Clareza** | Objetivo em uma frase clara | 5 |
| | Usuário alvo definido (persona ou segmento) | 5 |
| | Problema real descrito sem ambiguidade | 10 |
| **Escopo** | Itens IN (funcionalidades incluídas) com justificativa | 10 |
| | Itens OUT (o que não será feito) explicitados (Anti‑Goals) | 10 |
| **Critérios de Aceite** | Pelo menos três critérios mensuráveis | 10 |
| | Cada critério tem forma de teste/validação | 10 |
| **Riscos** | Pelo menos dois riscos identificados (técnicos, de negócio, de segurança) | 10 |
| | Cada risco possui estratégia de mitigação | 10 |
| **Métricas** | Definição de um KPI principal (ex: leads captados, tempo médio de resposta) | 10 |
| | Método de medição do sucesso da aplicação | 10 |

Para passar no gate, o PRD deve somar **≥ 75 pontos** e nenhuma categoria pode ficar zerada.

## Como Utilizar

1. **Preenchimento:** o `prd‑generator` preenche o PRD seguindo o template oficial, abordando cada seção da rubrica.
2. **Cálculo da nota:** uma rotina (`prd_validator.py`) analisa o PRD e calcula a pontuação de cada item (pode usar uma heurística ou IA auxiliar).  A nota final é a soma das categorias.
3. **Feedback:** se a nota < 75 ou algum item estiver ausente, o PRD retorna para refinamento.  O feedback inclui quais critérios faltaram e sugestões de melhoria.
4. **Aprovação humana:** além da nota, o owner (Lucas) revisa o PRD para aspectos que a automação pode ter perdido (ex: misalignment estratégico).

## Próximos Passos

1. Implementar a classe `PRDQualityScorer` em `src/prd/prd_validator.py` para calcular a pontuação.
2. Integrar a pontuação ao `GATE‑03: PRD QUALITY` para bloquear PRDs abaixo do mínimo.
3. Ajustar o template de PRD (em `templates/prd`) para destacar seções obrigatórias e facilitar o cálculo automático.

---
*Gerado por: Aurora — Perfect Factory V6 | 2026‑06‑04*