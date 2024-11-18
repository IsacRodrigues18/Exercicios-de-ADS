# 61.Verifique se uma string começa com uma letra maiúscula.

nome = input('Digite seu nome: ')

if nome[0] == nome[0].upper():
    print('Nome digitado com a primeira letra maiúscula.')
else:
    print('Nome digitado com a primeira letra minuscula.')