# FILE: .claude/commands/appfactory-export.md

## Objetivo
Gerar o pacote final de entrega (handoff) contendo todos os artefatos
aprovados e prontamente consumíveis por uma equipe de desenvolvimento
humana ou pelos clientes da App Factory.  Este comando consolida a
documentação, esquemas, planos, relatórios de validação e snapshots
em um único pacote organizado.

## Quando usar
Após os artefatos terem sido validados e aprovados em todos os
gates necessários (Fase 2).  A exportação deve ser a última etapa
antes de qualquer desenvolvimento real ou deploy.

## Inputs esperados
* Todos os artefatos aprovados:
  - PRD (`docs/prd.md` ou equivalente)
  - Blueprint (`docs/blueprint.md`)
  - Schema (`schemas/*.json` ou `.sql`)
  - API contract (`config/api_contract.yaml`)
  - Scaffold plan (`docs/scaffold.plan.md`)
  - Test plan (`docs/test_plan.md`)
  - Security review (`docs/security_review.md`)
  - Validation report (`upgrade_reports/VALIDATION_REPORT.md`)
  - AKASHA event (JSON)
  - KRATOS snapshot (JSON)

## Outputs esperados
* `handoff_report.md` — relatório resumido conforme `handoff_report_schema.json`.
* `handoff_package.zip` — zip contendo todos os artefatos acima em
  diretórios padronizados.
* Atualização da memória Akasha e snapshot do Kratos (quando habilitado).

## Paths permitidos
Somente criação de arquivos dentro de `output/` ou `upgrade_reports/`.
Não deve tocar `src/` ou `templates/` durante exportação.

## Risco
**R1–R2** — Exportar artefatos para entrega.  Deve ser executado em
`dry_run=True` primeiro para garantir que nenhum arquivo será sobrescrito.

## Regras de segurança
* Não incluir secrets ou informações sensíveis nos pacotes exportados.
* Verificar que todos os artefatos estejam aprovados nos gates.
* Confirmar `dry_run=True` antes de qualquer zipagem real.
* Avisar se alguma dependência estiver faltando.

## Critérios de aceite
* O handoff package contém todos os arquivos listados, sem duplicações.
* O relatório de handoff segue o JSON schema e inclui artefatos, gates
  passados e pendências.
* A memória Akasha e o snapshot Kratos foram preparados (se aplicável).

## Proibições
* Não enviar pacotes incompletos ou fora do padrão.
* Não executar ações de push ou deploy como parte da exportação.