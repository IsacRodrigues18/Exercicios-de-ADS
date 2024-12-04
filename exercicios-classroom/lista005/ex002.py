# 2. Função com Condicional
# Questão: Crie uma função chamada par_ou_impar que receba um número inteiro como
# parâmetro e retorne "Par" se o número for par e "Ímpar" se o número for ímpar.
# Dica: Use a operação módulo (%) para verificar se o número é divisível por 2.

def par_ou_impar(numero_inteiro):
    if numero_inteiro % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
print(par_ou_impar(0))