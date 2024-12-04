# 2. Escreva um programa em Python que leia um número inteiro positivo e mostre na tela,
# EM UMA ÚNICA LINHA, todos os números primos de 1 até esse número, inclusive.
# (20 PONTOS)
# EXEMPLO:
# - ENTRADA = 10
# - SAÍDA = 2 3 5 7

# lembrete: número primo: só é divisível por ele mesmo e por um
# o resto da divisão só pode dar zero para o próprio número e um
# cont | r | resto
# 7:7 = 1 - 0
# 7:6 = 0 - 1
# 7:5 = 0 - 1
# 7:4 = 0 - 1
# 7:3 = 0 - 1
# 7:2 = 0 - 1
# 7:1 = 1 - 0

numero = int(input('Digite um número: '))
contador = numero-1
numeros_primos = []
primo = True

for i in range(numero):
    for n in range(i-1, 1, -1):
        resto_divisao = i%contador

        if resto_divisao == 0:
            primo = False
            break
        contador -= 1

    if primo:
        numeros_primos.append(i)

print(numeros_primos)

# não finalizado