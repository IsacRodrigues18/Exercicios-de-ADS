# 3. Função com Condicional
# Enunciado:
# Crie uma função chamada verifica_quadrado_perfeito que recebe um número e retorna
# informado se ele é, ou não é, um quadrado perfeito. Teste a função com um número de sua escolha.

import math

def verifica_quadrado_perfeito(numero):
    raiz = math.sqrt(numero)

    if raiz.is_integer():
        return "é um quadrado perfeito."
    else:
        return "não é um quadrado perfeito."

numero = int(input('Digite um valor qualquer: '))

print(f'A raiz de {numero} é {math.sqrt(numero)} e {verifica_quadrado_perfeito(numero)}')