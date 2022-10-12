import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import logging


def button_click(update: Update, context: CallbackContext):
    button_A = telegram.InlineKeyboardButton('Рациональные числа', callback_data='button_A')
    button_B = telegram.InlineKeyboardButton('Комплексные числа', callback_data='button_B')
    replay_markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[button_A], [button_B]])
    update.message.reply_text('Добрый день! Чтобы начать работу с калькулятором выберите вид чисел',
                              reply_markup=replay_markup)

    return callback

def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'button_A':
        query.answer()
        query.message.reply_text(text='Список действий:')
        query.message.reply_text(text='/add <первое число> <второе число>')
        query.message.reply_text(text='/sub <первое число> <второе число>')
        query.message.reply_text(text='/mult <первое число> <второе число>')
        query.message.reply_text(text='/div <первое число> <второе число>')
    if variant == 'button_B':
        query.answer()
        query.message.reply_text(text='Список действий:')
        query.message.reply_text(text='/add_com <первое число> <второе число>')
        query.message.reply_text(text='/sub_com <первое число> <второе число>')
        query.message.reply_text(text='/mult_com <первое число> <второе число>')
        query.message.reply_text(text='/div_com <первое число> <второе число>')


def add_command(update: Update, context: CallbackContext) -> None:
    a = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f'{int(context.args[0])} + {int(context.args[1])} = {a}')

def sub_command(update: Update, context: CallbackContext) -> None:
    a = int(context.args[0]) - int(context.args[1])
    update.message.reply_text(f'{int(context.args[0])} - {int(context.args[1])} = {a}')

def mult_command(update: Update, context: CallbackContext) -> None:
    a = int(context.args[0]) * int(context.args[1])
    update.message.reply_text(f'{int(context.args[0])} * {int(context.args[1])} = {a}')

def div_command(update: Update, context: CallbackContext) -> None:
    a = int(context.args[0]) / int(context.args[1])
    update.message.reply_text(f'{int(context.args[0])} / {int(context.args[1])} = {a}')

def add_command_compl(update: Update, context: CallbackContext) -> None:
    a = complex(context.args[0]) + complex(context.args[1])
    update.message.reply_text(f'{complex(context.args[0])} + {complex(context.args[1])} = {complex(a)}')

def sub_command_compl(update: Update, context: CallbackContext) -> None:
    a = complex(context.args[0]) - complex(context.args[1])
    update.message.reply_text(f'{complex(context.args[0])} - {complex(context.args[1])} = {complex(a)}')

def mult_command_compl(update: Update, context: CallbackContext) -> None:
    a = complex(context.args[0]) * complex(context.args[1])
    update.message.reply_text(f'{complex(context.args[0])} * {complex(context.args[1])} = {complex(a)}')

def div_command_compl(update: Update, context: CallbackContext) -> None:
    a = complex(context.args[0]) / complex(context.args[1])
    update.message.reply_text(f'{complex(context.args[0])} / {complex(context.args[1])} = {complex(a)}')

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
updater = Updater('5770096099:AAGWDSGlYrSwMfvUyOEpWU6Suct02VDP4uo')
dispatch = updater.dispatcher
button_click_handler = CommandHandler('button', button_click)
callback_handler = CallbackQueryHandler(callback=callback, pattern=None, run_async=False)
add_handler = CommandHandler('add', add_command)
sub_handler = CommandHandler('sub', sub_command)
mult_handler = CommandHandler('mult', mult_command)
div_handler = CommandHandler('div', div_command)
add_compl_handler = CommandHandler('add_com', add_command_compl)
sub_compl_handler = CommandHandler('sub_com', sub_command_compl)
mult_compl_handler = CommandHandler('mult_com', mult_command_compl)
div_compl_handler = CommandHandler('div_com', div_command_compl)
dispatch.add_handler(button_click_handler)
dispatch.add_handler(callback_handler)
dispatch.add_handler(add_handler)
dispatch.add_handler(sub_handler)
dispatch.add_handler(mult_handler)
dispatch.add_handler(div_handler)
dispatch.add_handler(add_compl_handler)
dispatch.add_handler(sub_compl_handler)
dispatch.add_handler(mult_compl_handler)
dispatch.add_handler(div_compl_handler)
updater.start_polling()
updater.idle()



