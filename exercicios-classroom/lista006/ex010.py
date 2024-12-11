# 10. Função de Manipulação de Strings - Palíndromo
# Enunciado:
# Crie uma função chamada verifica_palindromo que recebe uma string como parâmetro e
# informa se a palavra é um palíndromo.

def verifica_palindromo(string):
    # remove os espaços e deixa tudo minúsculo
    nova_string = string.replace(" ", "").lower()

    # verificação
    if nova_string == nova_string[::-1]:
        return 'é um palíndromo.'
    else:
        return 'não é um palíndromo.'

string = input('Digite uma palavra: ')

print(f'A palavra {string} {verifica_palindromo(string)}')