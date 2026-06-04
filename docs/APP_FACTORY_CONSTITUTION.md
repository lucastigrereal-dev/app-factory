# Constituição da App Factory
> Leis invioláveis da forja

## Lei 1: Dry-run é padrão
**Nenhuma skill executa em produção sem dry-run explícito desativado.**
- Default: `--dry-run=true`
- Produção requer aprovação do operador
- Violacão = bloqueio automático

## Lei 2: Checkpoints são obrigatórios
**Nenhum estado avança sem checkpoint aprovado.**
- CP-0 a CP-15: cada transição tem gate
- Checkpoint falso = pipeline corrompido
- Reversão obrigatória em checkpoint inválido

## Lei 3: Schema/API = sequencial
**Mudanças em schema ou contrato de API nunca rodam em paralelo.**
- Shared src/ = HIGH RISK
- Schema changes bloqueiam pipeline até aprovação
- API contract changes bloqueiam consumers

## Lei 4: R3 = aprovação humana
**Risco R3 sempre requer confirmação explícita do operador.**
- Nenhuma automação supera R3
- Sem confirmação = pipeline pausado
- Timeout de 24h = cancelamento

## Lei 5: Toda skill termina com next_action
**Toda skill, agente e subagente retorna `next_action`.**
- Sem next_action = execução incompleta
- Next_action vago = rejeitado
- Sempre próximo passo concreto

## Lei 6: Memory-write é obrigatório
**Toda missão termina com persistência no Akasha + snapshot no Kratos.**
- Sem persistência = missão não existe
- Akasha = fonte única de verdade
- Kratos = estado operacional

## Lei 7: Nenhuma factory substitui outra
**App Factory cria fábricas, não substitui as existentes.**
- Automation Factory complementa, não elimina
- Marketing Factory amplia, não remove
- Content Factory acelera, não substitui Publisher OS

## Lei 8: Documentação vive com código
**Toda mudança em skill/template/squad atualiza documentação.**
- Sem docs = não mergeia
- README primeiro, código depois
- Constituição só menda por votação do operador
