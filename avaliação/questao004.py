# 4. Crie um programa em Python que leia um texto digitado pelo usuário e conte quantas
# vogais de cada tipo (A, E, I, O, U) estão presentes no texto. O programa deve
# considerar tanto maiúsculas quanto minúsculas. Imprima o resultado no formato:
# (20 PONTOS)
# - "Existem X letras A".
# - "Existem X letras E".
# - "Existem X letras I".
# - "Existem X letras O".
# - "Existem X letras U".

texto = input('Digite seu texto: ')
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for char in texto:
    if 'a' in char.lower():
        cont_a += 1

for char in texto:
    if 'e' in char.lower():
        cont_e += 1

for char in texto:
    if 'i' in char.lower():
        cont_i += 1

for char in texto:
    if 'o' in char.lower():
        cont_o += 1

for char in texto:
    if 'u' in char.lower():
        cont_u += 1


print(f'''
- "Existem {cont_a} letras A".
- "Existem {cont_e} letras E".
- "Existem {cont_i} letras I".
- "Existem {cont_o} letras O".
- "Existem {cont_u} letras U".
''')