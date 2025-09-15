# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências.
# Isso aproveita o cache do Docker para builds mais rápidos.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto para o container
COPY . .

# Expõe a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação usando Gunicorn
# Gunicorn irá rodar 4 workers e a aplicação app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "4"]