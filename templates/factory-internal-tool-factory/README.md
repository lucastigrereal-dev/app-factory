# Template: Internal Tool Factory

## O que cria
Ferramentas internas: gestão de tarefas, inventário, RH, finanças.

## Quando usar
- Processo interno manual e repetitivo
- Planilha virou bagunça
- Necessidade de controle de acesso
- Automação de aprovações

## Produtos típicos
- Sistema de controle de estoque
- Gestão de tarefas da equipe
- Controle de despesas
- Aprovação de férias

## Stack
- **Frontend:** Next.js + Tailwind
- **Backend:** Supabase (Edge Functions)
- **Database:** PostgreSQL
- **Auth:** Supabase Auth (roles internos)
- **Deploy:** Vercel / Railway

## Riscos
- R1: Ninguém usa a ferramenta (UX ruim)
- R2: Dados sensíveis expostos internamente
- R3: Sem backup = perda de dados
