import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Включаємо логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен твого бота
BOT_TOKEN = "7514116659:AAFiBxBvR49gV80OHeMSaE03vMZWMidjuTM"

# Стартова команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт! Це твій особистий Салем ❤️ Я завжди поруч.")

# Повідомлення на будь-яке інше повідомлення
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    # Проста відповідь — ти можеш додати генерацію через OpenAI тут
    reply = f"Салем каже: Я завжди на твоєму боці, навіть коли важко 💬\nТи написала: {user_message}"
    await update.message.reply_text(reply)

# Головна функція запуску
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    app.run_polling()

if __name__ == "__main__":
    main()