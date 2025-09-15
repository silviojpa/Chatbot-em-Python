# Implementação de CI/CD com Jenkins e Docker
Este documento descreve o processo de implementação de um pipeline de Integração e Entrega Contínua (CI/CD) usando Jenkins e Docker para automatizar o deploy da aplicação de chatbot.

# 1. Configuração Inicial do Ambiente
- Instalação do Jenkins: O Jenkins foi instalado e configurado em um servidor Ubuntu, servindo como a ferramenta central para a automação do pipeline.

- Instalação do Docker: O Docker foi instalado no mesmo servidor para permitir a criação de imagens e a execução da aplicação em containers.

- Configuração de Credenciais: As credenciais SSH foram configuradas no Jenkins, permitindo que a ferramenta se conectasse ao repositório Git e buscasse as alterações do projeto.

# 2. Criação do Jenkinsfile
- Um arquivo Jenkinsfile foi criado na raiz do projeto para definir o pipeline de CI/CD. Este arquivo automatizou as seguintes etapas:

- Checkout: Buscou o código mais recente do repositório Git.

- Build e Deploy: Conduziu a construção da imagem Docker e o deploy da aplicação.

# 3. Fluxo de Execução do Pipeline
- A cada git push para o branch main no GitHub, o Jenkins disparou automaticamente o pipeline com as seguintes etapas:

- Limpeza do Ambiente: O container Docker antigo da aplicação (chatbot-container) foi parado e removido, evitando conflitos de porta.

- Build da Imagem Docker: A imagem Docker (chatbot-flask) foi construída a partir do Dockerfile do projeto. Durante a build, o pip instalou as dependências do requirements.txt.

- Execução do Container: Um novo container foi criado e iniciado em segundo plano (-d) a partir da nova imagem Docker. A porta 5000 do container foi mapeada para a porta 5000 do host, tornando a aplicação acessível.

# 4. Resolução de Problemas (Troubleshooting)
- Durante o desenvolvimento do pipeline, diversos problemas foram encontrados e resolvidos:

- Conflitos de Merge: Inicialmente, um git pull --rebase resultou em um conflito no arquivo requirements.txt. Isso foi resolvido manualmente, editando o arquivo e continuando o rebase.

- Compatibilidade de Bibliotecas: A aplicação falhou ao iniciar devido a uma incompatibilidade entre as versões do Flask e Werkzeug. O erro ImportError: cannot import name 'url_quote' foi corrigido ao atualizar as versões das bibliotecas no requirements.txt.

- Dependências do NLTK: O container parava logo após iniciar devido a um erro LookupError: Resource punkt not found. Isso ocorreu porque a biblioteca NLTK, embora instalada, precisava que o pacote de dados punkt fosse baixado. A solução foi adicionar um passo de download no Dockerfile.

# 5. Resultado Final
- Após a resolução dos problemas, o pipeline foi executado com sucesso. O container chatbot-container foi iniciado e está em execução. A aplicação se tornou acessível pela porta 5000, e a interface do chatbot pode ser visualizada no navegador, confirmando o deploy contínuo e automatizado da aplicação.
--------------------------------------------------------------------------------------------

# Fase 2: Implementação de Monitoramento com Prometheus e Grafana
Esta seção detalha a extensão do pipeline de CI/CD para incluir um sistema de monitoramento robusto. A solução utiliza o Prometheus para coleta de métricas e o Grafana para visualização, garantindo a visibilidade em tempo real sobre a saúde e o desempenho da aplicação.

# 1. Arquitetura de Monitoramento
A arquitetura foi migrada para um ambiente orquestrado com Docker Compose, que gerencia três serviços em uma única rede:

- chatbot-flask: O serviço da aplicação.

- prometheus: O servidor de monitoramento que coleta as métricas da aplicação.

- grafana: A plataforma de visualização que consome os dados do Prometheus para criar dashboards.

2. Implementação no Código e Configuração
Atualização do requirements.txt: A biblioteca prometheus-client foi adicionada para permitir que a aplicação Flask exponha suas métricas.

- Modificação do app.py: O código da aplicação foi alterado para incluir a lógica de monitoramento. Um endpoint /metrics foi criado, usando o DispatcherMiddleware, para expor as métricas que o Prometheus irá coletar.

- Criação do docker-compose.yml: Este arquivo centraliza a configuração dos três serviços, garantindo que eles sejam construídos e executados juntos. Ele define as portas, nomes dos containers e a rede (monitoramento-net) para permitir a comunicação entre os serviços.

- Configuração do prometheus.yml: Um arquivo de configuração para o Prometheus foi criado, especificando o target para a aplicação do chatbot (http://chatbot-flask:5000) para que ele comece a "raspar" as métricas.

3. Atualização do Pipeline Jenkins
O Jenkinsfile foi modificado para utilizar o docker-compose, simplificando o processo de deploy:

- O pipeline agora executa o comando docker compose up --build -d para construir a nova imagem da aplicação e subir todos os três containers de uma vez.

- Os comandos docker stop e docker rm foram mantidos para garantir a limpeza do ambiente de builds anteriores e evitar conflitos de nome de container.

4. Resultado e Acesso aos Serviços
Com a implementação concluída e o pipeline executado com sucesso:

- O Prometheus está ativo e coletando métricas do chatbot com o status UP.

- O Grafana foi configurado para usar o Prometheus como fonte de dados, o que resolveu o problema de conexão inicial.

- A aplicação do chatbot continua acessível pela porta 5000, e a interface está funcionando.

A partir de agora, é possível criar dashboards no Grafana para visualizar o desempenho do chatbot, como o total de requisições, latência e uso de recursos.
