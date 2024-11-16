# 7. Calcule o fatorial de um número dado pelo usuário usando um loop for.

numero = int(input("Digite um número: ")) # recebe número do usuário
valor = numero
contador = numero

for n in range(numero):
    valor = valor*contador
    print(valor)