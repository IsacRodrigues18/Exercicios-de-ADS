# e) Crie uma função que retorne a lista de elementos únicos de uma lista.

lista = [1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 8, 10, 10]

def elementos_unicos(lista):
    # convertendo a lista para conjunto
    # isso remove as duplicatas
    conjunto = set(lista)

    lista_unicos = list(conjunto)

    return lista_unicos

print(f'A lista de elementos originais é: {lista}')
print(f'A lista de elementos únicos é: {elementos_unicos(lista)}')