# d) Implemente uma função que receba uma lista de números e retorne a média deles.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def media(lista):
    media = sum(lista) / len(lista)
    return media

print(f'Os números da lista são: {lista}')
print(f'A média da lista é: {media(lista)}')