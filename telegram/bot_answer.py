from telegram import Update
from telegram.ext import ContextTypes
from weather import get_weather

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\n'
                                    f'Узнать погоду: /weather название_города')

async def weather_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_list = update.message.text.split(' ')
    if len(message_list) == 2:
        await update.message.reply_text(f'В городе {message_list[1]} за окном {get_weather(message_list[1])}')
    else:
        await update.message.reply_text(f'Вы ввели что-то неправильно. Попробуйте еще ращ')