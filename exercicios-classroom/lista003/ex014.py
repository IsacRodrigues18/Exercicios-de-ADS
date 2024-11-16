# 14. Crie um programa que imprima os primeiros 10
# números da sequência de Fibonacci usando
# um loop while.

# cada número é a soma dos dois números anteriores
# começa com zero e um
# a partir disso, os dois números gerados são resultantes da soma dos dois anteriores

sequencia = [0, 1]

while len(sequencia) < 10:
    # adicionando como último elemento da lista a soma entre os dois valores anteriores.
    sequencia.append(sequencia[-1] + sequencia[-2])

print(sequencia)