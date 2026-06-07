# Skill: validation-gate-runner

**Descrição**

Executa gates de validação (CP‑0 a CP‑3) conforme definidos em ``docs/VALIDATION_GATES.md``. Avalia se cada artefato atende aos critérios mínimos antes de avançar no pipeline.

**Quando usar**

A cada transição de fase — intake → PRD, PRD → blueprint, blueprint → scaffold, scaffold → export. Garantir qualidade e conformidade evita retrabalho.

**Inputs**

- Artefato a ser validado (MissionPackage, PRD, blueprint, scaffold).
- Identificador do gate (CP‑0, CP‑1, CP‑2, CP‑3).

**Outputs**

- ``docs/validation_report.md`` atualizado com o resultado de cada gate.
- Indicação de aprovação ou rejeição.

**Ferramentas permitidas**

- Execução de testes unitários via ``pytest``.
- Validação de schemas YAML/JSON.

**Ferramentas proibidas**

- Alteração dos artefatos validados.
- Execução de código externo.

**Risco**

``R1`` — Apenas leitura, validação e geração de relatório.

**Aprovação humana necessária**

Não para rodar; sim para decidir se avança em caso de dúvidas.

**Etapas**

1. Selecionar gate e artefato.
2. Carregar critérios do gate.
3. Executar testes e validações correspondentes.
4. Registrar resultado no relatório.
5. Retornar status aprovado/reprovado.

**Gates**

CP‑0: Validação do intake → checa JSON e campos.
CP‑1: Validação do PRD → checa seções obrigatórias.
CP‑2: Validação do blueprint → valida módulos e dependências.
CP‑3: Validação do scaffold → verifica estrutura de arquivos e presença de docstrings.

**Artefatos gerados**

- ``docs/validation_report.md``

**Testes esperados**

- Relatório deve conter status PASS/FAIL por critério.

**Failure modes**

- Gate incorreto selecionado para o artefato.
- Falha na leitura de schemas ou arquivos.

**Exemplo de uso**

```
from skills.validation_gate_runner import run_gate
run_gate("CP-1", artifact_path="docs/PRD.md")
```