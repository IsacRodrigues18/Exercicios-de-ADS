# 16. Escreva um programa que conte quantas
# vezes um caractere específico aparece em uma
# string usando um loop while.

frase = """
"Às vezes a simplicidade e o silêncio dizem mais que a eloquência planejada."
-- William Shakespeare
"""
letra = "a"
cont = 0
char = 0

while cont <= len(frase):
    if frase[cont-1] == letra:
        char += 1
    cont += 1

print(frase)
print(f"A letra '{letra}' aparece {char} vezes na frase acima.")