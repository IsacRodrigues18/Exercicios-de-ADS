# 48.Verifique se uma string contém apenas letras minúsculas.

nome = input('Digite seu nome: ')

if nome == nome.lower():
    print('Todas as letras estão em minúsculas.')
else:
    print('Há letras maiúsculas na palavra.')