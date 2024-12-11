# 6. Função com Manipulação de Strings
# Enunciado:
# Crie uma função chamada inverter_string que receba uma string como argumento e retorne
# a string invertida. Teste a função com a palavra "Python".

def inverter_string(string):
    nova_string = string[::-1]
    return nova_string

string = input('Digite uma palavra: ')

print(f'A palavra {string} invertida é {inverter_string(string)}.')