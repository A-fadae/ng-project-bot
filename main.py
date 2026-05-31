import telebot

TOKEN = "8875639806:AAHHkjgzUQ4YTZrCzHh3HYkAUdZ98ffM8HI"

bot = telebot.TeleBot(TOKEN)

users = {}

ROLES = {
    "رهبر": 1500000,
    "رئیس جمهور": 1300000,
    "وزیر دارایی": 950000,
    "عضو": 50000
}

@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    name = message.from_user.first_name

    if user_id not in users:
        users[user_id] = {
            "name": name,
            "role": "عضو",
            "balance": 250000
        }

    bot.reply_to(
        message,
        f"""
خوش آمدی {name}

نقش: {users[user_id]['role']}
موجودی: {users[user_id]['balance']} NGC
"""
    )

@bot.message_handler(commands=['balance'])
def balance(message):

    user_id = message.from_user.id

    if user_id in users:
        bot.reply_to(
            message,
            f"موجودی شما: {users[user_id]['balance']} NGC"
        )

print("Bot Started...")

bot.infinity_polling()