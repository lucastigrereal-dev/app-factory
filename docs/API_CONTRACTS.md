# API Contracts

Este documento define as diretrizes para a criação de **contratos de API** no contexto do System Creation OS.  Um contrato de API é uma especificação formal (idealmente em OpenAPI/JSON Schema) que descreve como componentes comunicam‑se entre si e com serviços externos.  O objetivo é garantir interoperabilidade, segurança e governança.

## Objetivo

* Padronizar a definição de endpoints, métodos HTTP, parâmetros e códigos de resposta.
* Assegurar que toda API declare claramente as precondições, pós‑condições e restrições de segurança.
* Permitir a geração automática de stubs, mocks e documentação a partir dos contratos.

## Boas práticas

1. **Especificação formal**: Utilize OpenAPI (versão 3.x) para descrever rotas, parâmetros, corpos de requisição e de resposta.  Inclua exemplos concretos.
2. **Versionamento**: Indique a versão da API no caminho (`/v1/`), pois contratos estáveis favorecem evoluções sem quebrar compatibilidade.
3. **Segurança**: Defina mecanismos de autenticação/autorização (chave de API, OAuth) sem incluir segredos diretamente nos contratos.
4. **Consistência**: Prefira nomes de rotas e recursos no singular (`/mission` ao invés de `/missions`) e verbos HTTP adequados (GET, POST, PUT, DELETE).
5. **Códigos de status claros**: Documente todos os códigos de status retornados, incluindo mensagens de erro estruturadas (`error.code`, `error.message`).
6. **Campos obrigatórios**: Marque explicitamente campos obrigatórios nos schemas e forneça descrições para cada propriedade.

## Exemplos

Veja `config/mission_package.schema.yaml` e `config/work_order_result.schema.yaml` para exemplos de contratos machine‑readable.  Siga o mesmo estilo para demais serviços.

## Processo

1. Leia o PRD e o blueprint para identificar recursos e operações necessárias.
2. Modele o banco de dados (se aplicável) e derive entidades e relacionamentos.
3. Crie um arquivo YAML/JSON no diretório `config/` contendo a especificação da API.
4. Valide o contrato utilizando ferramentas OpenAPI linter.
5. Somente após a aprovação (CP‑2) gere stubs ou passe para o desenvolvimento.

## Risco

Este documento é classificativo **R0** (documentação).  A criação de contratos em `config/` é **R1**, pois não interage com sistemas externos, mas requer validação humana.