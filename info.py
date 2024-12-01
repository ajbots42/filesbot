from telegram import Update
from telegram.ext import ContextTypes

# Define the /info command
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🤖 *Bot Information* 🤖\n"
        "I am a Telegram bot created to assist with various tasks and provide information.\n\n"
        "*Features:*\n"
        "- Respond to commands like /start and /help.\n"
        "- Echo back messages with /echo.\n"
        "- Share useful info with /info.\n\n"
        "For more details, contact my developer."
    )
    await update.message.reply_text(message, parse_mode="Markdown")

# Define the /about command
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🔍 *About Me* 🔍\n"
        "This bot was developed using Python and the `python-telegram-bot` library. "
        "It serves as an example to demonstrate Telegram bot functionality. "
        "Feel free to extend my capabilities!"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

# Define the /developer command
async def developer_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👨‍💻 *Developer Info* 👨‍💻\n"
        "Created by [Your Name or Username].\n"
        "Contact: [email@example.com](mailto:email@example.com)\n"
        "GitHub: [https://github.com/your-username](https://github.com/your-username)"
    )
    await update.message.reply_text(message, parse_mode="Markdown")
