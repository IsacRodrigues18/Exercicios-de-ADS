# 7. Função de Contagem de Caracteres
# Enunciado:
# Crie uma função chamada contar_caracteres que receba uma string e retorne o número de
# vezes que a letra "a" aparece nela. Teste a função com a palavra "banana".

def contar_caracteres(string):
    cont = 0

    for char in string:
        if "a" in char:
            cont += 1
    
    return cont

string = input('Digite alguma coisa: ')

print(f'A letra "a" aparece {contar_caracteres(string)} vezes na palavra {string}.')