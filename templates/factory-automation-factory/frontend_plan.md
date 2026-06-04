# Frontend Plan — Automation Factory

## Interface
- **Dashboard n8n:** Interface nativa para monitorar fluxos
- **Painel de status:** Simples HTML/JS embedado ou iframe do n8n
- **Relatórios:** PDF/email automático (sem UI dedicada)

## Componentes
| Componente | Tipo | Tecnologia |
|---|---|---|
| Dashboard | External | n8n native |
| Status widget | Embed | HTML + CSS |
| Log viewer | Embed | n8n executions |

## UX
- Zero código para operação diária
- Logs acessíveis em 2 clicks
- Alertas visuais no status widget

## Acessibilidade
- Cores semânticas (verde=ok, vermelho=erro)
- Contraste mínimo 4.5:1
