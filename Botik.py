import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('6346928706:AAE6oHLLhtyouMCWKRGls_rqlQSRFWRJ6wk')





def main_menu_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)




    # button1 = KeyboardButton('когда родился билл гейтс')
    # button2 = KeyboardButton('когда родился дэвид базуке')
    # button3 = KeyboardButton('когда родился илон маск')
    # button4 = KeyboardButton('когда родился илон маск')
    # button5 = KeyboardButton('когда родился стив роджерс')
    button1 = KeyboardButton('контакты')
    button2 = KeyboardButton('наш адрес')
    button3 = KeyboardButton('про нас')
    button4 = KeyboardButton('каталог')
    button5 = KeyboardButton('сотрудничество')




    kb.add(button1, button2, button3, button4, button5)




    return kb



def BOTIK():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button5 = KeyboardButton('catalog of pets')

    button1 = KeyboardButton('каталог')
    button2 = KeyboardButton('cats')
    
    catalog = ['chototo', 'PC', 'HZ']


    kb.add(button1,button2,button5)
    
    return kb

def TIK():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button5 = KeyboardButton('GAGA')

    button1 = KeyboardButton('GAGIK')
    button2 = KeyboardButton('GORIK')
    
    log = ['GHGA', 'GAG', 'GG']


    kb.add(button1,button2,button5)
    
    return kb




def COTIK():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button5 = KeyboardButton('cot')

    button1 = KeyboardButton('coshak')
    button2 = KeyboardButton('cats')
    
    talog = ['lalog', 'coshki', 'HZ']


    kb.add(button1,button2,button5)
    
    return kb




def KOTIK():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button5 = KeyboardButton('HZ')

    button1 = KeyboardButton('HZ')
    button2 = KeyboardButton('hz')
    
    cat = ['lk', 'np', 'pn']


    kb.add(button1,button2,button5)
    
    return kb




def TIK():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button5 = KeyboardButton('ponpik')

    button1 = KeyboardButton('pon')
    button2 = KeyboardButton('ponchik') 
    
    catalog = ['CHOTOTO', 'PONNNNN', 'ZH']


    kb.add(button1,button2,button5)
    
    return kb

@bot.message_handler(commands=['start', 'hello'])
def start_messege(message):

    text = f'Meowwww {message.from_user.first_name}!\nMeow hi))'
    bot.send_message(message.from_user.id, text, reply_markup=main_menu_button())
    

    print(message.from_user.id)


@bot.message_handler(commands=['qrcode'])
def qrcode_coma(message):
    with open('./qr_code.png', 'rb') as qr_photo:
            bot.send_photo(message.from_user.id, qr_photo)



@bot.message_handler(content_types=['text'])
def mecho(message):

    # bot.send_message(message.from_user.id, message.text)
    # print(message.text)




    if message.text.lower() =='hello':
        bot.send_message(message.from_user.id, 'hi how i can help u?')

    # elif message.text.lower() =='когда родился стив джобс':
    #     bot.send_message(message.from_user.id, '24 февраля 1955 года.')

    # elif message.text.lower() =='когда родился илон маск':
    #     bot.send_message(message.from_user.id, '28 июня 1971 года')

    # elif message.text.lower() =='когда родился дэвид базуке':
    #     bot.send_message(message.from_user.id, '20 января 1963 года')

    # elif message.text.lower() =='когда родился билл гейтс':
    #     bot.send_message(message.from_user.id, '28 октября 1955 года')

    # elif message.text.lower() =='когда родился стив роджерс':
    #     bot.send_message(message.from_user.id, '4 июля 1918 года')

    elif message.text.lower() =='про нас':
        bot.send_message(message.from_user.id, 'мы марс айти учим за 100 миллиардов$  в неделю')

    elif message.text.lower() =='наш адрес':
        bot.send_message(message.from_user.id, 'Улица лоха дом лохатрона')

    elif message.text == 'каталог':
        bot.send_message(message.from_user.id, 'Выберите' ,reply_markup=BOTIK())
        
    elif message.text == 'контакты':
        bot.send_message(message.from_user.id, 'Выберите' ,reply_markup=TIK())

    elif message.text == 'сотрудничество':
        bot.send_message(message.from_user.id, 'Выберите' ,reply_markup=KOTIK())



    elif message.text.lower() =='кантакты':
        bot.send_message(message.from_user.id, '+667 66 666 77')

    elif message.text == 'Telephones':
        bot.send_message('IPHONES', 'NOKIA', 'XIAOMI', 'SONY')
        with open('./ppp.png', 'rb') as qr_photo:
            bot.send_photo(message.from_user.id, qr_photo)








    elif message.text.lower == 'catalog':
        catalog = ['PC','Acsessuares', 'PETS']



    elif message.text.lower() == 'ekjgjgpoejejfcmefnecefefxgrg4chn3cf4hr778944':
        bot.send_message(message.from_user.id, 'u activated this secret function what u want?')


    elif message.text.lower() =='who created u?':
        bot.send_message(message.from_user.id, 'my creator is サイダブラ')

    elif message.text.lower() == '11010000 10011011 11010000 10011110 11010000 10011011 100000 11010000 10100010 11010000 10101011 100000 11010000 10100000 11010000 10010101 11010000 10010000 11010000 10011011 11010000 10101100 11010000 10011101 11010000 10011110 100000 11010000 10011111 11010000 10011110 11010000 10101000 11010000 10010101 11010000 10011011 100000 11010000 10101101 11010000 10100010 11010000 10011110 100000 100000 11010000 10011111 11010000 10010101 11010000 10100000 11010000 10010101 11010000 10010010 11010000 10011110 11010000 10010100 11010000 10011000 11010000 10100010 11010000 10101100 111111':
        bot.send_message(message.from_user.id, "WTH WHAT U SAY can u translate it? in https://decodeit.ru/binary?ysclid=ll1vf50crd56323779 please")
    elif message.text.lower() == 'ЛОЛ ТЫ РЕАЛЬНО ПОШЕЛ ЭТО ПЕРЕВОДИТЬ?':
        bot.send_message(message.from_user.id, "BROOOOOOOOOOO WHAT U SAY BRO")

    elif message.text.lower() == 'wth':
        bot.send_message(message.from_user.id, "LOL XD")

    elif message.text.lower() == 'BRO':
        bot.send_message(message.from_user.id, "WHAT")

    elif message.text.lower() == 'U CAN SWEEM?':
        bot.send_message(message.from_user.id, "50% ON 50%")

    elif message.text.lower() == 'qrcode':
        with open('./qr_code.png', 'rb') as qr_photo:
            bot.send_photo(message.from_user.id, qr_photo)



@bot.message_handler(content_types=['photo'])
def photo_message(message):
    

    file = message.photo[-1].file_id
    print(file)


    bot.send_photo(message.from_user.id, file)



@bot.message_handler(content_types=['sticker'])
def sticker_message(message):
    

    sticker = message.sticker.file_id


    bot.send_sticker(message.from_user.id, sticker)




@bot.message_handler(content_types=['video'])
def video_message(message):
    video = message.video.file.id



    bot.send_video(message.from_user.id, video)




@bot.message_handler(content_types=['audio'])
def audio_message(message):
    audio = message.audio.file.id




    bot.send_audio(message.from_user.id, audio)



bot.polling()