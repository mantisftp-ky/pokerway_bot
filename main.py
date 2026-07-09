import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 Канал", url="https://t.me/pokerway2020")],
        [InlineKeyboardButton("💬 Личный Telegram", url="https://t.me/AlkseyZ")],
    ]

    text = (
        "Привет!\n\n"
        "Меня зовут Алексей Заворотный.\n\n"
        "Уже 10 лет тренирую регуляров с упором на GTO, "
        "ресёрчи поля и системный подход к обучению.\n\n"
        "Мне доверяют плюсовые реги NL100-NL2K."
        "Работаю без контрактов — люди остаются, потому что видят результат.\n\n"
        "Ниже можно перейти в канал или написать мне напрямую.\n"
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
