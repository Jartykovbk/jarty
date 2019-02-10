#!/usr/bin/env python

import telebot

TOKEN = '709201343:AAEM2nkgGPGbzYkI3MHHETNXvzkl3p-u9i4'

bot = telebot.TeleBot(TOKEN)

def log(message, answer):
    print('\n')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1} , (id = {2}) \n Текст - {3}'.format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    #user_markup.row("🇺🇿O'zbek tili")
    user_markup.row("🇷🇺Русский язык")
    user_markup.row("↗Перейти на наш канал")
    answer = 'FashionWorldBot:' \
             '\n🇷🇺Добро пожаловать! \nПожалуйста выберите свой язык .' \
             #'\n🇺🇿Xush kelibsiz! Iltimos, tilingizni tanlang.'
    log(message, answer)
    bot.send_message(message.from_user.id, answer , reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    answer = 'Хотите заказать бота для вашей организации ?' \
             '\n То смело заказывайте у меня @artykov013' \
             '\n Информационный бот о моих услугах t.me/kingdeveloperbot '
    log(message, answer)
    bot.reply_to(message, answer)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == '🛍Заказать товар':
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = telebot.types.KeyboardButton(text='📞Отправить номер телефона', request_contact=True)
        button_geo = telebot.types.KeyboardButton(text='🌐Отправить геолокацию', request_location=True)
        button_hub = telebot.types.KeyboardButton(text='🔙Назад')
        keyboard.add(button_phone,button_geo,button_hub)
        answer = 'Если вы перешли на это меню , ' \
                 '\nзначит вы заинтересованы покупкой ' \
                 '\nтоваров с нашего интернет магазина .' \
                 '\nДля того чтобы заказать товар вы' \
                 '\nдолжны выполнить три действия :' \
                 '\n1.Перейти на наш канал \nt.me/fashionworld_uzbekistan' \
                 '\n2.Выбрать товар из нашего интернет машазина' \
                 '\n3.Отправить его прямо сейчас и поделиться вашим ' \
                 '\nномером телефона и геолокацией .' \
                 '\nПосле этих трех шагов мы с вами свяжемся' \
                 '\nдля уточнения некоторых делатей заказа .' \
                 '\nИ уже в скором времени вы получите свой заказ .'


        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=keyboard)
    elif message.text == '🔝Перейти в меню выбора языка':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        #user_markup.row("🇺🇿O'zbek tili")
        user_markup.row("🇷🇺Русский язык")
        answer = 'Вы перешли в меню выбора языка.'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🇷🇺Русский язык':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("↗Перейти на наш канал",'📞Контактная информация')
        user_markup.row("🛍Заказать товар",'🔝Перейти в меню выбора языка')
        answer = 'Вы перешли в меню выбора языка.'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🔙Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("↗Перейти на наш канал",'📞Контактная информация')
        user_markup.row("🛍Заказать товар",'🔝Перейти в меню выбора языка')
        answer = 'Вы перешли в меню выбора языка.'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '📞Контактная информация':
        bot.send_message(message.from_user.id , '📞Контактная информация'
                                                '\n+998 94 6119619 ')
    elif message.text == '↗Перейти на наш канал':
        bot.send_message(message.from_user.id , 't.me/fashionworld_uzbekistan\nНажми на ссылку сверху🔝')

    else:
        bot.send_message(message.from_user.id , 'В моей базе данных нет ответа на ваше сообщение .')

@bot.message_handler(content_types=['location'])
def user_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    answer = 'Адресс покупателя {0} : {1},{2}'.format(message.from_user.first_name, lat, lon)
    bot.send_message(554625440, answer)

@bot.message_handler(content_types=['contact'])
def user_contact(message):
    answer = 'Заказ пришел от покупателя :{0} ,\nНомер телефона : {1}'.format(message.from_user.first_name,
                                                                              message.contact.phone_number)
    bot.send_message(554625440, answer)


bot.polling(none_stop=True)