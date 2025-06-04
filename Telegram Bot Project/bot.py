import os
from dotenv import load_dotenv
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import telegram

load_dotenv()  
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

updater = Updater(TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.\nPlease write /help to see the commands available.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands:
    /github - To get the GitHub Link
    /linkedin - To get the LinkedIn profile 
    /gmail - To get the Gmail contact
    /resume - To get Resume PDF
    /portfolio - To get the Portfolio Link
    /poll - Rate this bot""")

def gmail(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Gmail => mailto:hemangikariya1803@gmail.com")

def github_link(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GitHub => https://github.com/hemangikariya")

def linkedIn_link(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn => https://www.linkedin.com/in/hemangikariya")

def resume_pdf(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Portfolio => https://hemangi-kariya-portfolio.vercel.app")

def portfolio_link(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Portfolio => https://hemangi-kariya-portfolio.vercel.app")

def poll(update: Update, context: CallbackContext):
    question = "How do you rate this bot?"
    options = ["👍 Great", "👌 Good", "😐 Average", "👎 Poor"]
    
    context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question,
        options=options,
        is_anonymous=False, 
        allows_multiple_answers=False
    )

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Sorry '{update.message.text}' is not a valid command.")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Sorry I can't recognize what you said: '{update.message.text}'")
    
updater.dispatcher.add_handler(CommandHandler('poll', poll))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('github', github_link))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('resume', resume_pdf))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_link))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail))
updater.dispatcher.add_handler(CommandHandler('portfolio', portfolio_link))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown_text))  
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  

try:
    updater.start_polling()
    updater.idle()  # Keeps bot running until interrupted
except telegram.error.Conflict:
    print("Bot is already running elsewhere. Only one instance allowed.")
