import os
import telebot

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أنا بوت تيليجرام بسيط. كيف يمكنني مساعدتك؟ 😊")

bot.polling()
