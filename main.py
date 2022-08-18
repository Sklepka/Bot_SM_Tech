from telebot import types
import telebot

bot = telebot.TeleBot('5407736398:AAEbj12-ODSNzhBvtOyVnxkGMj02h1zAWYk')


@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name}, чем могу помочь?'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup() # описание дополнительной разметки, позволяет создавать встроенные вещи (кнопки, картинки ...)
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url='https://spbec-mining.ru/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)  # описание дополнительной разметки, позволяет создавать встроенные вещи (кнопки, картинки ...)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup = markup)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')
    
    
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твои ID: {message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':
        logo = open('Logo.png', 'rb')
        bot.send_photo(message.chat.id, logo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop = True)
