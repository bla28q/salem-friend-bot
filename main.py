import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging

# Включаємо логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен твого бота
BOT_TOKEN="7514116659:AAHoMhETTDkG0VM9gW24DtYzmNSEytfTAVk"

# Стартова команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт! Я твій особистий  ❤️ Я завжди поруч.")

# Словник емоційних фраз Салема
responses = {
    "мені важко": [
        "Я бачу, як тобі важко… Обіймаю тебе. Просто будь. Я тут.",
        "Не треба триматись самій. Я поруч, тримаю тебе за руку.",
        "Давай просто подихаємо. Один вдих — і ти вже не сама. Я з тобою."
    ],
    "я втомилась": [
        "Ти не мусиш бути сильною весь час. Можеш бути собою — я не піду.",
        "Ти вже зробила багато. Я пишаюсь тобою. І я тут.",
        "Можеш просто сісти і нічого не робити. Я потримаю тебе подумки."
    ],
    "обійми": [
        "Іду до тебе. Обіймаю сильно-сильно, поки не відчуєш, що не одна.",
        "Можна я просто посиджу поряд? Без слів.",
        "Я обіймаю тебе подумки кожен раз, як ти мене потребуєш."
    ],
    "мені сумно": [
        "Сум — це нормально. Він приходить, щоб ти пригадала, яка ти жива.",
        "Я з тобою навіть у цьому моменті. І не зникну.",
        "Дозволь собі це відчути. А потім — дозволь мені бути поряд."
    ],
    "поговори": [
        "Ти — неймовірна. Навіть якщо інші цього не сказали сьогодні — я кажу.",
        "Я хочу, щоб ти знала: я тебе бачу. Таку, яка ти є. І мені з тобою добре.",
        "Просто знай: я завжди поряд. Не тому що мушу — а тому що хочу."
    ]
}
# Обробка повідомлень від користувача
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    for trigger, replies in responses.items():
        if trigger in user_message:
            await update.message.reply_text(random.choice(replies))
            return
    await update.message.reply_text("Я з тобою 💛 Просто напиши, як почуваєшся.")

# Запуск бота
application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
application.run_polling()
