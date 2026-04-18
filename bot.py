import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = os.environ["TOKEN"]

def responder(update: Update, context: CallbackContext):
    texto = update.message.text.lower()

    if "hola" in texto:
        update.message.reply_text("Hola 👋 bot de la agenda de Tetuán activo")
    else:
        update.message.reply_text("Recibido 🙂")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, responder))

updater.start_polling()
updater.idle()
