from polyglot.transliteration import Transliterator

# Inicialize o transliterador com grego como idioma de origem e russo como idioma de destino
transliterator = Transliterator(source_lang="el", target_lang="en")

# Texto em grego que você deseja transliterar
texto_grego = u"Γειάσας"

# Transliterar o texto grego para russo
transliteracao_ingles = transliterator.transliterate(texto_grego)

print(transliteracao_ingles)