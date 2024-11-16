# 11. Crie um programa que inverta uma string
# fornecida pelo usuário usando um loop while.

string = input("Digite sua cor favorita: ")
cont = 0

while cont < len(string):
    cont += 1

print(f"A cor {string} tem {cont} letras.")