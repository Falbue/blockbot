bot_api = '460121789:AAES7eBIToqjxSICY3qnxDG-ZNXIwg12vYA'  # Здесь нужно указать ваш токен бота
id_admin = 1210146115  # Укажите ID администратора
error_path = 'error.txt'

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import os
import signal

bot = telebot.TeleBot(bot_api)

@bot.message_handler(commands=['start'])
def start(message):  # обработка команды start
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("Закрыть приложение", callback_data="close_app")
    markup.add(btn)
    bot.send_message(message.chat.id, 'Бот инициализирован', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "close_app")
def handle_query(call):
    if call.data == "close_app":
        bot.send_message(call.message.chat.id, "Приложение закрывается...")
        # Завершаем приложение
        os.kill(os.getppid(), signal.SIGTERM)

try:
    bot.polling(non_stop=True)
except Exception as e:
    with open(error_path, 'w+', encoding='utf-8') as f:
        f.write(str(e) + "\n")
