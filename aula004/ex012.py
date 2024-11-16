# condições switch case

pais = "Brasil"
pais.lower()
pais_nome = ""

## versão com switch
# alternativa mais organizada para estruturas
# condicionais com testes limitados
match pais:
    case "brasil":
        pais_nome = "do Brasil"
    case "itália":
        pais_nome = "do Itália"
    case "japão":
        pais_nome = "do Japão"
    case _:
        pais_nome = "da Argentina"

print(f"Toque o hino {pais_nome}")