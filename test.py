from translate import Translator

translator = Translator(to_lang="Russian")
translation = translator.translate('Hello!!! Welcome to my class')

print(translation)
