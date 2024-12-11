# 2. Função com Variáveis Locais
# Enunciado:
# Crie uma função chamada raiz_cubica que receba um valor numérico e retorne sua raiz cúbica.
# Em seguida, chame a função com um valor de lado de 5 e imprima o resultado.

def raiz_cubica(numero):
    return pow(numero, 1/3)

print(raiz_cubica(5))