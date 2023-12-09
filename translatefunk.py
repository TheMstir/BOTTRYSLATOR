from translate import Translator


def tryslator(g): # l_from, l_to, phrase
    """получает язык с которого и на который переводит, а так же фразу
    возвращает переведенную фразу"""
    translator = Translator(from_lang='English', to_lang="Russian")
    translation = translator.translate(g)

    return translation

