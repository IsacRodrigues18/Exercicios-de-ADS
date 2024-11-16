# 9. Faça um programa que calcule o fatorial de
# um número fornecido pelo usuário usando um
# loop while.

numero = int(input("Digite um número: "))
cont = numero-1

while cont >= 1:
    print(f"{numero} x {cont} = {numero*cont}")
    numero = numero*cont
    cont -= 1