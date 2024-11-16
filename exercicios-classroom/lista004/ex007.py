# 7. Escreva um programa de calculadora que permita ao usuário escolher uma operação (adição,
# subtração, multiplicação, divisão) e fornecer dois números. O programa deve realizar a
# operação escolhida e exibir o resultado. Use condicionais para a seleção da operação.

operação = input("""
..........................................
: Qual operação você deseja fazer?       :
:..................................:.....:
: Digite 1 para adição             :  +  :
: Digite 2 para subtração          :  -  :
: Digite 3 para multiplicação      :  *  :
: Digite 4 para divisão            :  /  :
:..................................:.....:

""")

operador_nome = ""
resultado = 0

match operação:
    case operação if "1" in operação:
        operador_nome = "adição"
        operador_valor = "+"
    case operação if "2" in operação:
        operador_nome = "subtração"
        operador_valor = "-"
    case operação if "3" in operação:
        operador_nome = "multiplicação"
        operador_valor = "*"
    case operação if "4" in operação:
        operador_nome = "divisão"
        operador_valor = "/"

print(f"Você selecionou {operador_nome}")

numero001 = int(input("Digite o primeiro número: "))
numero002 = int(input("Digite o segundo número: "))

match operador_nome:
    case operador_nome if "adição" in operador_nome:
        resultado = numero001 + numero002
    case operador_nome if "subtração" in operador_nome:
        resultado = numero001 - numero002
    case operador_nome if "multiplicação" in operador_nome:
        resultado = numero001 * numero002
    case operador_nome if "divisão" in operador_nome:
        resultado = numero001 / numero002


print(f"O resultado da {operador_nome} entre {numero001} e {numero002} é {resultado}.")