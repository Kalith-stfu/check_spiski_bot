import telebot
from telebot import types
from pars import ngueu_fi, ngueu_pi, sibguti_fi,sibguti_ib,sibguti_ist,sibguti_ivt,sibguti_pi,kemgu_fi,kemgu_mo,kemgu_pi,kemgu_pim

token=open('token.txt').readline()

bot=telebot.TeleBot(token)

#КЕМГУ
def input_snils_kemgu_fi(message):
    x= message.text
    bot.send_message(message.chat.id, kemgu_fi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_kemgu_mo(message):
    x= message.text
    bot.send_message(message.chat.id, kemgu_mo(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_kemgu_pi(message):
    x= message.text
    bot.send_message(message.chat.id, kemgu_pi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_kemgu_pim(message):
    x= message.text
    bot.send_message(message.chat.id, kemgu_pim(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')


#CИБГУТИ
def input_snils_sibguti_fi(message):
    x= message.text
    bot.send_message(message.chat.id, sibguti_fi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_sibguti_ib(message):
    x= message.text
    bot.send_message(message.chat.id, sibguti_ib(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_sibguti_ist(message):
    x= message.text
    bot.send_message(message.chat.id, sibguti_ist(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_sibguti_ivt(message):
    x= message.text
    bot.send_message(message.chat.id, sibguti_ivt(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')
def input_snils_sibguti_pi(message):
    x= message.text
    bot.send_message(message.chat.id, sibguti_pi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')


#НГУЭУ
def input_snils_ngueu_fi(message):
    x= message.text
    bot.send_message(message.chat.id, ngueu_fi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')

def input_snils_ngueu_pi(message):
    x= message.text
    bot.send_message(message.chat.id, ngueu_pi(x))
    bot.send_message(message.chat.id, 'Для продолжения /start')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("НГУЭУ")
    item2 = types.KeyboardButton("СИБГУТИ (часто тупят сервера)")
    item3 = types.KeyboardButton("КЕМГУ")
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id,"Выбери в каком ВУЗе смотреть своё место",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type=='private':
        if message.text=="НГУЭУ":
            markup_ngu=types.ReplyKeyboardMarkup(resize_keyboard=True)
            napr_ngu_1=types.KeyboardButton("Фундаментальная информатика(НГУЭУ)")
            napr_ngu_2=types.KeyboardButton("Прикладная информатика(НГУЭУ)")
            markup_ngu.add(napr_ngu_1,napr_ngu_2)
            bot.send_message(message.chat.id,"Выбери направление",reply_markup=markup_ngu)


        elif message.text=="СИБГУТИ (часто тупят сервера)":
            markup_sibguti=types.ReplyKeyboardMarkup(resize_keyboard=True)
            napr_sibguti_1=types.KeyboardButton("Фундаментальная информатика(СИБГУТИ)")
            napr_sibguti_2=types.KeyboardButton("Прикладная информатика(СИБГУТИ)")
            napr_sibguti_3=types.KeyboardButton("Информационные системы и технологии(СИБГУТИ)")
            napr_sibguti_4=types.KeyboardButton("Информатика и вычислительная техника(СИБГУТИ)")
            napr_sibguti_5=types.KeyboardButton("Информационная безопасность(СИБГУТИ)")
            markup_sibguti.add(napr_sibguti_1,napr_sibguti_2,napr_sibguti_3,napr_sibguti_4,napr_sibguti_5)
            bot.send_message(message.chat.id,"Выбери направление",reply_markup=markup_sibguti)

        elif message.text=='КЕМГУ':
            markup_kemgu=types.ReplyKeyboardMarkup(resize_keyboard=True)
            napr_kemgu_1=types.KeyboardButton("Фундаментальная информатика(КЕМГУ)")
            napr_kemgu_2=types.KeyboardButton("Прикладная информатика(КЕМГУ)")
            napr_kemgu_3=types.KeyboardButton("Сис админ крч(КЕМГУ)")
            napr_kemgu_4=types.KeyboardButton("Прикладная математика и информатика(КЕМГУ)")
            markup_kemgu.add(napr_kemgu_1,napr_kemgu_2,napr_kemgu_3,napr_kemgu_4)
            bot.send_message(message.chat.id,"Выбери направление",reply_markup=markup_kemgu)

        
        elif message.text=='Фундаментальная информатика(НГУЭУ)':
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_ngueu_fi)
        elif message.text=="Прикладная информатика(НГУЭУ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_ngueu_pi)
        
        elif message.text=="Фундаментальная информатика(КЕМГУ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_kemgu_fi)
        elif message.text=="Прикладная информатика(КЕМГУ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_kemgu_pi)
        elif message.text=="Сис админ крч(КЕМГУ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_kemgu_mo)
        elif message.text=="Прикладная математика и информатика(КЕМГУ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_kemgu_pim)

        elif message.text=="Фундаментальная информатика(СИБГУТИ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_sibguti_fi)
        elif message.text=="Прикладная информатика(СИБГУТИ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_sibguti_pi)
        elif message.text=="Информационные системы и технологии(СИБГУТИ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_sibguti_ist)
        elif message.text=="Информатика и вычислительная техника(СИБГУТИ)":
            msg = bot.send_message(message.chat.id,'Напиши мне свой СНИЛС')
            bot.register_next_step_handler(msg,input_snils_sibguti_ivt)


        
        else:
            bot.send_message(message.chat.id,'ди нах')

bot.polling(none_stop=True)