# 5. Função com Estrutura de Repetição - while
# Enunciado:
# Crie uma função chamada soma_ate_zero que leia números enquanto o número inserido não for
# zero. A função deve retornar a soma de todos os números inseridos (inclusive o zero final).

def soma_ate_zero():
    soma = 0
    numero = int(input('Digite um número: '))
    while numero != 0:
        soma += numero
        numero = int(input('Digite um número: '))
    return soma

print(f'O resultado da soma de todos os números é {soma_ate_zero()}.')