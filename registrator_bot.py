import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import database

bot = telebot.TeleBot('6346928706:AAE6oHLLhtyouMCWKRGls_rqlQSRFWRJ6wk')
def main ():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)



    button1 = KeyboardButton('send phone')


    kb.add(button1)

    return kb

@bot.message_handler(commands=['start'])
def start(message):
    text = f'PON {message.from_user.first_name}!\nMEOW MEOW HI HI'
    bot.send_message(message.from_user.id, 'Hi this is it school say me ur name for lessens')

    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_name = message.text
    # print(user_name)



    bot.send_message(message.from_user.id, 'Send me Contact for ending regitration', reply_markup=main())
    bot.register_next_step_handler(message, get_phone, user_name)


def get_phone(message, user_name):
    if message.contact:
        user_phone = message.contact.phone_number


        database.register.user(user_name, user_phone, message.from_user.id)
        bot.send_message(message.from_user_id, f'FINE! You Verryfied regestration)\nName: {user_name}\nPhone: {user_phone}')

    else:
        bot.send_message(message.from_user.id, 'Send Contact with button under')
        bot.register_next_step_handler(message, get_phone, user_name)


bot.polling()