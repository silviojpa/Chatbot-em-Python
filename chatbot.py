import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import json # Importa a biblioteca para trabalhar com JSON

# Função para carregar os dados do arquivo JSON
def carregar_respostas(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

# Carrega as respostas do arquivo respostas.json
respostas = carregar_respostas("respostas.json")

# Pré-processamento de texto
def preprocessar_texto(texto):
    # Converte para minúsculas
    texto = texto.lower()
    # Remove pontuação
    texto = "".join([char for char in texto if char not in string.punctuation])
    return texto

# Criando a lista de perguntas para o treinamento a partir das chaves do dicionário carregado
perguntas = list(respostas.keys())

# O vetorizador transforma o texto em vetores numéricos
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X_train = vectorizer.fit_transform(perguntas)

# Função principal do chatbot
def chatbot_resposta(pergunta):
    pergunta_processada = preprocessar_texto(pergunta)
    
    # Se a pergunta processada for uma das perguntas conhecidas, retorna a resposta direta
    if pergunta_processada in perguntas:
        return respostas[pergunta_processada]
        
    # Vetoriza a pergunta do usuário
    pergunta_vetorizada = vectorizer.transform([pergunta_processada])
    
    # Calcula a similaridade entre a pergunta do usuário e todas as perguntas de treinamento
    similaridades = cosine_similarity(pergunta_vetorizada, X_train)
    
    # Pega o índice da pergunta mais similar
    indice_max_similaridade = similaridades.argmax()
    
    # Pega a similaridade máxima encontrada
    valor_similaridade = similaridades[0][indice_max_similaridade]
    
    # Define um limite para considerar a resposta
    limite_similaridade = 0.5
    
    if valor_similaridade > limite_similaridade:
        pergunta_similar = perguntas[indice_max_similaridade]
        return respostas[pergunta_similar]
    else:
        return "Desculpe, não entendi a sua pergunta. Pode ser mais claro?"

# Loop principal para interagir com o usuário
print("Olá! Eu sou o seu chatbot. Digite 'tchau' para sair.")
while True:
    entrada_usuario = input("Você: ")
    if entrada_usuario.lower() == "tchau":
        print("Chatbot: Até mais! Foi um prazer conversar com você.")
        break
    else:
        resposta = chatbot_resposta(entrada_usuario)
        print("Chatbot:", resposta)