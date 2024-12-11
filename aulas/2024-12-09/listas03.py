# crie um programa que irá ler 10 números
# mostre a média, mediana e moda

# método mais simples
import statistics

# cria uma lista vazia e recebe os números
numeros = int(input('Digite um número: '))
lista_numeros = []

# adiciona os números na lista
while len(lista_numeros) < 10:
    lista_numeros.append(numeros)

    numeros = int(input('Digite um número: '))

print(f'A media dos números é {statistics.mean(lista_numeros)}')
print(f'A mediana dos números é {statistics.median(lista_numeros)}')
print(f'A moda dos números é {statistics.mode(lista_numeros)}')