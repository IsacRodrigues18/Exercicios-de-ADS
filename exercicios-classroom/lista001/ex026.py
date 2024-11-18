# 26.Compare dois números fornecidos pelo usuário e imprima o maior.

numero01 = int(input('Digite um número: '))
numero02 = int(input('Digite outro número: '))

match numero01, numero02:
    case numero01, numero02 if numero01 > numero02:
        print(f'O maior número digitado é {numero01}')
    case numero01, numero02 if numero01 < numero02:
        print(f'O maior número digitado é {numero02}')
    case _:
        print('Os dois números digitados são iguais.') 
