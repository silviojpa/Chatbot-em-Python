# Usa uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
# Isso aproveita o cache do Docker para builds mais rápidos.
COPY requirements.txt .

# Instala as bibliotecas Python
RUN pip install --no-cache-dir -r requirements.txt

# --- NOVO PASSO ADICIONADO ---
# Instala os dados do NLTK necessários para a aplicação
RUN python -c "import nltk; nltk.download('punkt')"
# --- FIM DO NOVO PASSO ---

# Copia o restante dos arquivos do projeto para o container
COPY . .

# Expõe a porta 5000 para o mundo exterior
EXPOSE 5000

# Comando para rodar a aplicação com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
