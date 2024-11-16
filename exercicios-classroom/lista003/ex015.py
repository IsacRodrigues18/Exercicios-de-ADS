# 15. Faça um programa que peça ao usuário para
# digitar números até que a soma desses números
# seja maior que 100 usando um loop while.

numero = 0
soma = 0

while soma <= 100:
    numero = int(input("Digite um número: "))
    soma = soma + numero

print(f"A soma dos números digitados é {soma}")
print("Portanto, o valor é maior que 100.")