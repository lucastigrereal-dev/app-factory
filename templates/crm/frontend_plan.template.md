# Plano de Frontend — CRM

Este plano orienta a construção das telas básicas de um CRM utilizando React, Next.js ou tecnologia similar.

## Telas Principais

1. **Dashboard** — Visão geral de métricas (número de contas, oportunidades em cada estágio).
2. **Lista de Contas** — Tabela paginada com filtros por status e segmento.
3. **Detalhe da Conta** — Informações gerais da empresa, lista de contatos e oportunidades relacionadas.
4. **Lista de Oportunidades** — Kanban ou pipeline de vendas mostrando oportunidades por estágio.
5. **Formulários de Criação/Edição** — Permitir adicionar e editar contas, contatos e oportunidades.

## Componentização

* Utilize componentes reutilizáveis para campos de formulário.
* Separe componentes de visualização (cards, tabelas) de containers de dados.

## Navegação

* Use um sistema de rotas (React Router ou Next.js) para navegar entre telas.
* Mantenha breadcrumbs ou navegação lateral para contexto.

## Estado e Dados

* Armazene dados em um ``store`` (ex.: Zustand, Redux) ou use ``React Query`` para buscar dados de uma API.
* Implemente uma camada de API abstraindo requisições ao backend.

## Observações

* Comece com dados mockados para desenvolvimento.
* Adicione tratamento de erros e carregamento.