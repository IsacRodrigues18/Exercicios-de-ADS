# pedir para o usuário digitar o nome, sexo e idade
# o sexo deve ser preenchido com M ou F
# imprimir na tela "Você é um/a (sexo) de XX anos" ou "voce não se indentifica com M ou F e tem XX anos"
# M, F ou O
# verificar se a idade é par ou impar
# dizer se o ano que você nasceu é bissexto ou não

# entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (M, F ou O): ")

# condições e declaração de variáveis
masculino = genero == "M" or genero == "m"
feminino = genero == "F" or genero == "f"
naoBinario = genero == "O" or genero == "o"
pronome = ""

valorPar = idade%2 == 0
parOuImpar = ""

valorBissexto = (2024-idade)%4 == 0
anoBissexto = ""

# verificação do gênero e atribuição dos pronomes.
if masculino:
    pronome = "um homem"
if feminino:
    pronome = "uma mulher"
if naoBinario:
    pronome = "uma pessoa não binária"

# verificar se a idade é par ou ímpar
if valorPar:
    parOuImpar = "par"
else:
    parOuImpar = "ímpar"

# verificação se o ano de nascimento da pessoa é bissexto.
if valorBissexto:
    anoBissexto = "nasceu"
else:
    anoBissexto = "não nasceu"

# saída
print(f"""
Olá, {nome}.
Você é {pronome} de {idade} anos.
Sua idade é um valor {parOuImpar}.
Você {anoBissexto} em um ano bissexto.
""")