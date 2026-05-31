import telebot
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "دولت NGCoin فعال شد ✅")

print("Bot Started...")
bot.infinity_polling()