import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "OK")

bot.polling()
