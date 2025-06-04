import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

@app.route('/', methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()

        if text == "/start":
            send_message(chat_id, "Hello sir, Welcome to the Bot.\nPlease write /help to see the commands available.")
        elif text == "/help":
            send_message(chat_id, """Available Commands:
    /github - To get the GitHub Link
    /linkedin - To get the LinkedIn profile 
    /gmail - To get the Gmail contact
    /resume - To get Resume PDF
    /portfolio - To get the Portfolio Link
    /poll - Rate this bot""")
        elif text == "/gmail":
            send_message(chat_id, "Gmail => mailto:hemangikariya1803@gmail.com")
        elif text == "/github":
            send_message(chat_id, "GitHub => https://github.com/hemangikariya")
        elif text == "/linkedin":
            send_message(chat_id, "LinkedIn => https://www.linkedin.com/in/hemangikariya")
        elif text == "/resume" or text == "/portfolio":
            send_message(chat_id, "Portfolio => https://hemangi-kariya-portfolio.vercel.app")
        elif text == "/poll":
            send_poll(chat_id)
        else:
            send_message(chat_id, f"Sorry, '{text}' is not a valid command.")

    return "ok"


def send_message(chat_id, text):
    url = f"{BOT_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


def send_poll(chat_id):
    url = f"{BOT_URL}/sendPoll"
    payload = {
        "chat_id": chat_id,
        "question": "How do you rate this bot?",
        "options": ["👍 Great", "👌 Good", "😐 Average", "👎 Poor"],
        "is_anonymous": False,
        "allows_multiple_answers": False
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
