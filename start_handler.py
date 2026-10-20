from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Use /report to send a fake report.')