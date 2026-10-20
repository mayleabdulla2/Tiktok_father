from telegram import Update
from telegram.ext import CallbackContext
from utils.proxy_manager import load_proxies
from utils.session_manager import load_sessions
from utils.report_sender import send_fake_report

def report(update: Update, context: CallbackContext) -> None:
    target = update.message.text.split(' ')[1] if len(update.message.text.split(' ')) > 1 else None
    if not target:
        update.message.reply_text('Please provide a target username.')
        return

    proxies = load_proxies()
    sessions = load_sessions()

    for proxy in proxies:
        for session in sessions:
            send_fake_report(target, proxy, session)

    update.message.reply_text(f'Fake reports sent to {target}.')