# idade = int(input("Digite sua idade: "))
# 
# maior_de_idade = idade >= 18
# if maior_de_idade:
#     print("Maior de idade")
# else:
#     print("Menor de idade")

# saber qual o maior número
numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))
numero03 = int(input("Digite o terceiro número: "))

primeiroMaior = numero01 > numero02 and numero01 > numero03
segundoMaior = numero02 > numero01 and numero02 > numero03

if primeiroMaior:
    print(f"o número {numero01} é o maior")
elif segundoMaior:
    print(f"o número {numero02} é o maior")
else:
    print(f"o número {numero03} é o maior")