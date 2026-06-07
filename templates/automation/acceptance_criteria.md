# Critérios de Aceitação — Workflow de Automação

O workflow só pode ser promovido para produção quando cumprir os seguintes critérios:

1. **Gatilho configurado corretamente** — O evento inicial aciona o fluxo de maneira consistente.
2. **Passos completos** — Todos os passos descritos no spec estão implementados e conectados.
3. **Validação de entradas** — O workflow lida graciosamente com entradas ausentes ou inválidas.
4. **Aprovação humana** — Se aplicável, a etapa de aprovação funciona e registra a decisão.
5. **Tratamento de erros** — Erros temporários de API são reprocessados e logs são gerados.
6. **Logs e métricas** — Cada execução registra início, fim, tempo de processamento e erros.
7. **Dry‑run validado** — O workflow foi executado em modo de simulação com dados de teste e produziu o resultado esperado.
8. **Revisão por pares** — O fluxo foi revisado por pelo menos um engenheiro de automação.

Após atender a todos os critérios, solicite aprovação no gate CP‑3 para promover o workflow a produção.