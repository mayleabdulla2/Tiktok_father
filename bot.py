import logging
from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from handlers.start_handler import start
from handlers.report_handler import report

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("report", report))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()