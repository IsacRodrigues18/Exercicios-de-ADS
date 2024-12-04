# condições switch case

pais = "Brasil"
pais.lower()
pais_nome = ""

## versão com if
if pais == "brasil":
    pais_nome = "do Brasil"
elif pais == "itália":
    pais_nome = "da Itália"
elif pais == "japão":
    pais_nome = "do Japão"
else:
    pais_nome = "da Argentina"

print(f"Toque o hino {pais_nome}")