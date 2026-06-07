# Skill: kratos-snapshot

**Descrição**

Gera eventos de snapshot do estado do projeto para o Kratos em modo dry-run. Registra métricas de progresso, custos, riscos e aprovações para auditoria futura.

**Quando usar**

Em marcos de projeto: após blueprint, após scaffold, após entregas de grandes funcionalidades ou antes de exportar o pacote final.

**Inputs**

- Informações do projeto: identificador, fase atual, custo acumulado, risco e aprovações.

**Outputs**

- Arquivo JSON ``examples/kratos_snapshot_event.json`` representando o evento de snapshot.

**Ferramentas permitidas**

- JSON para serialização.
- Escrita de arquivo local.

**Ferramentas proibidas**

- Conexão com serviços externos.
- Escrita real em banco de dados.

**Risco**

``R1`` — Geração de arquivo local sem side effect.

**Aprovação humana necessária**

Não para gerar o JSON; sim para envio ao Kratos real.

**Etapas**

1. Montar dicionário de campos obrigatórios (timestamp, project_id, status, risk, costs, approval).
2. Validar contra ``kratos_snapshot.schema.yaml``.
3. Salvar JSON em ``examples/``.

**Gates**

Deve ser validado pelo gate CP‑3 antes de exportar.

**Artefatos gerados**

- ``examples/kratos_snapshot_event.json``

**Testes esperados**

- Schema validation.
- Presença de todos os campos obrigatórios.

**Failure modes**

- Campos ausentes ou inválidos.
- Valores fora dos formatos esperados.

**Exemplo de uso**

```
from skills.kratos_snapshot import generate_snapshot
generate_snapshot(project_id="proj-123", status="blueprint-complete", cost=1234.56, risk="low", approval=True)
```