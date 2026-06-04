# Command: appfactory-intake

**Objetivo**

Receber os dados de entrada de uma nova missão de criação de produto e prepará-los para o pipeline do **System Creation OS**. Esse comando lê uma ideia ou problema de negócio, estrutura em campos padronizados, grava um arquivo ``.json`` (em ambiente seguro) e dispara a próxima etapa.

**Quando usar**

Use quando um cliente ou time interno submeter uma nova ideia de produto ou requisito. Este comando transforma a entrada livre em um ``MissionPackage`` normalizado, valida campos obrigatórios e armazena o arquivo no diretório de entrada configurado.

**Entradas esperadas**

- Texto livre descrevendo a ideia ou problema.
- Identificador opcional do cliente ou projeto.
- Parâmetros adicionais (setor, urgência, suposição de receita).

**Saídas esperadas**

- Arquivo ``mission_package.json`` gravado no diretório de ``examples/``.
- Mensagem de log indicando caminho do arquivo salvo.

**Paths permitidos**

- Somente diretórios abaixo de ``examples/`` e ``docs/`` são graváveis.

**Risco**

``R1`` — Criação de arquivo local sem efeitos externos. Nenhum acesso a rede.

**Regras de segurança**

1. Nunca ler ou gravar arquivos fora do diretório permitido.
2. Nunca acessar variáveis de ambiente ou secrets.
3. Não executar comandos de terminal ou acessar redes externas.

**Critérios de aceite**

- Entradas obrigatórias validadas: descrição não vazia.
- Arquivo salvo com sucesso no diretório ``examples/``.
- Campos adicionais ausentes devem ser definidos como ``null``.

**Proibições**

- Não executar ``git add``, ``git push`` ou qualquer operação de deploy.
- Não criar ou modificar arquivos de configuração do repositório.
- Não gravar em ``.env`` ou ler secrets.