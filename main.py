from flask import Flask, request
import requests
import os

# توکن ربات از متغیر محیطی Runflare
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

# تابع ارسال پیام با دکمه
def send_welcome_message(chat_id):
    keyboard = {
        "inline_keyboard": [
            [{"text": "📢 کانال تلگرام", "url": "https://t.me/irsolaris"}],
            [{"text": "📞 تماس", "url": "tel:+989203522359"}],
            [{"text": "🌐 سایت", "url": "https://mahdiworld.ir"}]
        ]
    }

    payload = {
        "chat_id": chat_id,
        "text": "سلام 👋\nبه ربات خوش آمدید.\nلطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        "reply_markup": keyboard
    }

    requests.post(f"{API_URL}/sendMessage", json=payload)

# وبهوک
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_welcome_message(chat_id)

    return "ok", 200

# تست در مرورگر
@app.route("/")
def home():
    return "ربات در حال اجراست ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
