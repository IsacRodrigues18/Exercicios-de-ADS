# 37.Conte quantas vezes um caractere específico aparece em uma string.

frase = '''
"Quem cedo e bem aprende, tarde ou nunca esquece. Quem negligencia as manifestações de amizade, acaba por perder esse sentimento."
-- William Shakespeare
'''

cont = 0
for char in frase:
    if "a" in char:
        cont += 1

print(f'Na seguinte frase, a letra "a" aparece {cont} vezes.')
print(frase)
