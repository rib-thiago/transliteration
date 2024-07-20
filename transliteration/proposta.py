from transliterate import translit

# Textos de entrada para cada idioma
texts = {
    'ru': "Привет, мир!",
    'ka': "გამარჯობა, სამყარო!",
    'el': "Γειά σας κόσμος!",
    'hy': "Բարեւ, աշխարհ!",
    'uk': "Привіт, світ!",
    'mk': "Здраво, светот!",
    'sr': "Здраво, свете!",
    'mn': "Сайн байна уу, дэлхий!",
    'bg': "Здравейте, свят!"
}

# Transliteração para cada idioma
for lang, text in texts.items():
    transliteration = translit(text, lang)
    print(f"{lang}: {transliteration}")
