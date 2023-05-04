const form = document.getElementById('chat-form');
const messageInput = document.getElementById('message-input');
const chatLog = document.getElementById('chat-log');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const message = messageInput.value.trim();
  messageInput.value = '';

  if (message) {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    const chatEntry = document.createElement('div');
    chatEntry.classList.add('chat-entry');

    const chatPrompt = document.createElement('div');
    chatPrompt.classList.add('chat-prompt');
    chatPrompt.innerText = message;

    const chatResponse = document.createElement('div');
    chatResponse.classList.add('chat-response');
    chatResponse.innerText = data.response;

    chatEntry.appendChild(chatPrompt);
    chatEntry.appendChild(chatResponse);

    chatLog.appendChild(chatEntry);
    chatLog.scrollTop = chatLog.scrollHeight;
  }
});
