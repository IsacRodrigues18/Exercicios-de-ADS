# c) Faça uma função que conte a quantidade de palavras em uma frase.

frase = input('Digite uma frase: ')

def contar_palavras(frase):
    # o split() separa as palavras da frase
    # adicionando-as a uma lista
    palavras = frase.split() 

    # len() retorna o tamanho da lista
    return len(palavras)

print(f'A frase tem {contar_palavras(frase)} palavras.')