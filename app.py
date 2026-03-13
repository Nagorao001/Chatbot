import time
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

# ===== Rate Limiter Configuration =====
RATE_LIMIT_MAX_REQUESTS = 10  # Max requests per window
RATE_LIMIT_WINDOW_SECONDS = 60  # Time window in seconds
rate_limit_store: dict[str, list[float]] = {}  # IP -> list of timestamps


def is_rate_limited(ip: str) -> tuple[bool, int]:
    """Check if an IP is rate-limited. Returns (is_limited, retry_after_seconds)."""
    now = time.time()
    window_start = now - RATE_LIMIT_WINDOW_SECONDS

    # Get existing timestamps and prune old ones
    timestamps = rate_limit_store.get(ip, [])
    timestamps = [t for t in timestamps if t > window_start]
    rate_limit_store[ip] = timestamps

    if len(timestamps) >= RATE_LIMIT_MAX_REQUESTS:
        # Calculate how long until the oldest request in the window expires
        oldest = timestamps[0]
        retry_after = int(oldest - window_start) + 1
        return True, max(retry_after, 1)

    # Record this request
    timestamps.append(now)
    return False, 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    # --- Rate limit check ---
    client_ip = request.remote_addr or '127.0.0.1'
    limited, retry_after = is_rate_limited(client_ip)
    if limited:
        return jsonify({
            'error': 'Rate limit exceeded. Please wait before sending another message.',
            'retry_after': retry_after
        }), 429

    data = request.get_json()
    user_message = data.get('message', '')
    if not user_message.strip():
        return jsonify({'response': 'Please type a message!'})
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
