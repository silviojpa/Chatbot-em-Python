pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona o seu repositório Git.
                git url: 'https://github.com/silviojpa/Chatbot-em-Python.git'
            }
        }

        stage('Build & Run') {
            steps {
                // Cria e ativa o ambiente virtual, e instala as dependências.
                // O comando 'source' é o padrão para shells no Ubuntu.
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install Flask scikit-learn numpy nltk
                '''
            }
        }

        stage('Execute o Chatbot') {
            steps {
                // Inicia o servidor do Flask.
                sh '''
                source venv/bin/activate
                python3 app.py
                '''
            }
        }
    }

}
