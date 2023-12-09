import asyncio
import logging
import time

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.formatting import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

import statelang
import translatefunk

from googletrans import Translator

import config
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
dp = Dispatcher(storage=MemoryStorage())

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.api_token, parse_mode='HTML')
# Диспетчер
dp = Dispatcher()


def Textre(message_text, from_lang, to_lang):
    """Прилетает сообщение и языкы на уровне api"""
    """Базовая функция обращения к api google, не забыть убрать в дургой фаил"""

    translator = Translator()
    result = translator.translate(message_text, src=from_lang, dest=to_lang)
    return result


# Хэндлер на команду /start
@dp.message(Command("start"))  # Команда для первичного запуска бота
async def cmd_start(message: types.Message):
    # кнопки которые появляются со стартом
    kb = [
        [
            types.KeyboardButton(text="сменить язык")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )

    # TODO преддположим что бот берет инормацию о языке приложения и пишет стартовое сообщение на нем
    await message.answer("""Привет! Я маленький бот переводчик!\n
                         У меня пока совсем крошечный функционал: 
                         Ты можешь переключить язык перевода нажав на большую кнопку внизу\n
                         Или переводи сразу! 
                         Просто пиши сообщения, язык перевода по умолчанию en->ru!
                         Помощь - \help""",
                         reply_markup=keyboard)


@dp.message(Command("help"))
async def help_menu(message: types.Message):
    """Информационное меню"""
    await message.answer('''МЕНЮ:\nТут кратко описаны функции, которых на данный момент и нет:\n
                         в идеале я научусь переводить с фотографий, при помощи библиотеки цифрового зрения\n
                         и по возможности перенаправлять сообщения от пользователей к вам (может в виде чата)''')


@dp.message()
# Базовая функция данного бота на текщий момент,
# возвращает сообщение и его перевод на выбранный язык
# TODO сделать эхо цитатой
async def echo(message: types.Message, froml, tol):
    if froml == '' and tol == '':
        # языки по умолчанию
        froml = 'English'
        tol = 'Russian'

    translate_message = translatefunk.tryslator(message.text, froml, tol)

    #translate_message = Textre({message.text}, froml, tol)
    await message.answer(f'''вы переводите: "{message.text}"\n
                         Перевод: {translate_message}''')


# Запуск процесса поллинга новых апдейтов
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.bot_token.get_secret_value())

    dp.include_router(common.router)
    dp.include_router(.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())