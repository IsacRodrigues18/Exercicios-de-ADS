import matematica
import limpartela

# limpar os dados da tela conforme o programa for executando
limpartela.limpatela()

# menus
sair = False
while not sair:
    operacao = int(input(f'''
┌────────────────────────────────────────────┐
│ Digite "1" para selecionar adição;         │
├────────────────────────────────────────────┤
│ Digite "2" para selecionar subtração;      │
├────────────────────────────────────────────┤
│ Digite "3" para selecionar multiplicação;  │
├────────────────────────────────────────────┤
│ Digite "4" para selecionar divisão;        │
├────────────────────────────────────────────┤
│ Digite "5" para sair.                      │
└────────────────────────────────────────────┘

    '''))
    limpartela.limpatela()

    # verificando a operação
    operador = ""
    sinal_operacao = ""
    def operador_aritmetico(operador):
        print(f'você selecionou {operador}.')

    match operacao:
        case 1:
            operador = "adição"
            sinal_operacao = "+"
            operador_aritmetico(operador)
        case 2:
            operador = "subtração"
            sinal_operacao = "-"
            operador_aritmetico(operador)
        case 3:
            operador = "multiplicação"
            sinal_operacao = "*"
            operador_aritmetico(operador)
        case 4:
            operador = "divisão"
            sinal_operacao = "/"
            operador_aritmetico(operador)
        case 5:
            sair = True
            break
        case _:
            print('operação inválida.')

    # operação
    numero01 = int(input('Digite o primeiro número: '))
    numero02 = int(input('Digite o segundo número: '))
    resultado = 0

    match operador:
        case "adição":
            resultado = matematica.adicao(numero01, numero02)
        case "subtração":
            resultado = matematica.subtracao(numero01, numero02)
        case "multiplicação":
            resultado = matematica.multiplicacao(numero01, numero02)
        case "divisão":
            resultado = matematica.divisao(numero01, numero02)

    print(f'O resultado da operação é: {numero01}{sinal_operacao}{numero02} = {resultado}.')

    input()
    limpartela.limpatela()