import sys
from polyglot.text import Text

def transliterate_greek_to_english(text):
    # Cria um objeto Text com o texto em grego
    text_obj = Text(text, hint_language_code='el')

    # Translitera o texto grego para inglês e junta as palavras em uma única string
    transliterated_text = ' '.join(text_obj.transliterate(target_language='en'))

    return transliterated_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o nome do arquivo como argumento.")
        sys.exit(1)

    # Obtém o nome do arquivo a partir dos argumentos da linha de comando
    filename = sys.argv[1]

    # Lê o texto do arquivo
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            greek_text = file.read()
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        sys.exit(1)

    # Translitera o texto grego para inglês
    english_transliteration = transliterate_greek_to_english(greek_text)
    print(english_transliteration)
