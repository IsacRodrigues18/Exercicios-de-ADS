# f) Desenvolva uma função que verifique se um número é primo.

def verificar_primo(n):
    """
    Verifica se um número é primo.

    Parâmetros:
        n (int): O número a ser verificado.

    Retorna:
        bool: True se o número for primo, False caso contrário.
    """
    # Números menores que 2 não são primos
    if n < 2:
        return False

    # Verifica se n é divisível por algum número de 2 até a raiz quadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Exemplo de uso
numero = int(input("Escreva um número inteiro: "))
if verificar_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
