# bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from backend.database import Database
from backend.telegram import TelegramAPI
from backend.utils import calculate_remaining_days, calculate_earnings

# Your bot token
TOKEN = "YOUR_BOT_TOKEN"

# Create an instance of the Updater class
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Create instances of Database and TelegramAPI
db = Database("database/users.json", "database/issues.json")
telegram_api = TelegramAPI(TOKEN)

# Register the "/start" command handler
def start_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if not db.user_exists(user_id):
        db.register_user(user_id)
        context.bot.send_message(chat_id=chat_id, text="Welcome to the Telegram bot!")

start_handler = CommandHandler('start', start_handler)
dispatcher.add_handler(start_handler)

# Register the "/register" command handler
def register_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if not db.user_exists(user_id):
        context.bot.send_message(chat_id=chat_id, text="Please enter your tracking ID.")
        context.user_data["register"] = True
    else:
        context.bot.send_message(chat_id=chat_id, text="You are already registered.")

register_handler = CommandHandler('register', register_handler)
dispatcher.add_handler(register_handler)

# Register the message handler for tracking ID
def tracking_id_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if "register" in context.user_data:
        tracking_id = update.message.text.strip()

        if tracking_id:
            db.set_tracking_id(user_id, tracking_id)
            context.bot.send_message(chat_id=chat_id, text="You have successfully registered.")
        else:
            context.bot.send_message(chat_id=chat_id, text="Invalid tracking ID.")

        del context.user_data["register"]
    else:
        context.bot.send_message(chat_id=chat_id, text="Invalid command.")

tracking_id_handler = MessageHandler(Filters.text & (~Filters.command), tracking_id_handler)
dispatcher.add_handler(tracking_id_handler)

# Register the "/countdown" command handler
def countdown_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    tracking_id = db.get_tracking_id(user_id)
    if tracking_id:
        remaining_days = calculate_remaining_days(tracking_id)
        earnings = calculate_earnings(remaining_days)
        context.bot.send_message(chat_id=chat_id, text=f"Remaining days: {remaining_days}\nEarnings: {earnings} Naira")
    else:
        context.bot.send_message(chat_id=chat_id, text="You are not registered.")

countdown_handler = CommandHandler('countdown', countdown_handler)
dispatcher.add_handler(countdown_handler)

# Register the "/report" command handler
def report_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    context.bot.send_message(chat_id=chat_id, text="Please enter your issue.")
    context.user_data["report"] = True

report_handler = CommandHandler('report', report_handler)
dispatcher.add_handler(report_handler)

# Register the message handler for reporting issues
def issue_handler(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if "report" in context.user_data:
        issue_text = update.message.text.strip()

        if issue_text:
            db.report_issue(user_id, issue_text)
            context.bot.send_message(chat_id=chat_id, text="Your issue has been reported.")
        else:
            context.bot.send_message(chat_id=chat_id, text="Invalid issue text.")

        del context.user_data["report"]
    else:
        context.bot.send_message(chat_id=chat_id, text="Invalid command.")

issue_handler = MessageHandler(Filters.text & (~Filters.command), issue_handler)
dispatcher.add_handler(issue_handler)

# Start the bot
updater.start_polling()
