pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main-mon', url: 'https://github.com/silviojpa/Chatbot-em-Python.git'
            }
        }

        stage('Build e Rodar com Docker') {
    steps {
        script {
            // Define o nome do seu compose file
            def composeFile = "docker-compose.yml"

            // Para evitar conflitos de porta, para e remove os containers anteriores, se existirem
            // O --rmi all remove as imagens criadas pelo compose
            sh "docker compose -f ${composeFile} down --rmi all || true"

            // Constrói e roda os containers em segundo plano (-d)
            // O docker-compose build é incluído automaticamente pelo "up"
            sh "docker compose -f ${composeFile} up --build -d"
                }
            }
        }
    }
}





