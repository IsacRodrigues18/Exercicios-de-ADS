# 7. Função para Verificar Número Primo
# Questão: Crie uma função chamada verificar_primo que receba um número inteiro e retorne
# True se o número for primo e False caso contrário.
# Dica: Um número é primo se ele for maior que 1 e só for divisível por 1 e por ele mesmo.

def verificar_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
            break

    return True

numero = int(input('Digite um número: '))

if verificar_primo(numero):
    print(f'{numero} é primo.')
else:
    print(f'{numero} não é primo.')