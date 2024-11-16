# 4. Escreva um programa que encontre o
# maior número em uma lista usando um loop while.

lista = [1, 2, 4, 5, 6, 123, 5544, 0]
maior = lista[0]
i = 0

while i < len(lista):
    if maior < lista[i]:
        maior = lista[i]
    i += 1

print(maior)