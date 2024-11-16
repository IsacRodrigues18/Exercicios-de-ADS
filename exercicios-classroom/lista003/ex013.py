# 13. Escreva um programa que verifique
# se um número é primo usando um loop while.

numero = int(input("Digite um número: "))
cont = numero-1
primo = True

while cont >= 2:
    if numero%cont == 0:
        primo = False
        break
    if numero == 1:
        primo = False
    if numero == 0:
        primo = False
    cont -= 1

if primo:
    resultado = "é primo"
else:
    resultado = "não é primo"

print(f"O número digitado {resultado}")