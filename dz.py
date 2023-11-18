import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('6163310066:AAHk8r7tY7bPGQSGGa-Wr-GJKpqXoy1BFNM')


def pon():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)


    button2 = KeyboardButton('колабы игр')
    button3 = KeyboardButton('математика')
    button4 = KeyboardButton('год рождения создателей')


    kb.add(button2, button3, button4)


    return kb


@bot.message_handler(commands=['start'])
def start(message):
    text = f'Здравствуйте! {message.from_user.first_name}!\n Это бот опросник выберите категорию что бы отвечать нужно отвечать правельно a то бот не будет считывать это'
    bot.send_message(message.from_user.id, 'Выберите любой опросник для продолжения', reply_markup=pon())

    bot.register_next_step_handler(message, uxer_name)

def uxer_name(message):
    user_name = message.text
    # print(user_name)


    if 
    bot.send_message(message.from_user.id, 'Напишите мне c кем фортнайт делал калоборации', reply_markup=pon())
    bot.register_next_step_handler(message, user_name)

bot.polling()