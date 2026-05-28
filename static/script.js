const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

window.onload = () => {
    addBotMsg("Hi, I'm AICompass! I'm here to boost your AI literacy. Ask me about definitions, facts, or quizzes using the guide on the side!");
};

function addUserMsg(text) {
    const wrapper = document.createElement('div');
    wrapper.className = 'msg-wrapper user-wrapper slide-in';
    wrapper.innerHTML = `<div class="msg user-msg">${text}</div>`;
    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addBotMsg(text) {
    const wrapper = document.createElement('div');
    wrapper.className = 'msg-wrapper bot-wrapper slide-in';
    wrapper.innerHTML = `<div class="bot-avatar">🧭</div><div class="msg bot-msg">${text}</div>`;
    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTyping() {
    const wrapper = document.createElement('div');
    wrapper.className = 'msg-wrapper bot-wrapper';
    wrapper.id = 'typing';
    wrapper.innerHTML = `<div class="bot-avatar">🧭</div><div class="msg bot-msg typing"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>`;
    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function handleSend() {
    const text = userInput.value.trim();
    if(!text) return;
    
    addUserMsg(text);
    userInput.value = '';
    addTyping();

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: text})
        });
        const data = await res.json();
        document.getElementById('typing').remove();
        
        let reply = data.reply;
        if (!reply || reply.trim() === "") {
            reply = "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!";
        }
        
        addBotMsg(reply);
    } catch (err) {
        document.getElementById('typing').remove();
        addBotMsg("I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!");
    }
}

sendBtn.addEventListener('click', handleSend);

userInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault(); 
        handleSend();
    }
});