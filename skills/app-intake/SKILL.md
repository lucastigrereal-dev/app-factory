# Skill: app-intake

**Descrição**

Recebe uma ideia ou problema de negócio e a transforma em um ``MissionPackage`` padronizado. Esta skill é o ponto de entrada do pipeline de criação, garantindo que todas as informações necessárias estejam presentes e estruturadas.

**Quando usar**

No momento em que um cliente ou stakeholder submete um novo pedido de produto ou automação. Antes de qualquer planejamento ou documentação.

**Inputs**

- Texto descritivo da ideia.
- Identificador opcional do cliente.

**Outputs**

- Arquivo JSON ``mission_package.json`` contendo campos padronizados (titulo, descrição, setor, prioridade).

**Ferramentas permitidas**

- Leitura e escrita de arquivos em ``examples/`` e ``docs/``.
- JSON para serialização.

**Ferramentas proibidas**

- Conexões de rede.
- Execução de comandos do sistema.
- Acesso a variáveis de ambiente ou secrets.

**Risco**

``R1`` — Skill básica de transformação sem side effects externos.

**Aprovação humana necessária**

Não. O intake é automático, porém a validação do conteúdo deve ser revisada por um humano posteriormente.

**Etapas**

1. Receber entrada bruta.
2. Aplicar normalização (trim, saneamento).
3. Preencher campos opcionais com ``null`` se ausentes.
4. Salvar JSON no diretório ``examples/``.
5. Registrar log de criação.

**Gates**

Após a execução, passar pelo gate de validação (CP‑0) para garantir que o ``MissionPackage`` atende ao schema.

**Artefatos gerados**

- ``examples/mission_package.json``

**Testes esperados**

- Verificar que campos obrigatórios não estão vazios.
- Validar contra ``mission_package.schema.yaml``.
- Checar se o arquivo é salvo corretamente.

**Failure modes**

- Entrada vazia ou incompleta.
- Permissões de escrita negadas.

**Exemplo de uso**

```
mission = app_intake.run("Precisamos de um sistema de agendamento para clientes", cliente_id="clinica_x")
print(mission["title"])  # Deve imprimir o resumo do problema
```