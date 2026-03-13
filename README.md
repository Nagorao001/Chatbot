<div align="center">

# 🤖 EduBot — Your Education Assistant

**An intelligent chatbot that answers questions about education, knowledge, literacy, and learning.**

Built with Python · Flask · Vanilla JS

---

</div>

## 📖 About

EduBot is a web-based chatbot designed to answer questions related to **education in India** — covering topics like the education system, literacy rates, study tips, online vs. offline learning, and more. When a predefined answer isn't available, EduBot automatically searches **Wikipedia** and provides a summary, ensuring users always get a helpful response.

## ✨ Features

- 💬 **Natural Language Processing** — Keyword-matching engine that understands user intent and returns the best response
- 🌐 **Wikipedia Fallback** — Automatically queries Wikipedia when no predefined answer matches the user's question
- 🔍 **Google Search Fallback** — Provides a Google search link as a last resort if Wikipedia lookup fails
- 🛡️ **Rate Limiting** — Built-in IP-based rate limiter (10 requests/minute) to prevent abuse
- ⚡ **Quick Reply Chips** — Pre-built topic buttons for instant access to popular questions
- 🎨 **Modern UI** — Sleek, responsive chat interface with smooth animations and dark theme
- 🧹 **Chat History Control** — Clear chat button to reset the conversation

## 🛠️ Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Backend    | Python, Flask             |
| Frontend   | HTML5, CSS3, JavaScript   |
| NLP Engine | Custom keyword matching   |
| Knowledge  | Wikipedia API             |
| Font       | Inter (Google Fonts)      |

## 📂 Project Structure

```
Chatbot-2.0/
├── app.py               # Flask server with API routes & rate limiting
├── chatbot.py           # NLP engine — keyword matching & Wikipedia fallback
├── long_responses.py    # Predefined long-form responses on education topics
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Chat UI template
└── static/
    ├── css/
    │   └── style.css    # Styling & animations
    └── js/
        └── chat.js      # Frontend chat logic & API calls
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Chatbot-2.0.git
   cd Chatbot-2.0
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 💡 Usage

- Type any education-related question in the chat input
- Use the **quick reply chips** for popular topics like:
  - 📚 *What is education?*
  - ✏️ *Study tips*
  - 🇮🇳 *Education in India*
  - 💻 *Online vs Offline*
  - 🎓 *Benefits of education*
  - 📊 *Literacy rate*
- If no predefined response matches, EduBot fetches a summary from **Wikipedia**

## 🔧 API Reference

### `POST /api/chat`

Send a message to the chatbot.

**Request Body:**
```json
{
  "message": "What is education?"
}
```

**Success Response** `200`:
```json
{
  "response": "Education is the medium that gives us the skills..."
}
```

**Rate Limited** `429`:
```json
{
  "error": "Rate limit exceeded. Please wait before sending another message.",
  "retry_after": 5
}
```

## 📋 Topics Covered

| Category                          | Examples                                         |
|-----------------------------------|--------------------------------------------------|
| Education basics                  | Definition, types, importance                    |
| Indian education system           | Policy, structure, literacy rates                |
| Western vs Indian education       | Comparison of policies and approaches            |
| Online & offline education        | Pros, cons, differences                          |
| Study tips                        | Effective strategies for students                |
| Moral vs academic education       | Comparison and importance                        |
| Special needs education (CWSN)    | Programs and special schools                     |
| Government initiatives            | SII Portal, Yuva Sangam                          |
| Career options in Computer Science| Software Engineer, Network Architect, etc.       |
| General knowledge                 | PM of India, President, Education Minister       |

## 👥 Authors

- **Nagorao Dinkar Kute**

## 📄 License

This project is open source and available for educational purposes.

---

<div align="center">

⭐ **Star this repo if you found it helpful!** ⭐

</div>
