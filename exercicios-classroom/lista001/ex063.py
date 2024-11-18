# 63.Verifique se todos os caracteres de uma string são dígitos.

idade = input('Digite sua idade: ')

if idade.isnumeric():
    print('Há apenas valores numéricos na string.')
else:
    print('Valor inválido. Tente novamente.')
