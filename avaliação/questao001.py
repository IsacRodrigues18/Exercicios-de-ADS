# 1. Escreva um programa em Python que peça ao usuário para digitar dois números
# inteiros. O programa deve calcular o fatorial de cada um dos números e somá-los. Após
# encontrar o resultado, o programa deve verificar se o resultado é par ou ímpar,
# imprimindo na tela o número e a sua classificação. (40 PONTOS)
# EXEMPLO:
# - ENTRADA 1 = 2
# - ENTRADA 2 = 3
# - RESULTADO = 2! + 3! = 2 + 6 = 8
# - SAÍDA = 8 É PAR

# entrada de dados
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

# fatorial do primeiro número
cont = primeiro_numero - 1
fator = primeiro_numero

while cont >= 1:
    fator = fator * cont
    cont -= 1

# fatorial do segundo número
cont02 = segundo_numero - 1
fator02 = segundo_numero

while cont02 >= 1:
    fator02 = fator02 * cont02
    cont02 -= 1

# soma dos fatores
soma_fatores = fator + fator02

# verificação se é par ou ímpar
par_impar = ""
if soma_fatores%2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

# saída de dados
print(f'''
- o fatorial de {primeiro_numero} é {fator};
- o fatorial de {segundo_numero} é {fator02};
- {fator} + {fator02} = {soma_fatores};
- {soma_fatores} é {par_impar}.
''')