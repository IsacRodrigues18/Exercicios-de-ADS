# 9. Função de Lógica Matemática - Fatorial
# Enunciado:
# Crie uma função chamada fatorial que calcule o fatorial de um número informado. Lembre-se
# que o fatorial de n é o produto de todos os inteiros positivos de 1 até n (exemplo: 5! = 5 × 4 × 3 × 2
# × 1).

def fatorial(n):
    fator = n

    for numero in range(n-1, 1, -1):
        fator = fator * numero

    return fator

numero = int(input('Digite um número: '))

print(f'O fatorial de {numero} é {fatorial(numero)}.')