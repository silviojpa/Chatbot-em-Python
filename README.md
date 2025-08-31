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

PYTHON/
├── templates/
│   └── chatbot_interface.html
├── static/
│   └── interacao.js
├── venv/
├── app.py
├── chatbot.py
└── respostas.json


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

Sinta-se à vontade para expandir este projeto! Algumas ideias:

* Adicionar mais perguntas e respostas ao arquivo `respostas.json`.
* Implementar um banco de dados (como SQLite ou PostgreSQL) para armazenar as respostas.
* Integrar o chatbot com uma API externa.
* Melhorar a lógica de similaridade de texto.
