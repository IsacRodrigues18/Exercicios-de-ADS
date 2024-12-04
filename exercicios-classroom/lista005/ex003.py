# 3. Função com Lógica Matemática
# Questão: Crie uma função chamada calculadora que receba três parâmetros: dois números e
# uma operação (um caractere: "+", "-", "*", "/"). A função deve realizar a operação matemática
# correspondente e retornar o resultado.
# Dica: Utilize condicionais para determinar qual operação será realizada com base no caractere.

def calculadora(operacao, n1, n2):
    match operacao:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            if n2 == 0:
                return "Divisão inválida."
            else:
                return n1 / n2
        case _:
            return "Operador inválido."

def verificar_operador(operador):
    lista = ['+', '-', '*', '/']

    if operador not in lista:
        return "Operador inválido!"
    else:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        return calculadora(operador, n1, n2)

def menu():
    operador = input('''
    - Digite "+" para somar;
    - Digite "-" para subtrair;
    - Digite "*" para multiplicar;
    - Digite "/" para dividir.
    ''')

    return verificar_operador(operador)

print(menu())