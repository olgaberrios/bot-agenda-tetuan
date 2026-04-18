import os

print("🚀 INICIO BOT")

TOKEN = os.environ.get("TOKEN")

print("TOKEN RAW:", TOKEN)

if not TOKEN:
    print("❌ ERROR: TOKEN NO ENCONTRADO")
    raise SystemExit("SIN TOKEN")

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

print("📦 librerías cargadas")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("OK 👋")

app = ApplicationBuilder().token(TOKEN).build()

print("🤖 BOT CONSTRUIDO")

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("▶️ RUNNING")

app.run_polling()
