# 47.Verifique se todos os caracteres de uma string são alfanuméricos.

nome = input('Digite seu nome: ')

if nome.isalpha():
    print('O nome digitado é válido.')
else:
    print('Ocorreu um erro, tente novamente.')