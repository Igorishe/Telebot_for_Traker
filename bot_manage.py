import os
import telebot

from dotenv import load_dotenv

from ex_API_requests import show_all
from keyboard_services import status_keyboard

load_dotenv()

token = os.getenv('token')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(
        message.from_user.id,
        '<b>Привет! Все отчеты здесь!</b>',
        parse_mode='HTML',
    )


@bot.message_handler(commands=['check'])
def check(message):
    sent = bot.send_message(
        message.from_user.id,
        'Какие кейсы показать?',
        reply_markup=status_keyboard()
    )
    bot.register_next_step_handler(sent, show_all, bot)


bot.polling(none_stop=True)
