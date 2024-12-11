# e) Ordene uma lista de números de forma crescente e decrescente.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# diferente do .reversed(), o .sorted() retorna uma nova lista
# esse tipo de abordagem é melhor para um código sem reatribuições
lista_crescente = sorted(lista)
lista_decrescente = sorted(lista, reverse=True)

print(f'Lista crescente: {lista_crescente}')
print(f'Lista decrescente: {lista_decrescente}')