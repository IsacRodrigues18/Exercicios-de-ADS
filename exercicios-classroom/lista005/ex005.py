# 5. Função para Contagem Regressiva
# Questão: Crie uma função chamada contagem_regressiva que receba um número inteiro n
# como parâmetro e exiba uma contagem regressiva de n até 1, decrementando 1 a cada vez.
# Dica: Use um laço while ou for para realizar a contagem regressiva.

def contagem_regressiva(n):
    for numero in range(n):
        print(n - numero)

contagem_regressiva(10)