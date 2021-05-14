from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor

from main.models import Url

# Создание бота
bot = Bot(settings.TOKEN)
dp = Dispatcher(bot)


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def handle_start_command(message: types.Message):
    await message.answer(
        text='Здравствуйте! Я URL-бот. Помогу Вам сократить ссылку. Нажмите на кнопку "Shorten the link".',
        reply_markup=types.ReplyKeyboardMarkup([[types.KeyboardButton('Shorten the link')]], True, True)
    )


# Обработка кнопки Shorten the link
@dp.message_handler(text=['Shorten the link'])
async def handle_shorten_the_lint(message: types.Message):
    await message.answer(
        text='Введите ссылку, которую нужно сократить и имя новой ссылки через пробел.\n'
             'Если хотите, чтоб имя новой ссылки было сгенерировано автоматически, то введите "@"'
    )


# Обработка ссылок
@dp.message_handler()
async def handle_text(message: types.Message):
    if len(message.text.split()) != 2 or not message.entities:
        return
    entity = message.entities[0]
    if entity.type != 'url':
        return
    url = Url(
        old=message.text[entity.offset:entity.offset + entity.length],
        new=message.text.split()[1] if message.text.split()[1] != '@' else ''
    )
    await sync_to_async(url.save)()
    await message.answer(f'Вот Ваша новая ссылка! https://prourl.herokuapp.com/{url.new}')
    '''if entities := message.entities:
            entity = entities[0]
            if entity.type == 'url':
                url = Url(
                    old=message.text[entity.offset:entity.offset+entity.length],
                    new=message.text.split()[1] if message.text.split()[1] != '@' else ''
                )
                await sync_to_async(url.save)()
                await message.answer(f'Вот Ваша новая ссылка! https://prourl.herokuapp.com/{url.new}')'''


# класс, который создал команду бот
class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True)