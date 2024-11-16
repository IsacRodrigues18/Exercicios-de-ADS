# estruturas de repetição

vezes = int(input("Digite quantas vezes você quer testar valores: "))
condicao = ""

for n in range(vezes):
    numero = int(input("Digite um número: "))
    if numero%2 == 0:
        condicao = "par"
    else:
        condicao = "ímpar"
    print(f"O número {numero} é {condicao}")