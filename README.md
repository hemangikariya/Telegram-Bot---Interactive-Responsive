# 🚀 Telegram Bot - Interactive & Responsive 🤖

This sophisticated Telegram bot offers seamless interaction through multiple commands, including polls, links to social profiles, and quick assistance features.

## ✨ Features

- `/start`: Initiates the bot with a warm welcome message.
- `/help`: Displays a comprehensive list of available commands.
- `/poll`: Engages users by creating an interactive poll.
- `/github`, `/linkedin`, `/gmail`, `/resume`, `/portfolio`: Provides quick access to professional links.
- Intelligent handling of unknown commands and messages.

## 🛠️ Prerequisites

- Python 3.7 or higher
- python-telegram-bot
- python-dotenv

## ⚙️ Setup Instructions

1. Clone or download this repository.
2. Create a `.env` file in the root directory and insert your Telegram Bot token as follows:
   TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
3. Install required dependencies:
   ```bash
   pip install python-telegram-bot python-dotenv
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

## 🚀 How to Test Your Bot

1. Search for your bot’s username in the Telegram app.
2. Start a chat and send commands like `/start` or `/poll`.
3. Watch your bot respond instantly with messages or polls.
4. Use `/poll` to initiate a live poll and engage users directly.

## ⚠️ Important Notes

- Ensure only one instance of the bot is running at a time to avoid conflicts.
- Never expose your `.env` file or token in public repositories.

---

Your powerful Telegram bot is now ready to engage users with dynamic features! 🎉🤖
