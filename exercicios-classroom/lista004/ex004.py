# 4. Crie um programa que solicita ao usuário para digitar uma palavra. O programa deve
# inverter a palavra digitada. Utilize “for”. Utilize “len(palavra)” para saber quantas letras a
# palavra tem.

palavra = input("Digite sua comida favorita: ")
palavra_inversa = ""

for char in range(len(palavra), 0, -1):
    palavra_inversa += palavra[char-1]

print(f"A palavra que você digitou tem {len(palavra)} letras.")
print(f"A palavra '{palavra}' ao contrário fica '{palavra_inversa}'.")