import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.environ["TOKEN"]

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "hola" in texto:
        await update.message.reply_text("Hola 👋 bot de la agenda de Tetuán activo")
    else:
        await update.message.reply_text("Recibido 🙂")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

app.run_polling()
