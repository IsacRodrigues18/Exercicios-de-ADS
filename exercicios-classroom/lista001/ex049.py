# 49.Verifique se uma string contém apenas letras maiúsculas.

nome = input('Digite seu nome: ')

if nome == nome.upper():
    print('Todas as letras estão em maiúsculas.')
else:
    print('Há letras minúsculas na palavra digitada.')