# 57.Verifique se uma string é um número hexadecimal.

valor = input('Digite um valor hexadecimal (sem #): ')
hex = True

valores_validos = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(valor) == 6 or len(valor) == 3:
    for char in valor:
        if char not in valores_validos:
            hex = False
            break
else:
    hex = False

if hex:
    print('A string contém um valor hexadecimal válido')
else:
    print('VALOR INVÁLIDO.')