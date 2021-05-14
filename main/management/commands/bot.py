from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram import Update
from telegram.utils.request import Request
from django.conf import settings
from telegram.ext import Updater
from telegram.ext.filters import Filters
from telegram.ext.conversationhandler import CallbackContext
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from main.models import Url


def start(update: Update, context: CallbackContext):
    reply_text = 'Здравствуйте! Я URL-бот. Помогу Вам сократить ссылку. Нажмите на кнопку "Shorten the link".'
    reply_keyboard = [['Shorten the link']]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        text=reply_text,
        reply_markup=markup
    )


def long(update: Update, context: CallbackContext):
    reply_text = 'Введите ссылку, которую нужно сократить и имя новой ссылки через пробел.' \
                 'Если хотите, чтоб имя новой ссылки было сгенерировано автоматически, то введите "@"'
    update.message.reply_text(
        text=reply_text,
    )
    return link(update, context)


def tex(update: Update, context: CallbackContext):
    text = update.message.text
    t1, t2 = map(str, text.split())
    return t1, t2


def link(update: Update, context: CallbackContext):
    t1, t2 = tex(update, context)
    if t2 == '@':
        t2 = ''
    form = Url(
        old=t1,
        new=t2
    )

    form.save()
    update.message.reply_text(
        text='Вот Ваша новая ссылка! http://127.0.0.1:8000/' + form.new,
    )


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            # base_url=settings.PROXY_URL
            )
        print(bot.get_me())
        updater = Updater(
            bot=bot,
            use_context=True
        )

        message_handler = CommandHandler('start', start)
        message_handler1 = MessageHandler(Filters.regex('^Shorten the link$'), long)
        message_handler2 = MessageHandler(Filters.text, link)
        updater.dispatcher.add_handler(message_handler)
        updater.dispatcher.add_handler(message_handler1)
        updater.dispatcher.add_handler(message_handler2)
        updater.start_polling()
        updater.idle()