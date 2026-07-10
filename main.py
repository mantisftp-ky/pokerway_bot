import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 Канал", url="https://t.me/pokerway2020")],
    ]

    welcome_text = (
    "Привет!\n\n"
    "Добро пожаловать в официальный бот Pokerway.\n\n"
    "В канале публикуются:\n\n"
    "— разборы раздач против регуляров и любителей;\n"
    "— материалы по GTO и эксплойтной стратегии;\n"
    "— анализ типичных ошибок на постфлопе;\n"
    "— разборы современных тенденций поля;\n"
    "— обучающие материалы и комментарии Алексея Заворотного.\n\n"
    "Если хотите системно развивать игру, нажмите кнопку ниже и перейдите в канал."
)

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
