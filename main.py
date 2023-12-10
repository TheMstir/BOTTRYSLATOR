import asyncio
import logging

from aiogram.fsm.storage.memory import MemoryStorage

from handlers import statelang, echosquad

import config
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


bot = Bot(token=config.api_token, parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(statelang.router)
dp.include_router(echosquad.router)

kb = [
    [
        types.KeyboardButton(text="/change_languages")
    ],
]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder=""
)

# Хэндлер на команду /start
@dp.message(Command("start"))  # Команда для первичного запуска бота
async def cmd_start(message: types.Message):
    """Стартовый хедлер"""
    # TODO преддположим что бот берет инормацию о языке приложения и пишет стартовое сообщение на нем
    await message.answer("""Привет! Я маленький бот переводчик!\n
У меня пока совсем крошечный функционал: 
Ты можешь переключить язык перевода нажав на большую кнопку внизу /change_languages\n
    Или переводи сразу! 
Просто пиши сообщения, язык перевода по умолчанию en->ru!
    Помощь - /help""",
                         reply_markup=keyboard)


@dp.message(Command("help"))
async def help_menu(message: types.Message):
    """Информационное меню"""
    await message.answer('''МЕНЮ:\nТут кратко описаны функции, которых на данный момент и нет:
в идеале я научусь переводить с фотографий, при помощи библиотеки цифрового зрения
и по возможности перенаправлять сообщения от пользователей к вам (может в виде чата)''')


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())