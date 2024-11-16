# 8. Crie um programa que imprima a tabuada
# de um número fornecido pelo usuário usando um
# loop while.

numero = int(input("Digite um valor para saber a tuabuada: "))
cont = 0

while cont < 11:
    print(f"{cont} x {numero} = {cont*numero}")
    cont += 1