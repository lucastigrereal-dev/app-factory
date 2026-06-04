# KRATOS Snapshot Protocol

Este documento define como criar e enviar **snapshots** para o KRATOS, o cockpit onde os usuários visualizam o progresso dos produtos.

## Objetivo

* Padronizar as mensagens de status enviadas ao KRATOS.
* Garantir que o cockpit reflita fielmente o estágio atual do pipeline.
* Minimizar ruído ou inconsistências na interface.

## Estrutura de snapshot

Um snapshot é um resumo do estado atual de uma missão ou produto.  Estrutura sugerida (veja `config/kratos_snapshot.schema.yaml`):

```
{
  "mission_id": "uuid",
  "timestamp": "2026-06-03T12:34:56Z",
  "stage": "Blueprint",
  "status": "In Progress",
  "progress": 0.5,
  "message": "Blueprinting in progress",
  "links": {
    "prd": "https://..."
  }
}
```

### Campos principais

* `mission_id`: Identificador único da missão.
* `timestamp`: Data/hora em UTC.
* `stage`: Etapa atual (Intake, PRD, Blueprint, Schema, API, Frontend, Test, Scaffold, Handoff).
* `status`: `Pending`, `In Progress`, `Completed`, `Failed`.
* `progress`: Valor entre 0 e 1 indicando percentual concluído.
* `message`: Texto livre com o resumo do que está acontecendo.
* `links`: URLs para artefatos ou relatórios relevantes.

## Processo

1. Após cada etapa do pipeline, monte um snapshot baseado nos dados atualizados.
2. Valide o snapshot com `config/kratos_snapshot.schema.yaml`.
3. Em modo `dry_run`, apenas logue o snapshot.  Envie ao KRATOS apenas quando autorizado (R3).
4. O KRATOS atualiza a UI do cockpit ao receber um snapshot.

## Risco

Criar snapshots é **R1**; enviá‑los ao KRATOS é **R3** e requer aprovação humana.