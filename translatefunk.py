from translate import Translator

#язык с которого
f_l = ''
#язык на который
s_l = ''


def get_language(first, second, user_id):
    """тут мы попобуем перехватывать язык"""

    with open('user_base.txt', 'r+') as file:
        data = file.read()
        search_term = f"{user_id}"
        if search_term in data:
            finder = data.split('\n')
            click = 0
            for el in finder:
                user = el.split(' ')
                print(finder[click])
                if user[0] == f'{user_id}':
                    finder[click] = (f'{user_id} {first},{second}\n')
                    print(f'тут произошла замена {finder}')
                    new = ''.join(finder)
                    with open('user_base.txt', 'w') as file:
                        file.write(new)
                    break
        else:
            file.write(f'{user_id} {first},{second}\n')



    print(f'Первая{first}\nВторой{second}, User ID {user_id}')
    # Хорошо - идея для реализации. Открывает блокнот делает там запись, а функция перевода к тому же блокноту обращается
    # Ищет строчку и по ней все возвращает!


def tryslator(text, user_id): # еще пользователя передаем чтобы найти его в txt файле
    """получает язык с которого и на который переводит, а так же фразу
    возвращает переведенную фразу"""

    with open('user_base.txt', 'r') as file:
        data = file.read()
        search_term = f"{user_id}"
        if search_term in data:
            folder = data.split('\n')
            for el in folder:
                now = el.split(' ')
                if now[0] == f'{user_id}':
                    langus = now[1].split(',')
                    from_lang = langus[0]
                    to_lang = langus[1]
                    print(f'{langus[0]} a vtoroy {langus[1]}')
        else:
            from_lang = 'English'
            to_lang = 'Russian'

    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    if text != '':
        try:
            translation = translator.translate(text)
            return translation

        except:
            return 'Не знаю таких слов('

