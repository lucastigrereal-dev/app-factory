# AKASHA Writeback Protocol

Este documento descreve o protocolo para registrar eventos e resultados de projetos de volta na **AKASHA**, o sistema de memória persistente do OMNISVERSO.

## Objetivo

* Normalizar o formato dos eventos de writeback enviados à AKASHA.
* Garantir que toda criação (missão, pacote, work order) seja persistida de forma auditável.
* Facilitar a ingestão de dados pela AKASHA sem perda de contexto.

## Estrutura de evento

Um evento de writeback deve ter a seguinte estrutura mínima (veja `config/akasha_writeback.schema.yaml` para o schema completo):

```
{
  "id": "uuid",
  "timestamp": "2026-06-03T12:34:56Z",
  "source": "app-factory",
  "type": "work_order_completed",
  "payload": {
    "work_order_id": "abc123",
    "status": "completed",
    "summary": "Descrição breve do resultado",
    "files": ["gs://bucket/report.md"]
  }
}
```

### Campos principais

* `id`: Identificador único do evento.
* `timestamp`: Data/hora ISO 8601 em UTC.
* `source`: Identifica o componente emissor (ex.: `app-factory`).
* `type`: Tipo do evento (`mission_created`, `work_order_completed`, etc.).
* `payload`: Objeto específico de cada tipo de evento, contendo IDs e dados relevantes.

## Processo de writeback

1. Ao concluir uma etapa significativa (ex.: handoff), reúna todos os dados relevantes (IDs, relatórios, links de arquivos).
2. Monte um objeto conforme o schema e verifique validade com `config/akasha_writeback.schema.yaml`.
3. Em modo `dry_run`, logue o evento; quando autorizado (CP‑3), emita o evento real para o endpoint da AKASHA via HTTPS.
4. Armazene a resposta da AKASHA em logs para auditoria.

## Risco

Emitir eventos reais é uma ação de **R3** e requer aprovação humana.  O desenvolvimento e validação em dry‑run é **R1**.