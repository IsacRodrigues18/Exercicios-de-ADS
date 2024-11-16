# 10. Escreva um programa que conte o número de
# vogais em uma string fornecida pelo usuário
# usando um loop while.

string = input("Digite sua comida favorita: ")
cont = 0

while cont < len(string):
    cont += 1

print(f"Sua comida favorita ({string}) tem {cont} caracteres.")