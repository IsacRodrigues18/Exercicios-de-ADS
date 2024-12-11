# b) Escreva uma função que verifique se um número está presente em uma lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input('Digite um número: '))

def verificar_numero(lista, numero):
    if numero in lista:
        return True
    else:
        return False

if verificar_numero(lista, numero):
    print(f'O número {numero} está na lista.')
else:
    print(f'O número {numero} não está na lista.')