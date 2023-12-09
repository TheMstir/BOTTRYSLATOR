from translate import Translator


def tryslator(text): # l_from, l_to, phrase
    """получает язык с которого и на который переводит, а так же фразу
    возвращает переведенную фразу"""
    translator = Translator(from_lang='English', to_lang="Russian")
    if text != '':
        try:
            translation = translator.translate(text)

            return translation

        except:
            return 'Не знаю таких слов('

