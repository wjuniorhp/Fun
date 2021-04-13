import telebot
import time
from random import choice,betavariate, random as rnd,triangular
from time import gmtime, strftime, localtime
import os

with open("config.txt","r") as f:
    bot_token = f.readline()

bot = telebot.TeleBot(token=bot_token)

def write_log(xate):
    f = open('log.txt','a')
    now = strftime("%Y-%m-%d %H:%M:%S", localtime())
    log = f"{now}: {xate.first_name} {xate.last_name} (username={xate.username})\n" \
          f"\t\t\tchat id = {xate.id},\t chat type: {xate.type}" \
          f"\n\n"
    f.write(log)
    f.close()

def n_prus():
    return int((betavariate(1.8,10)*10)+1)

def extra1():
    extra = rnd()
    if 0.00<=extra<0.07:
        ponto = '!?'
    elif 0.2<=extra<0.27:
        ponto = '...'
    elif 0.4<=extra<0.5:
        ponto = '?'
    elif 0.6<=extra<0.7:
        ponto = '!'
    else:
        ponto=''
    return ponto
def extra2():
    extra = rnd()
    if 0.00<=extra<0.25:
        yay = ['PRUUUUUU!!!']
    elif 0.25<=extra<0.32:
        yay = ['PLOC!',u'\U0001f4a9']
    elif 0.5<=extra<0.6:
        yay = [u'\U0001f426'*(int(rnd()*4)+1)]
    else:
        yay=[]
    return yay

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message,'Pruuu (Cheguei!)')

@bot.message_handler(commands=['pru'])
def pru(message):
    write_log(message.chat)
    nlins = n_prus()
    if nlins == 1 and rnd()<=0.05:
        prum = '.--. .-. ..-    '
    else:
        prum = 'pru '
    for i in range(nlins):
        nprus = n_prus()
        bot.send_message(chat_id=message.chat.id,text=prum*nprus+extra1())
        time.sleep(triangular(0.1,1.0,0.3))

    for yayo in extra2():
        time.sleep(2)
        bot.send_message(chat_id=message.chat.id,text=yayo)

# bot.polling(none_stop=True,interval=1,timeout=20)
while True:
    try:
        bot.polling(none_stop=True,interval=1,timeout=10)
    except:
        time.sleep(15)