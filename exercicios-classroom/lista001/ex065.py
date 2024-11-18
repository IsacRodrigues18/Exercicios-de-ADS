# 65.Crie uma string e remova caracteres duplicados.

nome = "Peedroo"
cont = []
novo_nome = ""

for char in nome:
    if char not in cont:
        cont.append(char)
        novo_nome += char

print(nome)
print(novo_nome)