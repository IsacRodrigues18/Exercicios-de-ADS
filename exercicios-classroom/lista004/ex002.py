# 2. Escreva um programa que solicite diversos números ao usuário. Os números podem ser
# positivos e negativos, inteiros e reais. O programa deve parar quando a soma desses
# números for maior ou igual a 100. Antes de parar, o programa deve exibir o valor da
# multiplicação entre todos os números digitados.

soma = 0
while soma <= 100:
    numero = input("Digite um número: ")

    if "." in numero:
        numero = float(numero)
    else:
        numero = int(numero)

    soma = numero + soma
    print(soma)

print("A soma dos números ultrapassou 100. Programa finalizado.")