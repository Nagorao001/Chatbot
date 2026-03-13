# Chatbot Website — Full-Stack Implementation

Build a premium, modern chatbot web application using Flask as the backend and your existing [chatbot.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py) + [long_responses.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/long_responses.py) as the AI engine.

## Proposed Changes

### Backend — Flask API

#### [MODIFY] [chatbot.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py)
- Remove the `while True` loop at the bottom (lines 129–131) so the file can be cleanly imported as a module
- The [get_response()](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py#122-126) function remains unchanged and will serve as the API's core logic

#### [NEW] [app.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/app.py)
- Flask web server with two routes:
  - `GET /` — serves the chat UI page
  - `POST /api/chat` — accepts `{ "message": "..." }` JSON, calls `chatbot.get_response()`, returns `{ "response": "..." }`
- Imports [chatbot.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py) directly

#### [NEW] [requirements.txt](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/requirements.txt)
- Lists `flask` and `wikipedia` as dependencies

---

### Frontend — Premium Chat UI

#### [NEW] [templates/index.html](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/templates/index.html)
- Full HTML page with a modern, dark-themed chat interface
- Chat header with bot name and status indicator
- Scrollable message area with distinct user/bot message bubbles
- Input bar with send button at the bottom
- Typing indicator animation when waiting for bot response
- Suggested quick-reply chips for common questions
- Uses Google Fonts (Inter) for premium typography

#### [NEW] [static/css/style.css](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/static/css/style.css)
- Dark glassmorphism theme with gradient accents
- Smooth message entrance animations (slide-in + fade)
- Responsive layout that works on desktop and mobile
- Styled scrollbar, hover effects, micro-animations on buttons
- Typing indicator dots animation

#### [NEW] [static/js/chat.js](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/static/js/chat.js)
- Sends user messages to `/api/chat` via `fetch()` API
- Renders user and bot messages dynamically
- Shows/hides typing indicator during API calls
- Auto-scrolls to latest message
- Handles Enter key and send button
- Quick-reply chip click handlers

---

## Verification Plan

### Browser Testing
1. Run `pip install flask wikipedia` to install dependencies
2. Run `python app.py` to start the Flask dev server
3. Open `http://localhost:5000` in the browser
4. Verify the chat UI loads with the dark theme, header, input bar, and quick-reply chips
5. Send a message like "hello" and verify the bot responds "Hello!"
6. Send "what is education" and verify a long response is returned
7. Test quick-reply chips work correctly
8. Test typing indicator appears while waiting for response
9. Test responsive layout by resizing the browser window
