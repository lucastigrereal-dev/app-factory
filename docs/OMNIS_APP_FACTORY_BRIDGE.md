# OMNIS ↔ App Factory Bridge

Este documento explica como deve funcionar a ponte (bridge) entre o **OMNIS Core** e a **App Factory** (System Creation OS).  Esta integração é conhecida como **WAF‑01**.

## Objetivo

* Permitir que o OMNIS despache missões (mission packages) para a App Factory.
* Retornar work order results ao OMNIS para consumo por outras aplicações.
* Manter a separação de responsabilidades: OMNIS decide; App Factory executa.

## Visão geral

1. **Receber mission package**: O OMNIS envia um `MissionPackage` via API ou mensagem.  O objeto é validado contra `config/mission_package.schema.yaml`.
2. **Registrar mission**: A App Factory persiste o pacote em sua base interna (ou no AKASHA em R3).
3. **Executar pipeline**: A App Factory percorre as etapas (PRD → Blueprint → Schema → API → Frontend → Test → Scaffold → Handoff).
4. **Emitir work order result**: Ao finalizar, a App Factory monta um `WorkOrderResult` (ver `config/work_order_result.schema.yaml`) e retorna ao OMNIS.

## Componentes

* `src/bridge/omnis_bridge.py` — implementa a lógica de integração.  Deve operar em `dry_run` inicialmente.
* `src/events/event_bus.py` — pode ser usado para emitir eventos internos.
* `config/mission_package.schema.yaml` — define o formato das missões recebidas.
* `config/work_order_result.schema.yaml` — define o formato dos resultados entregues.

## Processo

1. **OMNIS** serializa e envia a missão.
2. **App Factory** valida, registra e dispara o pipeline.
3. **App Factory** gera snapshots (CP‑2) e aguarda aprovação para ações R3.
4. **App Factory** envia `WorkOrderResult` de volta ao OMNIS quando concluído.

## Risco

A criação e manipulação de missões em dry‑run é **R1**.  Enviar resultados reais e atualizar a AKASHA é **R3**.