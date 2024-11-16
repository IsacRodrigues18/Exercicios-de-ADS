# 11.Dada a lista numeros = [2, 4, 6, 8, 10], use um loop for para imprimir o quadrado de cada número.

lista = [2, 4, 6, 8, 10]

for numero in range(len(lista)):
    valor = 0
    valor = lista[numero]*lista[numero]
    print(valor)