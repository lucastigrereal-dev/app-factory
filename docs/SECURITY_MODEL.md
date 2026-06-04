# SECURITY_MODEL.md

**Versão:** 1.0 | **Data:** 2026‑06‑04 | **Autoridade:** APPFACTORY_CONSTITUTION.md

---

## Visão Geral

A segurança é um pilar não negociável do System Creation OS.  Esta fábrica de apps opera sobre dados sensíveis de clientes e fornece artefatos que podem ser incorporados em ambientes corporativos.  Este documento define os princípios, camadas e controles necessários para reduzir riscos de exposição de dados, execuções destrutivas e violações de conformidade.  Ele complementa a `SECURITY_POLICY.md` — que cobre governança e contratos — com uma visão técnica aplicável ao código, às automações e aos agentes.

## Princípios

1. **Defesa em profundidade:** múltiplos controles independentes (gates, sentinelas, revisões humanas) protegem cada etapa do pipeline.
2. **Menor privilégio:** cada agente ou skill só possui permissões estritamente necessárias para executar sua função, com ferramentas proibidas explicitamente documentadas.
3. **Imutabilidade operacional:** nenhum arquivo ou recurso pode ser sobrescrito ou deletado sem backup lógico e aprovação humana (`NO‑DESTRUCTIVE GUARD`).
4. **Zero secret tolerance:** nenhum token, chave privada ou valor sensível deve aparecer em arquivos, logs ou artefatos.  O `NO‑SECRET SENTINEL` bloqueia a criação de tais arquivos.
5. **Auditoria contínua:** toda execução gera rastros auditáveis (logs, eventos, snapshots) e cada decisão é registrada em Akasha ou Kratos para investigação posterior.

## Camadas de Controles

### 1. Controles de Entrada

- **Schema Validation**: ideias e PRDs são validados contra schemas JSON para garantir que campos obrigatórios estão presentes e no formato correto.  Inputs inválidos não avançam.
- **Gates de Qualidade:** `IDEA INTAKE`, `PRD QUALITY` e `BLUEPRINT COHERENCE` garantem que informações incompletas não sejam processadas.

### 2. Controles de Processamento

- **No‑Secret Sentinel** (`GATE‑08`): usa ferramentas de detecção de segredos (inspirado em GitGuardian, Gitleaks, TruffleHog) para impedir a criação de arquivos que contenham `.env`, chaves de API, tokens ou senhas.  Em caso de violação, o gate falha com bloqueio absoluto (`R3`).
- **No‑Destructive Guard** (`GATE‑09`): impede ações de `DELETE`, `DROP TABLE`, sobrescrita de arquivos existentes ou qualquer operação de git que adicione tudo (`git add -A`).  Esse guard ativa `dry_run` por padrão em todas as operações de risco `R2` ou `R3`.
- **Security Review Gate** (`GATE‑11`): todos os API contracts, schemas e blueprints passam por uma checklist automática baseada no OWASP Top 10.  Pontos como injeção de SQL, autenticação, autorização, rate limiting e exposure de dados são verificados.  Um agente `security‑guardian` revisa e aprova ou rejeita.

### 3. Controles de Saída

- **Handoff Completo**: o `GATE‑12` exige que cada entrega final inclua um relatório de handoff e eventos de memória (Akasha) e snapshot (Kratos).  Esses relatórios contêm links para todos os artefatos e logs de execução.
- **Delete e Clean Up:** a política de retenção define que arquivos temporários devem ser limpos após o handoff para evitar acumulação de dados sensíveis.  A eliminação de dados segue procedimentos documentados e auditados.

## Considerações Técnicas

- **PII**: qualquer campo que contenha informações pessoais (e‑mail, CPF, telefone) deve ser criptografado ou mascarado e explicitamente marcado no schema.  Os gabaritos de schema incluem campos `is_encrypted: true` para sinalizar proteção.
- **Autorização**: APIs geradas devem aderir ao princípio de `role‑based access control (RBAC)` e, quando aplicável, integrar‑se a provedores de identidade (ex: OAuth2, OpenID Connect).  O `api_contract.yaml` deve especificar requisitos de autenticação e autorização.
- **Audit Trail**: todos os módulos Python incluem logs estruturados (JSON) que registram timestamp, usuário/agente, ação, parâmetros sanitizados e status.  Logs nunca contêm dados sensíveis em texto claro.
- **Keys and Secrets**: a configuração de modelos e ferramentas (por exemplo, chaves da OpenAI ou Anthropic) deve ser lida a partir de cofres seguros (por exemplo, AWS Secrets Manager, HashiCorp Vault) e nunca commitada no repositório.

## Próximos Passos

1. Implementar o `security‑guardian` como sub‑agente real com escopo e ferramentas permitidas limitados a varredura de arquivos.
2. Criar scripts de `pre‑action` e `post‑action` na pasta `.claude/hooks` para ativar as sentinelas antes de cada operação de arquivo.
3. Definir a integração com provedores de secrets management para leitura segura de chaves de API.
4. Atualizar `config/risk_policy.yaml` para assegurar que todo risco `R3` exige `dry_run=True` e aprovação explícita.

---
*Gerado por: Aurora — Perfect Factory V6 | 2026‑06‑04*