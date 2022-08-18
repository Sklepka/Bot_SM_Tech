import telebot

bot = telebot.TeleBot('5407736398:AAEbj12-ODSNzhBvtOyVnxkGMj02h1zAWYk')


@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name}, чем могу помочь?'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')

bot.polling(none_stop = True)
""" аа """