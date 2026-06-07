# Skill: memory-writeback

**Descrição**

Planeja o writeback de registros de memória (insights, decisões) no Akasha sem executar a operação. Gera planos de escrita que podem ser aprovados e processados por um serviço externo.

**Quando usar**

Ao concluir fases ou projetos que geraram conhecimento que deve ser persistido. Após revisão das lições aprendidas e aprovação do comitê.

**Inputs**

- Lista de ``MissionMemoryRecord`` com insights.
- Configurações de priorização.

**Outputs**

- ``examples/akasha_write_plan.json`` com plano de escrita e ``is_dry_run=True``.

**Ferramentas permitidas**

- JSON para serialização.
- Escrita em ``examples/``.

**Ferramentas proibidas**

- Conexões de rede ou banco.
- Execução de escrita real.

**Risco**

``R1`` — Apenas planejamento sem side effect.

**Aprovação humana necessária**

Sim. O plano deve ser revisto antes de enviar para execução real.

**Etapas**

1. Montar estrutura de plano conforme ``akasha_writeback.schema.yaml``.
2. Preencher metadados dos registros.
3. Marcar ``is_dry_run=True``.
4. Salvar JSON no diretório ``examples/``.
5. Registrar log de criação.

**Gates**

Passar pelo gate CP‑3 antes de qualquer execução real.

**Artefatos gerados**

- ``examples/akasha_write_plan.json``

**Testes esperados**

- Validação do JSON conforme schema.
- Verificação de que ``is_dry_run`` está definido.

**Failure modes**

- Estrutura inválida de ``MissionMemoryRecord``.
- Tentativa de execução real.

**Exemplo de uso**

```
from skills.memory_writeback import generate_write_plan
generate_write_plan(records=[...], output_path="examples/akasha_write_plan.json")
```