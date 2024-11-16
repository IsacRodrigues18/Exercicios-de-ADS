# 3. Usando match-case, escreva um programa que peça ao usuário para digitar um caractere
# e diga se ele é uma vogal (a, e, i, o, u) ou não.

caractere = input("Digite apenas uma letra: ")
vogais = ["a", "e", "i", "o", "u"]
frase = "a letra que você digitou é uma vogal"

match caractere:
    case caractere if "a" in caractere:
        print(frase)
    case caractere if "e" in caractere:
        print(frase)
    case caractere if "i" in caractere:
        print(frase)
    case caractere if "o" in caractere:
        print(frase)
    case caractere if "u" in caractere:
        print(frase)
    case _:
        print("a letra que você digitou não é uma vogal.")