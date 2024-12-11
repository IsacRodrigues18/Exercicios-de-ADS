# 8. Função para Verificar Maioridade
# Enunciado:
# Crie uma função chamada verifica_maioridade que receba a idade de uma pessoa e retorne
# "Maior de idade" se a idade for 18 ou mais, e "Menor de idade" caso contrário.

def verifica_maioridade(idade):
    if idade >= 18:
        return 'Maior de idade'
    else:
        return 'Menor de idade'

idade = int(input('Digite sua idade: '))

print(f'Você é {verifica_maioridade(idade)}.')