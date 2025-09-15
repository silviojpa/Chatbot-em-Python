# Meu Chatbot em Python com Interface Web

Este é um projeto simples e elegante de um chatbot criado em Python, com uma interface de usuário completa e moderna, utilizando Flask para o servidor e Tailwind CSS para o design.

## Tecnologias Utilizadas

O projeto é dividido em Frontend e Backend.

* **Python**: A linguagem principal para toda a lógica do chatbot e do servidor.
* **Flask**: Um micro-framework Python utilizado para criar o servidor web.
* **HTML**: A linguagem de marcação que define a estrutura da interface do usuário.
* **CSS e Tailwind CSS**: Para a estilização. O Tailwind CSS, em particular, permite um design rápido e moderno.
* **JavaScript**: Controla a interatividade da interface, enviando e recebendo dados do servidor.

### Bibliotecas Python:

* **nltk e scikit-learn**: Usadas para processar texto e calcular a similaridade entre as perguntas.

## Estrutura do Projeto

A estrutura de pastas segue as boas práticas de um projeto Flask, separando os arquivos de código, templates e arquivos estáticos.
````
PYTHON/
├── templates/
│   └── chatbot_interface.html
├── static/
│   └── interacao.js
├── venv/
├── app.py
├── chatbot.py
└── respostas.json
````

## Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto em sua máquina.

1.  **Clone o Repositório:**

    *Nota: O link fornecido é de um vídeo do YouTube. Você deve substituir `[https://www.youtube.com/watch?v=GRf6so_sois](https://www.youtube.com/watch?v=GRf6so_sois)` pelo URL do seu repositório Git.*

    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [nome do repositório]
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    É uma boa prática isolar as dependências do projeto.

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as Dependências:**

    ```bash
    pip install Flask scikit-learn numpy nltk
    ```
    *Obs: Você pode ver a lista completa de pacotes instalados com `pip list`.*

4.  **Execute o Servidor Flask:**

    ```bash
    python app.py
    ```

5.  **Acesse o Chatbot:**
    Abra seu navegador e acesse a URL que o terminal irá fornecer, geralmente `http://127.0.0.1:5000`.

## Como Funciona

A lógica do projeto é bastante simples:

1.  O `app.py` inicia o servidor Flask e serve a página `chatbot_interface.html`.
2.  Quando você digita uma mensagem na interface, o JavaScript em `interacao.js` envia a mensagem para o servidor através de uma requisição `POST` para a rota `/get_response`.
3.  O `app.py` recebe essa requisição, processa a mensagem usando as funções de NLP do `chatbot.py` e encontra a melhor resposta no `respostas.json`.
4.  O servidor envia a resposta de volta para o JavaScript, que a exibe na tela para o usuário.

## Como Contribuir ou Melhorar

---------------------------------------------------------------------

## Implementação de CI/CD com Jenkins e Docker
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

Sinta-se à vontade para expandir este projeto! Algumas ideias:

* Adicionar mais perguntas e respostas ao arquivo `respostas.json`.
* Implementar um banco de dados (como SQLite ou PostgreSQL) para armazenar as respostas.
* Integrar o chatbot com uma API externa.
* Melhorar a lógica de similaridade de texto.
