# 6. Soma de Elementos de uma Lista
# Questão: Crie uma função chamada soma_lista que receba uma lista de números como
# parâmetro e retorne a soma de todos os elementos dessa lista.
# Dica: Você pode utilizar a função sum() ou criar um laço for para somar os elementos
# manualmente.

def soma_lista(numeros):
    for n in numeros:
        return sum(numeros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(soma_lista(numeros))