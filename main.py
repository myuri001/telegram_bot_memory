import telebot
from telebot import types

token = '5392029038:AAFBhcftWuZxyjU6E6waIEID6rdm91DY9fI'
bot = telebot.TeleBot(token)

tasks = dict()


HELP = '''
Список доступных команд:
/add - добавить выученное
/show - показать всё
'''

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1]
    task = command[2]
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
    print(tasks)
@bot.message_handler(commands=['show'])
def show(message):
    for i in tasks.items():
        bot.send_message(message.chat.id, i)

bot.polling(none_stop=True)
