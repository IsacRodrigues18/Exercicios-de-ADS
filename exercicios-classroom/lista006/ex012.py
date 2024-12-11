# 12. Função com Estrutura Condicional Aninhada
# Enunciado:
# Crie uma função chamada categoria_numero que receba um número inteiro e retorne:
# • "Positivo e Par" se o número for positivo e par.
# • "Positivo e Ímpar" se o número for positivo e ímpar.
# • "Negativo e Par" se o número for negativo e par.
# • "Negativo e Ímpar" se o número for negativo e ímpar.
# • "Zero" caso o número seja zero.

def categoria_numero(numero):
    def par_impar(valor):
        if valor % 2 == 0:
            return 'Par'
        else:
            return 'Impar'
    
    match numero:
        case numero if numero == 0:
            return 'Zero'
        case numero if numero > 0:
            return f'Positivo e {par_impar(numero)}'
        case numero if numero < 0:
            return f'Negativo e {par_impar(numero)}'

numero = int(input('Digite um número: '))

print(f'O número {numero} é {categoria_numero(numero)}.')