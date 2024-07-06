bot_api = ''
id_admin = 1
error_path = 'error.txt'

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot

bot = telebot.TeleBot(bot_api)


@bot.message_handler(commands=['start'])
def start(message): # обработка команды start
    bot.send_message(message.chat.id, 'Бот инициализирован')


try:
    bot.polling(non_stop = True)
except Exception as e:
    with open(error_path, 'w+', encoding='utf-8') as f:
        f.write(str(e) + "\n")
        goodbuy