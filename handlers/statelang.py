from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keybords import make_row_keyboard
import languages
from translatefunk import get_language

router = Router()


class LangChose(StatesGroup):
    """Переменные переключения языков"""
    choosing_lang_from = State()
    choosing_lang_to = State()


@router.message(Command("change_languages"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите язык с которого будем переводить:",
        reply_markup=make_row_keyboard(languages.lang_from_list)
    )
    # Устанавливаем пользователю состояние "выбирает язык на который переключиться"
    await state.set_state(LangChose.choosing_lang_from)


@router.message(LangChose.choosing_lang_from, F.text.in_(languages.lang_from_list))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_from=message.text.lower())
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, язык с которого будем переводить:",
        reply_markup=make_row_keyboard(languages.lang_to_list)
    )
    await state.set_state(LangChose.choosing_lang_to)

@router.message(LangChose.choosing_lang_from)
async def food_chosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого языка\n\n"
             "А может и знаю, но пока не понимаю как переключиться:",
        reply_markup=make_row_keyboard(languages.lang_from_list)
    )


@router.message(LangChose.choosing_lang_to, F.text.in_(languages.lang_to_list))
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = message.chat.id
    await message.answer(
        text=f"Вы выбрали Перевод с {user_data['chosen_from']} на {message.text.lower()}",
        reply_markup=ReplyKeyboardRemove()
    )
    get_language(user_data['chosen_from'], message.text.lower(), user_id)

    await state.clear()


@router.message(LangChose.choosing_lang_to)
async def food_size_chosen_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого языка\n\n"
             "А может и знаю, но пока не понимаю как переключиться:",
        reply_markup=make_row_keyboard(languages.lang_to_list)
    )