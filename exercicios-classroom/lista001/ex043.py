# 43.Divida uma string em palavras e imprima cada palavra.

frase = '''
"É comum falarmos mais e fazermos menos; a intenção é apenas escrava da memória, violenta ao nascer, mas transitória." William Shakespeare
'''
palavras = frase.split()

for item in range(len(palavras)):
    print(palavras[item])