from cyrtranslit import to_latin, to_cyrillic


# Transliteration to Russian
print(f'Russian: Моё судно на воздушной подушке полно угрей')
print(to_latin(u'Моё судно на воздушной подушке полно угрей', 'ru'))
input()

# Transliteration to Ukraine
print(f'Ukranian: Під лежачий камінь вода не тече')
print(to_latin(u'Під лежачий камінь вода не тече', 'ua'))
input()

# Transliteration to Serbian
print(f'Serbian: Мој ховеркрафт је пун јегуља')
print(to_latin(u'Мој ховеркрафт је пун јегуља'))
input()

# Transliteration to Macedonian
print(f'Macedonian: Моето летачко возило е полно со јагули')
print(to_latin(u'Моето летачко возило е полно со јагули', 'mk'))
input()

# Transliteration to Bulgarian
print(f'Bulgarian: Съединението прави силата!')
print(to_latin(u'Съединението прави силата!', 'bg'))
input()

# Transliteration to Mongol
print(f'Mongol: Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө')
print(to_latin(u'Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө', 'mn'))
input()

# Transliteration to Montenegrin
print(f'Montenegrin: Република')
print(to_latin(u'Република', 'me'))
input()


# Transliteration to Tajik
print(f'Tajik: Ман мактуб навишта истодам')
print(to_latin(u'Ман мактуб навишта истодам', 'tj'))
input()

