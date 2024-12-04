# 4. Importação de Biblioteca
# Questão: Importe a biblioteca math e utilize a função sqrt() para calcular a raiz quadrada de um
# número fornecido pelo usuário. Exiba o resultado.
# Dica: Lembre-se de usar import math no início do código e depois chamar a função
# math.sqrt().

import math

numero = int(input('Digite um número: '))

raiz = math.sqrt(numero)

print(f'A raiz quadrada de {numero} é {raiz}.')