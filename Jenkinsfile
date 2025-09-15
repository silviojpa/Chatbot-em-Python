pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'URL_DO_SEU_REPOSITORIO_AQUI'
            }
        }

        stage('Build e Rodar com Docker') {
            steps {
                script {
                    // Define o nome da sua imagem Docker
                    def imageName = 'chatbot-flask'
                    def containerName = 'chatbot-container'

                    // Para evitar conflitos de porta, pare e remova o container anterior se ele existir
                    sh "docker stop ${containerName} || true"
                    sh "docker rm ${containerName} || true"

                    // Constrói a imagem Docker a partir do Dockerfile
                    sh "docker build -t ${imageName} ."

                    // Roda o container em segundo plano (-d)
                    // Mapeia a porta 5000 do container para a porta 5000 da máquina host
                    sh "docker run -d --name ${containerName} -p 5000:5000 ${imageName}"
                }
            }
        }
    }
}
