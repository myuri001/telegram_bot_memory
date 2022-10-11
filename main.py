import telebot
from datetime import date
from telebot import types
from envparse import Env

env = Env()
TOKEN = env.str("TOKEN")
ADMIN_CHAT_ID = env.int("ADMIN_CHAT_ID")


bot = telebot.TeleBot(token=TOKEN)

# Проверка бота на включенное состояние и выводит клавиатуру с кнопками
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/словарь_1")
    btn2 = types.KeyboardButton("/словарь_2")
    btn3 = types.KeyboardButton("/словарь_3")
    btn4 = types.KeyboardButton("/запомнить")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!\n Я готов!".format(message.from_user), reply_markup=markup)

# Показывает элемент и спрашивает помню или нет
@bot.message_handler(commands=['словарь_1'])
def question_dct1(message):
    text_dct1 = get_in_dct(dct1)
    if text_dct1 is None:
        bot.send_message(message.chat.id, f' Словарь 1 пуст')
    else:
        bot.send_message(message.chat.id, f' Помнишь {text_dct1}?', reply_markup=get_keyboard())


@bot.message_handler(commands=['словарь_2'])
def question_dct2(message):
    text_dct2 = get_in_dct(dct2)
    if text_dct2 is None:
        bot.send_message(message.chat.id, f'Словарь 2 пуст')
    else:
        bot.send_message(message.chat.id, f' Помнишь {text_dct2}?', reply_markup=get_keyboard2())


@bot.message_handler(commands=['словарь_3'])
def question_dct3(message):
    text_dct3 = get_in_dct(dct3)
    if text_dct3 is None:
        bot.send_message(message.chat.id, f'Словарь 3 пуст')
    else:
        bot.send_message(message.chat.id, f' Помнишь {text_dct3}?', reply_markup=get_keyboard3())

# Выводит кнопки Yes и No
def get_keyboard():
    button_command_yes = 'button_command_yes_dct1'
    button_command_no = 'button_command_no_dct1'
    button_name_yes = 'Yes'
    button_name_no = 'No'
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton(button_name_yes, callback_data=button_command_yes)
    button_no = telebot.types.InlineKeyboardButton(button_name_no, callback_data=button_command_no )
    keyboard.add(button_yes, button_no)
    return keyboard


def get_keyboard2():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton('Yes', callback_data='Yes2')
    button_no = telebot.types.InlineKeyboardButton('No', callback_data='No2')
    keyboard.add(button_yes, button_no)
    return keyboard


def get_keyboard3():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton('Yes', callback_data='Yes3')
    button_no = telebot.types.InlineKeyboardButton('No', callback_data='No3')
    keyboard.add(button_yes, button_no)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # Реагирует на кнопки.
    # Если Yes, то добавляет элемент в список выше.
    # Если No, то возвращает в список 1 и удаляет из текущего списка
    if call.data == "button_command_yes_dct1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Убрал в словарь 2")
        add_dct2()
        delete_dct1()
    elif call.data == "button_command_no_dct1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вернул в словарь 1")
        add_dct1(dct1[0])
        delete_dct1()

    elif call.data == "Yes2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Убрал в словарь 3")
        add_dct3()
        delete_dct2()
    elif call.data == "No2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вернул в словарь 1")
        add_dct1(dct2[0])
        delete_dct2()

    elif call.data == "Yes3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добавил в конец словаря 3")
        add_dct33()
        delete_dct3()

    elif call.data == "No3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вернул в словарь 1")
        add_dct1(dct3[0])
        delete_dct3()

# Удаляют элементы из списков
def delete_dct1():
    del dct1[0]


def delete_dct2():
    del dct2[0]


def delete_dct3():
    del dct3[0]

# Добавляет элементы в списки
def add_dct1(text):
    dct1.append(text)

# Добавляет элементы из списка 2 в конец списка 3
def add_dct2():
    dct2.append(dct1[0])


def add_dct3():
    dct3.append(dct2[0])


def add_dct33():
    dct3.append(dct3[0])

# вытягивают из списков элементы
def get_in_dct(dct):
    for i in dct:
        return i


# Добавляет введеное с клавиатуры слово в список 1 и выводит подтверждение
@bot.message_handler(commands=['запомнить'])
def get_text_messages(message):    # Заносит в список и подтверждает занесение
    add_dct1(message.text)
    bot.send_message(message.chat.id, f"принял {message.text} и добавл на дату {now}")


if __name__ == '__main__':

    dct1 = ['A', 'B']
    dct2 = []
    dct3 = []
    now = date.today()
    while True:
        try:
            bot.polling()
        except:
            print('Что-то сломалось. Перезагрузка')

