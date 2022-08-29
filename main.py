from telebot import types
import telebot

bot = telebot.TeleBot('5407736398:AAEbj12-ODSNzhBvtOyVnxkGMj02h1zAWYk')


@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name}, чем могу помочь?'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')


@bot.message_handler(commands=['employee_search'])
def employee_search(message):
    bot.send_message(message.chat.id, 'Поиск сотрудника - ДОДЕЛАТЬ', parse_mode='html')

@bot.message_handler(commands=['documentation_search'])
def documentation_search(message):
    bot.send_message(message.chat.id, 'Поиск документации - ДОДЕЛАТЬ', parse_mode='html')

@bot.message_handler(commands=['requisites'])
def requisites(message):
    requisites_all = f'<b>Адрес местонахождения(юридический и почтовый адрес):<\b>\n 196140, Санкт-Петербург г., Шушары п., Кокколевская(Пулковское тер.) ул., дом 1, стр.1,\nпом.45-Н\nтел. +7 (812) 331 94 44\nОГРН 1117847356417\nИНН 7820326027\nКПП 782001001\nОКВЭД 46.69.5, 27.12, 33.14, 33.20, 62.01, 62.02, 71.1, 71.12.5, 71.12.6 85.42.9\nОКПО 92088830'
    bot.send_message(message.chat.id, requisites_all, parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup() # описание дополнительной разметки, позволяет создавать встроенные вещи (кнопки, картинки ...)
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url='https://spbec-mining.ru/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)

 
@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)  # описание дополнительной разметки, позволяет создавать встроенные вещи (кнопки, картинки ...)
    website = types.KeyboardButton('/website')
    employee_search = types.KeyboardButton('/employee_search')
    documentation_search = types.KeyboardButton('/documentation_search')
    requisites = types.KeyboardButton('/requisites')
    markup.add(website, employee_search, documentation_search, requisites)
    bot.send_message(message.chat.id, 'Список доступных команд:', reply_markup = markup)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'И что мне делать с этим фото?')
    
    
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f"Твои ID: {message.from_user.id}", parse_mode='html')
    elif message.text.lower() == 'photo':
        logo = open('Logo.png', 'rb')
        bot.send_photo(message.chat.id, logo)
    else:
        bot.send_message(message.chat.id, "Введите '/help' для получения доступных команд", parse_mode='html')


bot.polling(none_stop = True)