# 4. Função com Estrutura de Repetição - for
# Enunciado:
# Crie uma função chamada imprime_multiplicacao que receba um número n e imprima a
# tabuada de multiplicação desse número, de 1 a 10.

def imprime_multiplicacao(n):
    lista = []
    for i in range(1, 11):
        lista.append('{}x{} = {}'.format(n, i, n*i))
    
    for i in lista:
        print(i)

numero = int(input('Digite um número: '))

imprime_multiplicacao(numero)