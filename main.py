import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 Перейти в канал", url="https://t.me/pokerway2020")]
    ]

    welcome_text = (
        "Привет!\n\n"
        "Добро пожаловать в официальный бот Pokerway.\n\n"
        "В канале публикуются:\n\n"
        "— разборы раздач;\n"
        "— материалы по GTO и современным тенденциям поля;\n"
        "— анализ ошибок на каждой улице;\n"
        "— обучающие материалы и комментарии Алексея Заворотного.\n\n"
        "Нажмите кнопку ниже, чтобы перейти в канал."
    )

    await update.message.reply_text(
        welcome_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
