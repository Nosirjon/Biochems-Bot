import telebot
from telebot import types
from aiogram.types.web_app_info import WebAppInfo

bot = telebot.TeleBot('6930334902:AAET2Fy__jWI9ByGmPwJMqFD3WOQwDekD-U')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.InlineKeyboardButton(text='Посетить сайт', web_app=types.WebAppInfo(url='https://biochems.uz')))
    bot.send_message(message.chat.id,
                     text='Добро пожаловать на наш бот, на данный момент бот находиться на стадий разработки пака же то вы можите поситить наш сайт нажав на кнопочку ниже в меню.',
                     reply_markup=markup)


bot.polling(non_stop=True)
