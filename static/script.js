const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

const sessionId = Math.random().toString(36).substring(2, 15);

function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    
    if (sender === 'user') {
        messageDiv.classList.add('user-message');
    } else {
        messageDiv.classList.add('bot-message');
        text = '🧭 ' + text;
    }
    
    messageDiv.innerText = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function handleSend() {
    const text = userInput.value.trim();
    if (text === '') return;

    addMessage(text, 'user');
    userInput.value = '';

    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            message: text,
            session_id: sessionId
        })
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.reply, 'bot');
    })
    .catch(error => {
        console.error("Error connecting to server:", error);
        addMessage("Connection error. Ensure the Flask server is running.", 'bot');
    });
}

sendBtn.addEventListener('click', handleSend);

userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        handleSend();
    }
});