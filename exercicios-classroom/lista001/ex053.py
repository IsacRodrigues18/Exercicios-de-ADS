# 53.Verifique se uma string contém caracteres especiais.

esporte = input('Digite seu esporte favorito: ')
char_especiais = False

for char in esporte:
    if not char.isalnum():
        char_especiais = True
        break

if char_especiais:
    print('A string contém caracteres especiais.')
else:
    print('A string não contém caracteres especiais.')
