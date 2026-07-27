from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Trading Telegram Aktif!\n\n"
        "Perintah:\n"
        "/start\n"
        "/signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Analisis Contoh\n\n"
        "Pair: XAUUSD\n"
        "Trend: Bullish\n"
        "⚠️ Ini hanya contoh analisis, bukan jaminan hasil trading."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot sedang berjalan...")
app.run_polling()
