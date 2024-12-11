# 11. Função com Condicional - Classificação
# Enunciado:
# Crie uma função chamada classificar_riqueza que receba o salário de uma pessoa e
# classifique como segue (utilize valores arbitrados por você mesmo):
# • Baixa Renda
# • Média Renda
# • Alta Renda
# • Rico
# • Milionário
# • Bilionário
# • Trilionário

def classificar_riqueza(salario):
    match salario:
        case salario if salario < 1000:
            return 'Baixa Renda'
        case salario if salario > 2000:
            return 'Média Renda'
        case salario if salario > 5000:
            return 'Alta Renda'
        case salario if salario > 10000:
            return 'Rico'
        case salario if salario > 1000000:
            return 'Milionário'
        case salario if salario > 1000000000:
            return 'Bilionário'

valor = int(input('Digite o valor do seu salário: '))

print(f'Você é {classificar_riqueza(valor)}.')