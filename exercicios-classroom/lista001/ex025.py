# 25.Verifique se o número fornecido pelo usuário é positivo, negativo ou zero.

numero = int(input('Digite um número: '))

match numero:
    case numero if numero > 0:
        print('O número digitado é positivo.')
    case numero if numero < 0:
        print('O número digitado é negativo.')
    case _:
        print('O número digitado é zero.')