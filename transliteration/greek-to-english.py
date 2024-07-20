from polyglot.text import Text

def transliterate_greek_to_english(text):
    # Cria um objeto Text com o texto em grego
    text_obj = Text(text, hint_language_code='el')

    # Translitera o texto grego para inglês e junta as palavras em uma única string
    transliterated_text = ' '.join(text_obj.transliterate(target_language='en'))

    return transliterated_text

# Texto em grego que você deseja transliterar
greek_text = "Γειά σας, κόσμε! Καλημέρα σας!"

# Translitera o texto grego para inglês e imprime
english_transliteration = transliterate_greek_to_english(greek_text)
print(english_transliteration)
