const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Adiciona uma mensagem na interface
function addMessage(text, sender) {
    const messageContainer = document.createElement('div');
    messageContainer.className = `flex ${sender === 'user' ? 'justify-end' : 'justify-start'}`;

    const messageDiv = document.createElement('div');
    messageDiv.className = `p-3 rounded-lg max-w-xs shadow-sm ${
        sender === 'user' ? 'bg-indigo-500 text-white' : 'bg-gray-200 text-gray-800'
    }`;
    messageDiv.textContent = text;

    messageContainer.appendChild(messageDiv);
    chatBox.appendChild(messageContainer);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function getBotResponse(userMessage) {
    try {
        // Envia a mensagem do usuário para o servidor Python
        const response = await fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        });

        // Pega a resposta do servidor
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error("Erro ao comunicar com o servidor:", error);
        return "Desculpe, ocorreu um erro. Tente novamente mais tarde.";
    }
}

async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage === '') {
        return;
    }

    addMessage(userMessage, 'user');
    userInput.value = '';

    // Espera a resposta do bot antes de adicionar na tela
    const botResponse = await getBotResponse(userMessage);
    addMessage(botResponse, 'bot');
}

sendBtn.addEventListener('click', sendMessage);

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
