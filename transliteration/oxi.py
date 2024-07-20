from transliterate import translit, get_available_language_codes


# Transliteration to Russian
print(f'Russian: Привет, мир!')
print(translit(u'Привет, мир!', 'ru', reversed=True))
input()

# Transliteration to Ukraine
print(f'Ukranian: Привіт, світ!')
print(translit(u'Привіт, світ!', 'uk', reversed=True))
input()

# Transliteration to Serbian
print(f'Serbian: Здраво, свете!')
print(translit(u'Здраво, свете!', 'sr', reversed=True))
input()

# Transliteration to Macedonian
print(f'Macedonian: Здраво, светот!')
print(translit(u'Здраво, светот!', 'mk', reversed=True))
input()

# Transliteration to Bulgarian
print(f'Bulgarian: Съединението прави силата!')
print(translit(u'Съединението прави силата!', 'bg', reversed=True))
input()

# Transliteration to Mongol
print(f'Mongol: Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө')
print(translit(u'Амрагаа Сүнжидмаагаа гэсээр ирлээ дээ хө-хө-хө', 'mn', reversed=True))
input()

# Transliteration to Greek
print(f'Greek: Γειά σας κόσμος!')
print(translit(u'Γειά σας κόσμος!', 'el', reversed=True))
input()


# Transliteration to Armenian
print(f'Armenian: Բարեւ, աշխարհ!')
print(translit(u'Բարեւ, աշխարհ!', 'hy', reversed=True))
input()

# Transliteration to Georgian
print(f'Georgian: გამარჯობა, სამყარო!')
print(translit(u'გამარჯობა, სამყარო!', 'ka', reversed=True))
input()
