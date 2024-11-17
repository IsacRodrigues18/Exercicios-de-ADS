# Declare uma variável nome e atribua seu nome a ela
nome = "João Augusto"

# Declare uma variável idade e atribua sua idade a ela
idade = 21

# Imprima nome e idade usando a função print.
print(f"""
nome: {nome}
idade: {idade}
""")

# Solicite o nome do usuário com input e armazene na variável nome.
nome = input("Digite seu nome: ")

# Solicite a idade do usuário com input e armazene na variável idade.
idade = input("Digite sua idade: ")

# Converta a idade de string para inteiro.
idade = int(idade)
print(f"""
tipo primitivo da variável idade: {type(idade)}
""")

# Declare uma variável altura e atribua sua altura a ela.
altura = 1.70

# Converta altura para string e imprima.
altura = str(altura)
print(f"""
valor da variável altura: {altura}
tipo primitivo da variável altura: {type(altura)}
""")

# Converta altura para inteiro e imprima.
altura = float(altura)
altura = int(altura)
print(f"""
valor da variável altura: {altura}
tipo primitivo da variável altura: {type(altura)}
""")

# Crie uma variável booleana chamada estudante e atribua True ou False a ela.
estudante = True

# Verifique se nome está vazio e imprima uma mensagem adequada.
if nome == "":
    print("""
    O nome está vazio.
    """)

# Verifique se idade é maior que 18 e imprima uma mensagem adequada.
if idade >= 18:
    print("""
    Maior de idade
    """)

# Concatene nome e idade em uma mensagem.
print("nome:", nome, "idade:", idade)

# Acesse o primeiro caractere de nome.
print(f"""
primeiro caractere do nome: {nome[0]}
""")

# Acesse o último caractere de nome.
print(f"""
último caractere do nome: {nome[-1]}
""")

# Conte o número de caracteres em nome.
print(f"""
{nome} tem {len(nome)} caracteres.
""")

# Verifique se nome contém a letra "a".
if nome.find("a") or nome.find("ã") != -1:
    print("""
    o seu nome contém a letra 'a'
    """)
else:
    print("""
    o seu nome não contém nenhuma letra 'a'
    """)

# Divida nome em duas partes e imprima cada parte.
print(f"""
nome dividido: {nome.split()}
""")

# Converta nome para maiúsculas.
# Converta nome para minúsculas.
print(f"""
nome em caixa alta: {nome.upper()}
nome em letras minúscular: {nome.lower()}
""")

# Inverta a string nome.
print(f"""
seu nome invertido fica {''.join(reversed(nome))}
""")

# Solicite ao usuário dois números e some-os.
# Solicite ao usuário dois números e multiplique-os.
numero001 = int(input("Digite um número qualquer: "))
numero002 = int(input("Digite outro número qualquer: "))

print(f"""
a soma dos dois números que você digitou é {numero001 + numero002}
multiplicando os dois números o resultado é {numero001 * numero002}
""")

# Verifique se o número fornecido pelo usuário é par ou ímpar.
numero003 = int(input("Digite mais um número: "))
par_impar = ""

if numero003%2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"


# Verifique se o número fornecido pelo usuário é positivo, negativo ou zero.
positivo_negativo = ""

if numero003 > 0:
    positivo_negativo = "positivo"
elif numero003 < 0:
    positivo_negativo = "negativo"
else:
    positivo_negativo = "zero"

print(f"""
o número que você digitou é {par_impar}
o número que você digitou é {positivo_negativo}
""")

# Compare dois números fornecidos pelo usuário e imprima o maior.
maior_numero = ""
primeiro_maior = numero001 > numero002 and numero001 > numero003
segundo_maior = numero002 > numero001 and numero002 > numero003

if primeiro_maior:
    maior_numero = numero001
elif segundo_maior:
    maior_numero = numero002
else:
    maior_numero = numero003

print(f"""
dos números que você digitou {maior_numero} é o maior
""")

# Verifique se um ano fornecido é bissexto.
data_nascimento = int(input("Digite sua data de nascimento: "))
bissexto = ""

if data_nascimento%4 == 0:
    bissexto = "nasceu"
else:
    bissexto = "não nasceu"

print(f"""
você {bissexto} em um ano bissexto.
""")

# Acesse o terceiro caractere de uma string.
comida_favorita = input("Digite qual sua comida favorita: ")
print(f"""
o terceiro caractere da palavra {comida_favorita} é {comida_favorita[2]}
""")

# Crie uma string e imprima seus caracteres um a um.
for i in range(0, len(comida_favorita)):
    print(comida_favorita[i], end=" ")
print()

# Acesse o segundo caractere de uma string.
print(f"""
o segundo caractere de {comida_favorita} é {comida_favorita[1]}
""")

# Verifique se uma string começa com uma determinada letra.
if comida_favorita[0] == "a":
    print("""
    sua comida favorita começa com a letra 'a'
""")

# Verifique se uma string termina com uma determinada letra.
if comida_favorita[-1] == "a":
    print("""
sua comida favorita termina com a letra 'a'
    """)

# Crie uma string e substitua um caractere por outro.
substituicao_comida_favorita = comida_favorita.replace("a", "4")

print(f"""
todas as letras 'a' da palavra {comida_favorita} foram substituídas por '4', resultando em {substituicao_comida_favorita}.
""")

# Concatene duas strings.
print("concatenação das duas palavras:", comida_favorita, "e", substituicao_comida_favorita)

# Crie uma string e remova espaços em branco no início e no fim.
espacos_em_branco = "                 string de exemplo                     "
print(f"""
string com espaços: {espacos_em_branco}
string sem espaços: {espacos_em_branco.replace(" ", "")}
""")

