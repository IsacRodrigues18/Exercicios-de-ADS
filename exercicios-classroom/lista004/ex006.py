# 6. Escreva um programa que calcule o fatorial de N. O valor de N deve ser fornecido pelo
# usuário. Crie uma solução usando “for” e outra usando “while”.

numero = int(input("Digite um número para calcular o fatorial do mesmo: "))
valor_inicial = numero
cont = numero - 1

# solução com for
for i in range(1, numero):
    numero = numero * cont
    cont -= 1

print(f"O fatorial de {valor_inicial} é {numero}.")

# solução com while
# index = 1
# while index <= numero:
#     numero = numero * cont
#     cont -= 1
#     index += 1
# 
#     if cont == 0:
#         break
# 
# print(f"O fatorial de {valor_inicial} é {numero}.")