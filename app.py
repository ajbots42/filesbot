from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Flask app
app = Flask(__name__)

# Telegram bot application
application = Application.builder().token(BOT_TOKEN).build()

# Define the start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot running in a web app.")

# Define the help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - List available commands")

# Define the echo message handler
async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Set up Telegram bot handlers
application.add_handler(CommandHandler("start", start_command))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

# Flask route for the bot's webhook
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "OK"

# Route to set up the webhook
@app.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
    webhook_url = f"https://YOUR_DOMAIN/{BOT_TOKEN}"
    application.bot.set_webhook(webhook_url)
    return f"Webhook set to {webhook_url}"

# Main entry point for Flask app
if __name__ == "__main__":
    app.run(port=5000, debug=True)
