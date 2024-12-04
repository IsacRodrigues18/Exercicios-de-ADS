# 10. Média de uma Lista
# Questão: Crie uma função chamada media_lista que receba uma lista de números como
# parâmetro e retorne a média aritmética dos números.
# Dica: A média é a soma dos elementos dividida pelo número de elementos. Utilize a função sum()
# e a função len() para isso.

def media_lista(numeros):
    return sum(numeros) / len(numeros)

numeros = [1, 2, 3, 4, 5]

print(media_lista(numeros))