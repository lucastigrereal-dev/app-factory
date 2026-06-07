# SKILL: create-saas-mvp

## Nome
create-saas-mvp

## Descrição
Gera o pacote inicial para um produto SaaS mínimo viável, abordando PRD, blueprint (features básicas), plano de frontend e backend e critérios de aceitação.

## Quando usar
Quando se deseja iniciar rapidamente um SaaS com funcionalidades core (autenticação, billing, CRUD principal).

## Inputs
- Descrição do problema que o SaaS resolve.
- Público‑alvo e personas.
- Funcionalidades principais (ex.: login, assinatura, gerenciamento de recurso).

## Outputs
- PRD em Markdown.
- Blueprint YAML listando as features e stack (frontend/backend).
- Plano de frontend e backend.
- Critérios de aceitação.

## Ferramentas permitidas
- Templates em `/templates/saas`
- Escrita em `/docs` e `/config`

## Ferramentas proibidas
- Implantação de código real.
- Execução de builds ou pacotes.

## Risco
**R1/R2** — Documentação (R1); esboço de scaffolds (R2) sem deploy.

## Aprovação humana necessária
Requer aprovação em CP‑2 antes de gerar o scaffold (R2).

## Etapas
1. Preencher o PRD com visão, problema, solução e métricas.
2. Adaptar `product_blueprint.yaml` definindo tecnologias (Next.js, Supabase) e módulos.
3. Criar planos de frontend e backend (dois arquivos).
4. Definir critérios de aceitação.

## Gates
- CP‑1: Aprovação do PRD e blueprint.
- CP‑2: Aprovação dos planos e critérios.

## Artefatos gerados
- `/docs/saas_PRD.md`
- `/templates/saas/product_blueprint.yaml` adaptado
- `/docs/saas_frontend_plan.md`
- `/docs/saas_backend_plan.md`
- `/docs/saas_acceptance_criteria.md`

## Testes esperados
- Validação do blueprint YAML.
- Revisão manual do PRD.

## Failure modes
- Escopo muito amplo para um MVP.
- Tecnologia incompatível com requisitos.
- Critérios de aceite inalcançáveis.

## Exemplo de uso
Solicitar: “crie um MVP SaaS para gerenciamento de tarefas com login e pagamento recorrente”.