# 67.Crie uma string e conte o número de consoantes.

nome = input('Digite seu nome: ')
vogais = ['a', 'á', 'ã', 'e', 'é', 'i', 'o', 'u']
cont = 0

for char in nome:
    if char not in vogais:
        cont += 1

print(nome)
print(f'Seu nome tem {cont} consoante(s).')