// ===== DOM Elements =====
const messagesContainer = document.getElementById('chat-messages');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const clearBtn = document.getElementById('clear-chat-btn');
const welcomeSection = document.getElementById('welcome-section');

// ===== Bot Avatar SVG (reusable) =====
const BOT_AVATAR_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 2a4 4 0 0 1 4 4v1h1a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3v-7a3 3 0 0 1 3-3h1V6a4 4 0 0 1 4-4z"/>
    <circle cx="9" cy="13" r="1.25" fill="currentColor" stroke="none"/>
    <circle cx="15" cy="13" r="1.25" fill="currentColor" stroke="none"/>
    <path d="M9 17c1 1 5 1 6 0"/>
</svg>`;

const USER_AVATAR_SVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
    <circle cx="12" cy="7" r="4"/>
</svg>`;

// ===== Utility: Get timestamp =====
function getTimeString() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// ===== Create typing indicator element =====
function createTypingIndicator() {
    const row = document.createElement('div');
    row.className = 'typing-indicator';
    row.id = 'typing-indicator';
    row.innerHTML = `
        <div class="msg-avatar">${BOT_AVATAR_SVG}</div>
        <div class="typing-bubble">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
    `;
    return row;
}

// Add typing indicator to DOM
const typingIndicator = createTypingIndicator();
messagesContainer.appendChild(typingIndicator);

// ===== Scroll to bottom =====
function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// ===== Add a message to the chat =====
function addMessage(text, sender) {
    // Hide welcome section on first message
    if (welcomeSection) {
        welcomeSection.style.display = 'none';
    }

    const row = document.createElement('div');
    row.className = `message-row ${sender}`;

    const avatarSVG = sender === 'bot' ? BOT_AVATAR_SVG : USER_AVATAR_SVG;

    // Replace newlines with <br> for proper display
    const formattedText = text.replace(/\\n/g, '<br>').replace(/\n/g, '<br>');

    row.innerHTML = `
        <div class="msg-avatar">${avatarSVG}</div>
        <div>
            <div class="message-bubble">${formattedText}</div>
            <div class="msg-time">${getTimeString()}</div>
        </div>
    `;

    // Insert before the typing indicator
    messagesContainer.insertBefore(row, typingIndicator);
    scrollToBottom();
}

// ===== Show / Hide typing indicator =====
function showTyping() {
    typingIndicator.classList.add('visible');
    scrollToBottom();
}

function hideTyping() {
    typingIndicator.classList.remove('visible');
}

// ===== Rate-limit cooldown state =====
let isRateLimited = false;

function disableInput(seconds) {
    isRateLimited = true;
    messageInput.disabled = true;
    sendBtn.disabled = true;
    sendBtn.style.opacity = '0.4';
    messageInput.placeholder = `Rate limited — wait ${seconds}s...`;

    setTimeout(() => {
        isRateLimited = false;
        messageInput.disabled = false;
        sendBtn.disabled = false;
        sendBtn.style.opacity = '1';
        messageInput.placeholder = 'Type your question here...';
        messageInput.focus();
    }, seconds * 1000);
}

function addWarning(text) {
    if (welcomeSection) {
        welcomeSection.style.display = 'none';
    }
    const row = document.createElement('div');
    row.className = 'message-row bot';
    row.innerHTML = `
        <div class="msg-avatar">${BOT_AVATAR_SVG}</div>
        <div>
            <div class="message-bubble rate-limit-warning">${text}</div>
            <div class="msg-time">${getTimeString()}</div>
        </div>
    `;
    messagesContainer.insertBefore(row, typingIndicator);
    scrollToBottom();
}

// ===== Send message to the server =====
async function sendMessage(text) {
    const message = text.trim();
    if (!message || isRateLimited) return;

    // Add user message
    addMessage(message, 'user');
    messageInput.value = '';
    messageInput.focus();

    // Show typing indicator
    showTyping();

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        hideTyping();

        if (res.status === 429) {
            const data = await res.json();
            const retryAfter = data.retry_after || 10;
            addWarning(`⚠️ Slow down! You've sent too many messages. Try again in <strong>${retryAfter} seconds</strong>.`);
            disableInput(retryAfter);
            return;
        }

        const data = await res.json();
        addMessage(data.response, 'bot');
    } catch (error) {
        hideTyping();
        addMessage('Oops! Something went wrong. Please try again.', 'bot');
    }
}

// ===== Event Listeners =====

// Send button click
sendBtn.addEventListener('click', () => {
    sendMessage(messageInput.value);
});

// Enter key
messageInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(messageInput.value);
    }
});

// Quick chip clicks
document.querySelectorAll('.chip').forEach(chip => {
    chip.addEventListener('click', () => {
        const msg = chip.getAttribute('data-message');
        sendMessage(msg);
    });
});

// Clear chat
clearBtn.addEventListener('click', () => {
    // Remove all messages but keep typing indicator and welcome
    const messages = messagesContainer.querySelectorAll('.message-row');
    messages.forEach(msg => msg.remove());

    // Show welcome section again
    if (welcomeSection) {
        welcomeSection.style.display = 'flex';
    }
});

// Focus input on load
messageInput.focus();
