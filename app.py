from flask import Flask, request, render_template, jsonify
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import json

# Inicializa o Flask
app = Flask(__name__)

# Configurações do chatbot (carrega do arquivo JSON)
def carregar_respostas(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

respostas = carregar_respostas("respostas.json")
perguntas = list(respostas.keys())

vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X_train = vectorizer.fit_transform(perguntas)

def preprocessar_texto(texto):
    texto = texto.lower()
    texto = "".join([char for char in texto if char not in string.punctuation])
    return texto

def chatbot_resposta(pergunta):
    pergunta_processada = preprocessar_texto(pergunta)
    
    if pergunta_processada in perguntas:
        return respostas[pergunta_processada]
        
    pergunta_vetorizada = vectorizer.transform([pergunta_processada])
    similaridades = cosine_similarity(pergunta_vetorizada, X_train)
    indice_max_similaridade = similaridades.argmax()
    valor_similaridade = similaridades[0][indice_max_similaridade]
    limite_similaridade = 0.5
    
    if valor_similaridade > limite_similaridade:
        pergunta_similar = perguntas[indice_max_similaridade]
        return respostas[pergunta_similar]
    else:
        return "Desculpe, não entendi a sua pergunta. Pode ser mais claro?"

# --- Rotas do Servidor ---

# Rota para a página inicial, que renderiza a interface HTML
@app.route('/')
def index():
    return render_template('chatbot_interface.html')

# Rota para a API do chatbot
@app.route('/get_response', methods=['POST'])
def get_response():
    # Pega a mensagem do usuário do corpo da requisição JSON
    user_message = request.json.get('message')
    
    # Processa a mensagem com a função do seu chatbot
    bot_response = chatbot_resposta(user_message)
    
    # Retorna a resposta do bot em formato JSON
    return jsonify({"response": bot_response})

# --- Adicionando Rota para Métricas do Prometheus ---
# Rota para expor as métricas. O Prometheus irá coletar daqui.
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

# --- Modificação do Ponto de Entrada para usar Gunicorn com Prometheus ---
if __name__ == '__main__':
    # Roda o servidor. debug=True para reiniciar automaticamente após mudanças.
    app.run(debug=True)
