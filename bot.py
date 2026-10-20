from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Send TikTok Profile", callback_data='send_tiktok')],
        [InlineKeyboardButton("Report Profile", callback_data='report_profile')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'send_tiktok':
        query.edit_message_text(text="Please send the TikTok profile link you want to ban.")
        return

    elif query.data == 'report_profile':
        query.edit_message_text(text="Please send the report details for the TikTok profile.")
        return

def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    update.message.reply_text(f"You sent: {user_input}")

def main() -> None:
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("8966934790:AAFDp9p4pGTz39TmTxJ1SUapakrUGVligDk")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
