# Plano de Backend — SaaS MVP

## Tecnologias Sugeridas

* **FastAPI** — Framework web leve e assíncrono.
* **SQLAlchemy** — ORM para gerenciamento de banco de dados.
* **PostgreSQL** — Banco de dados relacional.
* **Alembic** — Migrações de esquema.

## Endpoints Básicos (REST)

* **POST /auth/signup** — Cria um novo usuário.
* **POST /auth/login** — Autentica e retorna um token JWT.
* **GET /user/me** — Retorna dados do usuário autenticado.
* **GET /metrics** — Retorna estatísticas para o dashboard.
* **POST /billing/subscribe** — Cria assinatura (mock no MVP).

## Modelos de Banco

* **User** — id, email, password_hash, created_at.
* **Subscription** — id, user_id, plan, status, start_date, end_date.
* **Metric** — id, user_id, type, value, timestamp.

## Observações

* Durante o MVP, o billing pode ser mockado e salvo localmente.
* Use migrações Alembic para versionar o esquema.
* Proteja endpoints sensíveis com autenticação JWT.