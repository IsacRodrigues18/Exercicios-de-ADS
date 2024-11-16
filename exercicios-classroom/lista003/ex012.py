# 12. Faça um programa que conte de 1 a 100,
# mas pare o loop quando atingir um número
# divisível por 17 usando um loop while.

cont = 1

# se numero%17 = 0:
while cont <= 100:
    print(cont)
    if cont%17 == 0:
        break
    cont += 1