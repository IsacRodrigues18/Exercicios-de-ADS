# crie um programa que solicite ao usuário que digite vários números.
# o programa só deve parar quando o usuário digitar zero.
# mostre na tela, em uma única linhya, todos os números digitados de maneira ordenada.
# além disso, informe, também, o maior e o menor número.

valor = int(input('Digite um número: '))
lista_numeros = []

while valor != 0:
    lista_numeros.append(valor)
    valor = int(input('Digite um número: '))

lista_numeros.sort()

print(f'Os números digitados foram: {lista_numeros}')
print(f'O maior número é {max(lista_numeros)}')
print(f'O menor número é {min(lista_numeros)}')
print(f'A soma dos números é {sum(lista_numeros)}')