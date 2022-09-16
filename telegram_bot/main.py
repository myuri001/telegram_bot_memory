import telebot
from datetime import date, datetime
from telebot import types
import time
import schedule


def set_token():    # выводит токен
    file_token = '../token.txt'
    with open(file_token, 'r') as file:  # считывает токен из файла и закрывает его
        return file.readline()


bot = telebot.TeleBot(set_token())

@bot.message_handler(commands=['start'])
def start(message):    # Выводит клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/словарь_1")
    btn2 = types.KeyboardButton("/словарь_2")
    btn3 = types.KeyboardButton("/словарь_3")
    btn4 = types.KeyboardButton("/запомнить")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!\n Вспоминаем или запоминаем?".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['словарь_1'])
def question_dct1(message):  # при вводе словарь 1 выводит 'Привет', с кнопкой
    bot.send_message(message.chat.id,
                     f' Припоминаешь {get_in_dct1()}?',
                     reply_markup=get_keyboard())


def get_keyboard():    # функция кнопки при вводе start
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton('Yes', callback_data='set timer')
    button_no = telebot.types.InlineKeyboardButton('No', callback_data='set timer')
    keyboard.add(button_yes, button_no)
    return keyboard


def add_in_dct1(text):  # добавляет введеный пользователем текст в список
    dct1.append(text)

def get_in_dct1():
    for i in dct1:
        return i

@bot.message_handler(commands=['запомнить'])
def get_text_messages(message):    # Заносит в список и подтверждает занесение
    add_in_dct1(message.text)
    bot.send_message(message.chat.id,
                     f"принял {message.text} и добавл на дату {now}")

    print(dct1)


if __name__ == '__main__':

    dct1 = []
    dct2 = []
    dct3 = []
    now = date.today()
    while True:
        try:
            bot.polling()
        except:
            print('Что-то сломалось. Перезагрузка')

