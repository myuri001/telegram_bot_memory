import telebot
from telebot import types

bot = telebot.TeleBot('5392029038:AAFBhcftWuZxyjU6E6waIEID6rdm91DY9fI')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Функция получения сообщения от пользователя"""
    keyboard = types.InlineKeyboardMarkup()
    key_oven = types.InlineKeyboardButton(text='название кнопки', callback_data='ссылка кнопки')
    keyboard.add(key_oven)
    bot.send_message(message.from_user.id, text='сообщение пользователю', reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
