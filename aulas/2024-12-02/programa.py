import random # importando biblioteca

# 1. pedir pro usuário digitar cara ou coroa
# 2. verificar se o valor é válido
# 3. gerar um valor aleatório para cara e coroa
# 4. verificar se o valor bate ou não com o do sistema.
valor_usuario = input('Digite CARA ou COROA: ').lower()
valor_gerado = random.randint(1, 2)
valor_system = 0

if valor_usuario == "cara":
    valor_system = 1
elif valor_usuario == "coroa":
    valor_system = 2
else:
    print('valor inválido')
