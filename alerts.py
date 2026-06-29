import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    """
    Send a Telegram message.
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        return True

    except Exception as e:
        print(f"Telegram Error: {e}")
        return False
