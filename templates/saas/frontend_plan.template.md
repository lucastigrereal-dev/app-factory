# Plano de Frontend — SaaS MVP

## Estrutura de Páginas

1. **Home/Dashboard** — Resumo com métricas e atalhos.
2. **Sign Up / Login** — Telas para registro e autenticação de usuários.
3. **Plans** — Página apresentando opções de assinatura.
4. **Billing** — Tela para inserir dados de pagamento (mock durante MVP).
5. **Profile/Settings** — Permite ao usuário alterar informações básicas e cancelar a assinatura.

## Tecnologias Sugeridas

* **Next.js** para renderização híbrida (SSR + CSR).
* **Tailwind CSS** para estilização rápida.
* **Supabase** para autenticação pronta.

## Fluxo de Navegação

* Usuário anônimo acessa Home → é direcionado para cadastro.
* Após login, é redirecionado ao Dashboard.
* O menu inclui links para Plans, Billing e Profile.

## Observações

* Utilize componentes reutilizáveis para formulários.
* Mantenha o design responsivo.
* Implemente feedback visual para ações do usuário (spinners, toasts).