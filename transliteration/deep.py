from deep_translator import MyMemoryTranslator

def translate_pt_to_hy(text):
    source_lang = 'pt-BR'  # Português
    target_lang = 'hy-AM'  # Armênio
    translated_text = MyMemoryTranslator(source=source_lang, target=target_lang).translate(text)
    return translated_text

def translate_hy_to_pt(text):
    source_lang = 'hy-AM'  # Armênio
    target_lang = 'pt-BR'  # Português
    translated_text = MyMemoryTranslator(source=source_lang, target=target_lang).translate(text)
    return translated_text

# Teste de tradução do português para o armênio
text_pt = "Olá, como você está ?"
translated_text_hy = translate_pt_to_hy(text_pt)
print("Português para Armênio:", translated_text_hy)

# Teste de tradução do armênio para o português
text_hy = "Բարև, ինչպես ես?"
translated_text_pt = translate_hy_to_pt(text_hy)
print("Armênio para Português:", translated_text_pt)
