# 6. Faça um programa que peça ao usuário para digitar números
# até que ele digite 0, então imprima a soma de todos os
# números digitados usando um loop while.

numero = 1
soma = 0

while numero != 0:
    numero = int(input("Digite um número: "))
    soma = numero + soma

print(f"A soma dos números é {soma}")
print("O último número digitado foi zero. Fim do programa.")