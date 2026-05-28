const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function addMsg(text, className) {
    const div = document.createElement('div');
    div.className = `msg ${className}`;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTyping() {
    const div = document.createElement('div');
    div.className = 'typing';
    div.id = 'typing';
    div.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
    chatBox.appendChild(div);
}

document.getElementById('send-btn').onclick = async () => {
    const text = userInput.value;
    if(!text) return;
    addMsg(text, 'user-msg');
    userInput.value = '';
    addTyping();

    const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: text})
    });
    const data = await res.json();
    document.getElementById('typing').remove();
    addMsg(data.reply, 'bot-msg');
};