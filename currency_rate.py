from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from datetime import datetime

def cur_rate(update: Update, context: CallbackContext):
    msg = update.message.text
    msg = msg.split(' ')
    val = msg[1]
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in response:
        return None
    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_r = response[response.find('Date=') + 6:response.find('"', response.find('Date=') + 6)].split('.')
    day, month, year = map(int, day_r)

    print(f'Курс {val} на дату {datetime(day=day, month=month, year=year)} равен {rub}')
    update.message.reply_text(f'Курс {val} на дату {datetime(day=day, month=month, year=year)} равен {rub}')


updater = Updater('5770096099:AAGWDSGlYrSwMfvUyOEpWU6Suct02VDP4uo')

updater.dispatcher.add_handler(CommandHandler('cur', cur_rate))
print('server start')
updater.start_polling()
updater.idle()

