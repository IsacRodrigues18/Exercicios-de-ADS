# 5. Escreva um programa que gere e exiba os primeiros N números da sequência de Fibonacci.
# O valor de N deve ser fornecido pelo usuário.

numero = int(input("Digite o tamanho da sequencia que você quer ver: "))

fibonacci = [0, 1]

for i in range(numero-2):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

print(fibonacci)