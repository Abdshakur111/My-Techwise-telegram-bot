# telegram.py
import requests

class TelegramAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, chat_id, text):
        method = "sendMessage"
        url = f"{self.base_url}{method}"
        params = {
            "chat_id": chat_id,
            "text": text
        }
        requests.post(url, params=params)
