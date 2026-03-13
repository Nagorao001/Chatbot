# EduBot — Chatbot Website Walkthrough

## What Was Built

A fully functional chatbot website powered by your existing [chatbot.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py) and [long_responses.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/long_responses.py) backend logic, served through a Flask web server with a premium dark-themed chat interface.

## Files Created / Modified

| File | Action | Purpose |
|------|--------|---------|
| [chatbot.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/chatbot.py) | Modified | Added `if __name__` guard so it can be imported by Flask |
| [app.py](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/app.py) | New | Flask server with `/` and `/api/chat` routes |
| [templates/index.html](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/templates/index.html) | New | Chat UI with welcome screen, quick chips, message area |
| [static/css/style.css](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/static/css/style.css) | New | Dark glassmorphism theme with animations |
| [static/js/chat.js](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/static/js/chat.js) | New | Client-side message handling, fetch API, typing indicator |
| [requirements.txt](file:///c:/Users/Nagorao/OneDrive/Desktop/Python_Codes/New%20folder/requirements.txt) | New | `flask` and `wikipedia` dependencies |

## How to Run

```bash
cd "c:\Users\Nagorao\OneDrive\Desktop\Python_Codes\New folder"
pip install flask wikipedia
python app.py
```

Then open **http://localhost:5000** in your browser.

## Test Results

All tests passed ✅ — quick-reply chips, typed messages, typing indicator, and clear chat all work correctly.

````carousel
![Landing page with dark theme, EduBot header, welcome message and quick-reply chips](C:\Users\Nagorao\.gemini\antigravity\brain\00291dd1-28d7-445f-8546-9b1e66d5580c\initial_landing_page_1773431070070.png)
<!-- slide -->
![Bot responding to "What is education?" quick chip](C:\Users\Nagorao\.gemini\antigravity\brain\00291dd1-28d7-445f-8546-9b1e66d5580c\conversation_after_quick_reply_1773431111178.png)
<!-- slide -->
![Full conversation with "hello" and "give me study tips" messages](C:\Users\Nagorao\.gemini\antigravity\brain\00291dd1-28d7-445f-8546-9b1e66d5580c\final_conversation_1773431121956.png)
````

## Demo Recording

![Full browser test recording](C:\Users\Nagorao\.gemini\antigravity\brain\00291dd1-28d7-445f-8546-9b1e66d5580c\chatbot_ui_test_1773430929039.webp)
