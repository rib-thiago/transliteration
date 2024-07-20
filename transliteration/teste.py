from transliterate import translit, get_available_language_codes

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

input(text)

# Transliteration to Armenian
print(translit(text, 'hy'))


# Transliteration to Georgian
print(translit(text, 'ka'))


# Transliteration to Greek
print(translit(text, 'el'))


# Transliteration to Russian
print(translit(text, 'ru'))


# Transliteration to Ukraine
print(translit(text, 'uk'))


# Transliteration to Serbian
print(translit(text, 'sr'))


# Transliteration to Macedonian
print(translit(text, 'mk'))


# Transliteration to 
print(translit(text, 'l1'))


# Transliteration to Mongolian
print(translit(text, 'mn'))


# Transliteration to Bulgarian
print(translit(text, 'bg'))
