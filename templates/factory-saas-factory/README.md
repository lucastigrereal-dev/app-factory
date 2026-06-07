# Template: SaaS Factory

## O que cria
SaaS multi-tenant: auth, billing, roles, admin, API, webhooks.

## Quando usar
- Produto com múltiplos clientes
- Cobrança recorrente (assinatura)
- Níveis de acesso (admin, user, guest)
- API pública para integrações

## Produtos típicos
- SaaS de agendamento para hotéis
- Plataforma de reviews
- Ferramenta de gestão de redes sociais
- Sistema de reservas

## Stack
- **Frontend:** Next.js 14 + Tailwind + shadcn/ui
- **Backend:** Next.js API Routes + tRPC
- **Database:** PostgreSQL (Supabase)
- **Auth:** NextAuth + Supabase Auth
- **Billing:** Stripe
- **Email:** Resend

## Riscos
- R1: Vazamento de dados entre tenants
- R2: Falha no billing = churn
- R3: Escalabilidade horizontal complexa
