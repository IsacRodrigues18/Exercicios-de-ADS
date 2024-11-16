# 17. Crie um programa que peça ao usuário
# para digitar uma série de números e encontre o
# menor número digitado usando um loop while.

##### ainda terminando

numero = 1
menor_numero = 1

while numero < menor_numero:
    numero = int(input("Digite um número (0 para finalizar): "))
    menor_numero = numero
    if numero == 0:
        break

print(f"O menor número dentre os que foram digitados foi {numero}")