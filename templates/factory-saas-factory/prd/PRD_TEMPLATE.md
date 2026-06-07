# PRD — SaaS Factory

## Visão
SaaS de [FUNÇÃO] para [NÍCH] com planos [FREE/PRO/ENTERPRISE].

## Problema
[Processo manual, escala limitada, falta de ferramenta dedicada]

## Solução
- Multi-tenant: isolamento por cliente
- Auth: roles e permissões
- Billing: assinatura recorrente
- API: integrações externas
- Admin: gestão de tenants

## Requisitos
| ID | Requisito | Prio |
|---|---|---|
| SAAS-1 | Cadastro e login | P0 |
| SAAS-2 | Isolamento de dados | P0 |
| SAAS-3 | Planos e billing | P0 |
| SAAS-4 | Painel admin | P1 |
| SAAS-5 | API pública | P2 |

## Aceite
- [ ] Tenant A não vê dados do Tenant B
- [ ] Stripe cobra recorrente
- [ ] Admin gerencia usuários
- [ ] API documentada (OpenAPI)
