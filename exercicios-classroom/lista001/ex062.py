# 62.Crie uma string e converta todos os caracteres para o valor ASCII.

nome = input('Digite seu nome: ')
ascii = []

for char in nome:
    ascii.append(ord(char))

print(nome)
print(f'Nome em ascii: {ascii}.')