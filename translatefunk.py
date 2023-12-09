from translate import Translator


def tryslator(): # l_from, l_to, phrase
    """получает язык с которого и на который переводит, а так же фразу
    возвращает переведенную фразу"""
    translator = Translator(from_lang='Russian', to_lang="German")
    translation = translator.translate('Hello')


print(tryslator())
