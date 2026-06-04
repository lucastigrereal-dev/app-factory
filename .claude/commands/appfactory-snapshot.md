# Command: appfactory-snapshot

**Objetivo**

Registrar um snapshot de status no **Kratos** para auditoria e histórico. Esse comando coleta indicadores de progresso, custos, riscos e aprovações e gera um evento de snapshot, sem enviar dados para o Kratos real (modo dry-run).

**Quando usar**

Em marcos importantes: conclusão de fases (Blueprint, Scaffold, Release), geração de relatórios ou antes de entregar o produto. Cada snapshot facilita comparações futuras e auditoria de mudanças.

**Entradas esperadas**

- Informações estruturadas do projeto (status, custos, risco, aprovação).

**Saídas esperadas**

- Arquivo ``kratos_snapshot_event.json`` em ``examples/`` contendo evento de snapshot pronto para envio.

**Paths permitidos**

- Escrita em ``examples/kratos_snapshot_event.json``.

**Risco**

``R1`` — Geração de artefatos locais sem comunicação externa.

**Regras de segurança**

1. Não incluir dados sensíveis ou identificadores pessoais no snapshot.
2. ``dry_run`` deve ser ``True``; nenhum envio real.
3. Verificar se ``kratos_snapshot.schema.yaml`` valida o JSON gerado.

**Critérios de aceite**

- Evento contém campos: ``timestamp``, ``project_id``, ``status``, ``risk``, ``costs`` e ``approval``.
- Validação contra o schema do snapshot passa.

**Proibições**

- Não abrir conexão com Kratos real.
- Não gravar em banco de dados.