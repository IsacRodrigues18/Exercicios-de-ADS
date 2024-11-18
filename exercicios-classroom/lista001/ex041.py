# 41.Crie uma string e remova todas as vogais.

frase = '''
"Tem mais do que mostras,fala menos do que sabes."
William Shakespeare
'''
nova_frase = ''

vogais = ['a', 'e', 'i', 'o', 'u']

for char in frase:
    if char not in vogais:
        nova_frase += char

print(frase)
print(nova_frase)