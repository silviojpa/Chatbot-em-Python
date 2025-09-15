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
                    def composeFile = "docker-compose.yml"
                    def containerName = "chatbot-container"
        
                    // Adicionado para garantir que o container existente seja removido
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"
        
                    // Agora, com o ambiente limpo, o docker-compose pode subir
                    sh "docker-compose -f ${composeFile} up --build -d"
                }
            }
        }
    }
}






