# Command: appfactory-writeback

**Objetivo**

Planejar e registrar eventos de escrita de memória (Akasha) sem executá-los. O comando de writeback avalia quais aprendizados devem ser persistidos em memória de longo prazo e prepara pacotes de writeback que podem ser aprovados manualmente e executados por outro serviço.

**Quando usar**

Após concluir um projeto ou automação, quando há lições aprendidas, decisões ou artefatos que devem ser registrados de forma durável no Akasha.

**Entradas esperadas**

- Lista de ``MissionMemoryRecord`` contendo insights e decisões.
- Parâmetros de priorização (setor, relevância, formato).

**Saídas esperadas**

- Arquivo ``akasha_write_plan.json`` em ``examples/`` contendo plano de writeback (dry_run).

**Paths permitidos**

- Leitura de diretórios de documentação e configurações.
- Escrita em ``examples/akasha_write_plan.json``.

**Risco**

``R1`` — Criação de plano de escrita sem execução real.

**Regras de segurança**

1. Nunca executar a escrita real — ``is_dry_run`` deve permanecer ``True``.
2. Não incluir nenhum dado sensível no plano (ex. segredos, credenciais).
3. Nenhum acesso à rede ou banco de dados.

**Critérios de aceite**

- O plano contém listas de registros com metadados (sector, relevance, action).
- ``is_dry_run`` marcado como ``True``.

**Proibições**

- Não modificar arquivos fora de ``examples/``.
- Não abrir conexões a serviços externos.