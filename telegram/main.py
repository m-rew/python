from telegram.ext import ApplicationBuilder, CommandHandler
import bot_answer

app = ApplicationBuilder().token("5959586307:AAHg6Jpsqc4qEv4eTgsSn4SXjvI8EO482QY").build()

app.add_handler(CommandHandler("start", bot_answer.start_callback))
app.add_handler(CommandHandler("weather", bot_answer.weather_callback))

app.run_polling()