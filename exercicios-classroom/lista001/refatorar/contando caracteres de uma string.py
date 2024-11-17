# 37.Conte quantas vezes um caractere específico aparece em uma string.
frase = """
"É mais fácil obter o que se deseja com um sorriso do que à ponta da espada."
-- William Shakespeare
"""

contador = 0
for letra in frase:
    if letra.lower() == 'a':
        contador += 1

print(f"""
{frase}

nessa frase, a letra 'a' aparece {contador} vezes.
""")