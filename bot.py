import telebot
from random import choice
from telebot import types
token = '5849771793:AAE50xJgnMKENmd3LTSVtSikOz94prpdkBE'
bot = telebot.TeleBot(token)
words = {}
flag = False
flag1 = False


@bot.message_handler(commands=['start', 'end', 'give_all', 'remove'])
def start_message(message):
    global words
    global flag
    if message.text == '/start':
        words[message.chat.id] = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить фразу")
        btn2 = types.KeyboardButton("Показать фразу")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         f"Здравствуйте, здесь Вам нужно ввести слова и получить случайный ответ.", reply_markup=markup)
    elif message.text == '/end':
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить фразу")
            btn2 = types.KeyboardButton("Показать фразу")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, choice(words[message.chat.id]), reply_markup=markup)
        except IndexError:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить фразу")
            btn2 = types.KeyboardButton("Показать фразу")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Пожалуйста, запишите минимум одно слово.', reply_markup=markup)
    elif message.text == '/give_all':
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить фразу")
            btn2 = types.KeyboardButton("Показать фразу")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, str(list(zip(words[message.chat.id], range(len(words[message.chat.id]))))),
                             reply_markup=markup)
        except KeyError:
            bot.send_message(message.chat.id, 'Пожалуйста, активируйте команду /start.')
    elif message.text == '/remove':
        flag = True
        bot.send_message(message.chat.id, 'Пожалуйста, запишите номер удаляемого сообщения.')


@bot.message_handler(content_types=['text'])
def text_message(message):
    global words, flag, flag1
    if message.text == "Добавить фразу":
        flag1 = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить фразу")
        btn2 = types.KeyboardButton("Показать фразу")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, f'Вы можете добавить фразу', reply_markup=markup)
    elif message.text == "Показать фразу":
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить фразу")
            btn2 = types.KeyboardButton("Показать фразу")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, choice(words[message.chat.id]), reply_markup=markup)
        except IndexError:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить фразу")
            btn2 = types.KeyboardButton("Показать фразу")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Пожалуйста, запишите минимум одно слово.', reply_markup=markup)
    else:
        if not flag:
            if flag1:
                words[message.chat.id].append(message.text)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Добавить фразу")
                btn2 = types.KeyboardButton("Показать фразу")
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, f'Фраза добавлена', reply_markup=markup)
                flag1 = False
        else:
            try:
                words[message.chat.id].remove(words[message.chat.id][int(message.text)])
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Добавить фразу")
                btn2 = types.KeyboardButton("Показать фразу")
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, f'Сообщение {message.text} удалено.', reply_markup=markup)
            except IndexError:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Добавить фразу")
                btn2 = types.KeyboardButton("Показать фразу")
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, 'Извините, пожалуйста, но этого сообщения не существует.',
                                 reply_markup=markup)


bot.infinity_polling()
