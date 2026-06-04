# Especificação de Workflow de Automação

## 1. Visão Geral

Descreva brevemente o objetivo da automação e o benefício esperado (redução de tempo, aumento de precisão, etc.).

## 2. Gatilho (Trigger)

Explique o evento que inicia a automação. Exemplos: criação de tarefa, recebimento de email, atualização em planilha.

## 3. Variáveis de Entrada

Liste e descreva todas as variáveis que o workflow recebe. Indique se são obrigatórias ou opcionais.

## 4. Passos do Workflow

### 4.1 Passo 1 — Nome do passo

* **Descrição:** o que este passo faz.
* **Ferramentas:** API ou serviço usado (por ex., ClickUp, Notion, CRM).
* **Campos de entrada:** variáveis utilizadas.
* **Campos de saída:** resultados gerados.

Repita subseções para cada passo adicional.

## 5. Lógica de Decisão

Descreva condicionais ou bifurcações no fluxo (ex.: se resposta de API for X, fazer Y; senão, fazer Z).

## 6. Aprovação Humana (Opcional)

Indique se há algum ponto em que um humano deve aprovar antes de prosseguir. Explique critérios e como a aprovação é solicitada (ex.: notificação via Slack).

## 7. Manejo de Erros

Defina como o workflow lida com falhas em APIs, dados inválidos ou tempo limite. Inclua estratégias de retry ou escalonamento.

## 8. Log e Monitoramento

Liste os eventos que serão registrados para auditoria e diagnóstico (ex.: início, fim, erros).

## 9. Resultados Esperados

Descreva o que constitui uma execução bem-sucedida e quais métricas serão coletadas (tempo de execução, itens processados, etc.).