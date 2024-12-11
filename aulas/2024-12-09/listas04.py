# crie um programa que irá ler 10 números
# mostre a média, mediana e moda

# método manual

# cria uma lista vazia e recebe os números
numeros = int(input('Digite um número: '))
lista_numeros = []

# adiciona os números na lista
while len(lista_numeros) < 10:
    lista_numeros.append(numeros)

    numeros = int(input('Digite um número: '))

# soma todos os valores e divide pelo tamanho da lista
media = sum(lista_numeros)/len(lista_numeros)

# ordena a lista e pega o valor do meio
def mediana(lista):
    lista.sort()
    # lista_tamanho = len(lista)
    # lista_metade = lista_tamanho//2
    # lista_metade_2 = lista_tamanho//2 - 1

    if len(lista) % 2 == 0:
        # return (lista[lista_metade] + lista[lista_metade_2])/2
        
        # método resumido
        return (lista[len(lista)//2] + lista[len(lista)//2 - 1])/2
    else:
        # return lista[lista_metade]

        # método resumido
        return lista[len(lista)//2]

def moda_multimodal(lista):
    # dicionário vazio que conta as frequencias de cada número
    frequencia_numeros = {}

    # converte a lista em um conjunto
    # elimina as duplicatas
    numeros_unicos = set(lista)

    # conta quantas vezes cada número aparece
    # para cada número único na lista
    # o valor é adicionado ao dicionário
    for numero in numeros_unicos:
        frequencia_numeros[numero] = lista.count(numero)

    # identifica o maior valor de frequência
    # o maior valor é a moda
    # frequencia_numeros.values() retorna os valores do dicionário
    # max() retorna o maior valor do dicionário
    # max(frequencia_numeros.values()) retorna o maior valor do dicionário
    maior_frequencia = max(frequencia_numeros.values())

    # lista para armazenar os valores que são modas
    modas = []

    # para cada número no dicionário
    # o valor é igual ao maior valor de frequência
    # o valor é adicionado na lista de modas
    for numero in frequencia_numeros:
        if frequencia_numeros[numero] == maior_frequencia:
            modas.append(numero)

    return modas


# mostra os resultados
print(f'A média dos números é {media}')
print(f'A mediana dos números é {mediana(lista_numeros)}')
print(f'A moda dos números é {moda_multimoda(lista_numeros)}')