from transliterate import translit

text = u'''
ἤ μιν ἑλὼν ῥδίφω ἐς Τάρταρον ἠερόεντα

τῆλε μάλ᾽, ἦχι βάϑιστον ὑπό χϑονός ἐστι βέρεϑρον,
ἔνϑα σιδήρειαί τε πύλαι καὶ χάλκεος οὐδός,

τόσσον ἔἤνερϑ᾽ ᾿Αίδεω ὅσον οὐρανός ἐστ᾽ ἀπὸ γαίης.
'''

# Transliteration to Greek
print(f'Greek: {text}')
print(translit(text, 'el', reversed=True))
input()