import telebot
import requests
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from tabulate import tabulate
import pandas as pd
import time


bot = telebot.TeleBot('api key goes here')

def Button(message):
    keyboard= ['Product', 'Price']
    key = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    text = 'Hello {0} '.format(message.from_user.first_name,':D')
    for i in keyboard:
        button = KeyboardButton(i)
        key.add(button)
    bot.send_message(message.from_user.id, text, reply_markup=key)

@bot.message_handler(commands=['start'])
def start(message):
    Button(message)



@bot.message_handler(content_types='text')
def Send_Message(message):
    link = 'https://productstoreapi.herokuapp.com/api/text'
    text = {"text": message.text, "from_user": message.from_user.id, "first_name": message.from_user.first_name}
    user_id= {"from_user": message.from_user.id}

    print(user_id)
    print(text)
    r = requests.post(link, data=json.dumps(text))
    data = json.loads(r.text)

    if data['code'] == 401:
        bot.send_message(message.from_user.id, "Data can't be fetched or use the buttons again")
    elif data['text']=="Please enter the correct value":
        bot.send_message(message.from_user.id, "Please enter the correct value")
    elif data['text']== []:
        bot.send_message(message.from_user.id, "The entry doesn't exist")
    elif data['text'] == 'insert':
        bot.send_message(message.from_user.id,'Please type the query according to the selection. If you have selected "Price",'
                                              'you can search the products with the condition "greater than" & "less than".'
                                              'I.E- [greater 40000][less 40000] ')


    else:
        dic = data['text']
        # dic_final = []
        for a in dic:
            dic_tuple = list(a.items())
            dic_list = [list(ele) for ele in dic_tuple]
            # dic_final.append(dic_list)
            status = tabulate(dic_list, showindex=False)
            status1 = "<pre>{}</pre>".format(status)
            # dic_final.append(status)
            bot.send_message(message.from_user.id, status1, parse_mode='HTML')

bot.polling()


# while True:
#
#     try:
#         bot.polling()
#     except Exception:
#         time.sleep(5)