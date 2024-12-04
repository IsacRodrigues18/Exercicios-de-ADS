# 1 - informa se é primo
# 2 - calcula o fatorial
# 3 - calcula o quadrado do número
# 4 - sair


# menu de seleção
def menu():
    opcao = int(input('''
    ┌───────────────────────────────────┐
    │ Opções:                           │
    ├───────────────────────────────────┤
    │ 1 - Informa se é primo;           │
    ├───────────────────────────────────┤
    │ 2 - Calcula o fatorial;           │
    ├───────────────────────────────────┤
    │ 3 - Calcula o quadrado do número; │
    ├───────────────────────────────────┤
    │ 4 - Sair.                         │
    └───────────────────────────────────┘

    '''))
    sair = False
    while not sair:
        match opcao:
            case 1:
                print('Você escolheu a opção 1.')
            case 2:
                print('Você escolheu a opção 2.')
            case 3:
                print('Você escolheu a opção 3.')
            case 4:
                print('Saindo do programa.')
                sair = True
            case _:
                print('Operação inválida.')

        if sair:
            break
        else:
            return opcao

def numero_primo():
    print("selecionado número primo.")
def fatorial():
    print("selecionado fatorial.")
def quadrado():
    print("selecionado quadrado.")

# opção selecionada
match menu():
    case 1:
        numero_primo()
    case 2:
        fatorial()
    case 3:
        quadrado()