# DB Schema Guidelines

Este documento descreve as linhas gerais para planejar e documentar o **schema de banco de dados** de produtos construídos com o System Creation OS.

## Objetivo

* Garantir que todos os objetos persistentes (tabelas, colunas, relacionamentos) estejam claramente definidos e versionados.
* Minimizar riscos de corrupção de dados, vazamento de informações sensíveis ou inconsistências.
* Facilitar a geração automática de migrações e scaffolding.

## Princípios

1. **Normalização**: Estruture dados de forma a evitar duplicações; utilize chaves estrangeiras para relacionamentos.
2. **Tipos explícitos**: Defina tipos e tamanhos de campo com clareza (`VARCHAR(255)`, `INTEGER`, `TIMESTAMP WITH TIME ZONE`).
3. **Sem segredos**: Nunca armazene chaves de API, tokens, senhas ou segredos em texto plano.  Use cofres de segredo ou tabelas criptografadas.
4. **Controle de acesso**: Separe dados sensíveis em tabelas com políticas de acesso restritivas; utilize RLS (Row Level Security) em Supabase/Postgres.
5. **Versionamento**: Cada versão do schema deve ser rastreável.  Use scripts de migração ou ferramentas como Alembic.

## Processo

1. A partir do PRD e blueprint, identifique entidades de domínio (empresa, rotina, usuário, etc.).
2. Crie diagramas ER (mermaid ou outra ferramenta) para visualizar relações.
3. Defina o schema no diretório `config/` como um arquivo YAML ou SQL template.
4. Submeta o schema para revisão (CP‑1).  Somente após aprovação deve ser aplicado em um ambiente de teste.

## Exemplos

Consulte `config/mission_package.schema.yaml` como exemplo simples de definição.  A documentação do Supabase é um bom recurso para definir chaves estrangeiras e políticas RLS.

## Risco

Este é um documento de nível **R0**.  A criação de schemas no diretório `config/` é **R1**.