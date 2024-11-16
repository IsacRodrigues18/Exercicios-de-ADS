# 1. Escreva um programa que peça ao usuário para digitar
# um número inteiro positivo N. Em seguida, exiba todos
# os números ímpares no intervalo [-N, N] (intervalo fechado).

numero = int(input("Digite um número: "))

# se digitar 5, retornar o -5 com números ímpares até o 5 que o usuário digitou

negativo = -abs(numero) # valor convertido em negativo
positivo = abs(numero) # valor convertido em positivo
lista = [] # lista para colocar o intervalo
cont = 0 # usado para fazer a contagem dos valores positivos

# atribuindo os valores positivos e negativos
while negativo < 0:
    lista.append(negativo)
    negativo += 1
while positivo >= cont:
    lista.append(cont)
    cont += 1

# filtrando os numeros ímpares
impares = []
for item in lista:
    if lista[item]%2 != 0:
        impares.append(lista[item])

impares.sort() # ordenando os valores
print(impares)