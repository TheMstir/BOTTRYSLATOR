from aiogram import Router, types
from translatefunk import tryslator

router = Router()

@router.message()
# Базовая функция данного бота на текщий момент,
# возвращает сообщение и его перевод на выбранный язык
# TODO сделать эхо цитатой
async def echo(message: types.Message): # , froml, tol если их можно передать, но надо брать значения из состояний
#    if froml == '' and tol == '':
        # языки по умолчанию
#        froml = 'English'
#        tol = 'Russian'

    translate_message = tryslator(message.text) # , froml, tol

    #translate_message = Textre({message.text}, froml, tol)
    await message.answer(f'''вы переводите: "{message.text}"\n
         Перевод: {translate_message}''')

