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


def start(update: Update, context: CallbackContext):
    reply_text = 'Здравствуйте! Я URL-бот. Помогу Вам сократить ссылку. Пропишите "Сократить ссылку".'
    # reply_keyboard = [['Cократить ссылку']]
    # markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        text=reply_text,
        # reply_markup=markup
    )


def long(update: Update, context: CallbackContext):
    reply_text = 'Введите ссылку, которую нужно сократить'
    update.message.reply_text(
        text=reply_text
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
        message_handler1 = MessageHandler(Filters.regex('^Сократить ссылку'), long)
        message_handler2 = MessageHandler(Filters.regex('^сократить ссылку'), long)
        updater.dispatcher.add_handler(message_handler)
        updater.dispatcher.add_handler(message_handler1)
        updater.dispatcher.add_handler(message_handler2)

        updater.start_polling()
        updater.idle()