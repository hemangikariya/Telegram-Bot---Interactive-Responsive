# import os
# from dotenv import load_dotenv
# from telegram.update import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# import telegram

# load_dotenv()  
# TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# updater = Updater(TOKEN)

# def start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Hello sir, Welcome to the Bot.\nPlease write /help to see the commands available.")

# def help(update: Update, context: CallbackContext):
#     update.message.reply_text("""Available Commands:
#     /github - To get the GitHub Link
#     /linkedin - To get the LinkedIn profile 
#     /gmail - To get the Gmail contact
#     /resume - To get Resume PDF
#     /portfolio - To get the Portfolio Link
#     /poll - Rate this bot""")

# def gmail(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Gmail => mailto:hemangikariya1803@gmail.com")

# def github_link(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "GitHub => https://github.com/hemangikariya")

# def linkedIn_link(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "LinkedIn => https://www.linkedin.com/in/hemangikariya")

# def resume_pdf(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Portfolio => https://hemangi-kariya-portfolio.vercel.app")

# def portfolio_link(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "Portfolio => https://hemangi-kariya-portfolio.vercel.app")

# def poll(update: Update, context: CallbackContext):
#     question = "How do you rate this bot?"
#     options = ["👍 Great", "👌 Good", "😐 Average", "👎 Poor"]
    
#     context.bot.send_poll(
#         chat_id=update.effective_chat.id,
#         question=question,
#         options=options,
#         is_anonymous=False, 
#         allows_multiple_answers=False
#     )

# def unknown(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         f"Sorry '{update.message.text}' is not a valid command.")

# def unknown_text(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         f"Sorry I can't recognize what you said: '{update.message.text}'")
    
# updater.dispatcher.add_handler(CommandHandler('poll', poll))
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('github', github_link))
# updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(CommandHandler('resume', resume_pdf))
# updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_link))
# updater.dispatcher.add_handler(CommandHandler('gmail', gmail))
# updater.dispatcher.add_handler(CommandHandler('portfolio', portfolio_link))
# updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown_text))  
# updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  

# try:
#     updater.start_polling()
#     updater.idle()  # Keeps bot running until interrupted
# except telegram.error.Conflict:
#     print("Bot is already running elsewhere. Only one instance allowed.")

# https://api.telegram.org/bot7929396841:AAGhnVEfWr4X734iMjwqxUCc1KT7YJVyRf4/setWebhook?url=https://6eab-2409-40c1-3193-ea99-11ff-dbdc-b667-cee3.ngrok-free.app/7929396841:AAGhnVEfWr4X734iMjwqxUCc1KT7YJVyRf4


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

@app.route(f"/{TOKEN}", methods=["POST"])
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
