# usado para estruturas de repetição onde já está definido
# o parâmetro para parar a verificação

# numero = int(input("Digite um número: "))
# 
# while numero != 0:
#     print(f"Número digitado = {numero}")

# nome, idade, sexo.
# só para quando encontrar alguém de cinquenta anos

idade = 0
sexo = ""
nome = ""

while idade <= 50:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    nome = input("Digite seu nome: ")
    print()

print("Tem mais de 50 anos.")