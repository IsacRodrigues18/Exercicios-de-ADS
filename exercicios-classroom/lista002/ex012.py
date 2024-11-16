# 12.Use um loop for para verificar se um número é primo.

numero = int(input("Digite um número: ")) # recebe número do usuário

while numero != 0:
    primo = True

    if numero <= 1:
        primo = False

    for n in range(2, numero): # começa do dois e termina um número antes do valor total
        if numero%n == 0:
            primo = False
            break

    if primo: # não precisa de operador de igualdade, o valor dentro da variável já é reconhecido
        print("É primo.")
    else:
        print("Não é primo.")

    numero = int(input("Digite um número: ")) # recebe número do usuário