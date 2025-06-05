# 🚀 Telegram Bot - Interactive & Responsive 🤖

This Flask-based Telegram bot, deployed on Render, offers seamless interaction through various commands such as polls, social media links, and quick assistance—combined with an interactive and fully responsive landing page that makes it easy for users to connect and engage via Telegram.

## ✨ Features

- `/start`: Initiates the bot with a warm welcome message.
- `/help`: Displays a comprehensive list of available commands.
- `/poll`: Engages users by creating an interactive poll.
- `/github`, `/linkedin`, `/gmail`, `/resume`, `/portfolio`: Provides quick access to professional links.
- Intelligent handling of unknown commands and messages.

## 🛠️ Prerequisites

- Python 3.7 or higher
- Flask
- python-telegram-bot (if used separately)
- python-dotenv
- requests

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/telegram-bot-interactive-responsive.git
cd telegram-bot-interactive-responsive
```

### 2. Add Environment Variables
Create a .env file in the root directory and add your Telegram bot token:
```bash
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
```

### 3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the bot:
```bash
python bot.py
```

## 🔑 Obtaining Your Bot Token

1. Open Telegram and search for `@BotFather`.
2. Send `/start`, then `/newbot` to create a new bot.
3. Follow the prompts to name your bot and generate a username.
4. Copy the provided token and add it to your `.env` file.

## 🌐 Webhook Setup (for Deployment)
Use this URL to set your webhook (replace placeholders accordingly):
```bash
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://<your-app-name>.onrender.com/
```
After successful setup, you'll receive:
```bash
{"ok":true,"result":true,"description":"Webhook was set"}
```

🎨 Landing Page Design
The homepage (/) includes:
- Responsive layout with modern UI
- A centered card saying: "🤖 Bot is Running!"
- Direct Telegram chat button → [💬 Chat with our Telegram Bot](https://t.me/TeleSmartPy_Bot)
- This page adjusts beautifully across devices and is mobile-friendly.

## 🚀 How to Test Your Bot

1. Search for your bot’s username in the Telegram app.
2. Start a chat and send commands like `/start` or `/poll`.
3. Watch your bot respond instantly with messages or polls.
4. Use `/poll` to initiate a live poll and engage users directly.

## ⚠️ Important Notes

- Ensure only one instance of the bot is running at a time to avoid conflicts.
- Never expose your `.env` file or token in public repositories.
- Do not push sensitive data to public repositories
- If you update your Render link or bot token, re-run the webhook setup

## 🙋‍♀️ Author
Made with ❤️ by Hemangi Kariya
GitHub: www.github.com/hemangikariya
LinkedIn: www.linkedin.com/in/hemangikariya

---

Your powerful Telegram bot is now ready to engage users with dynamic features! 🎉🤖
