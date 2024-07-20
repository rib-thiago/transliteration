from deep_translator import  MyMemoryTranslator


langs_dict = MyMemoryTranslator().get_supported_languages(as_dict=True)

for key, value in langs_dict.items():
    print(f'{key} : {value}')
