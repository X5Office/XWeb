import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebGK.settings")
django.setup()

from Core.config import TELEGRAM_BOT_TOKEN
from TelegramBot.registration.handler import registration_handler
from TelegramBot.datamitrix.dm import cmd_gdm, response_reacon
from TelegramBot.admin_mode.handler import cdm_shift
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(registration_handler())
    application.add_handler(CommandHandler("gdm", cmd_gdm))
    application.add_handler(CommandHandler("shift", cdm_shift))
    application.add_handler(CallbackQueryHandler(response_reacon))
    application.run_polling()

if __name__ == '__main__':
    main()
