# 11.Verifique se nome está vazio e imprima uma mensagem adequada.

nome = input('Digite seu nome: ')
nome_preenchido = bool(nome)

if nome_preenchido:
    print(f'seu nome é {nome}')
else:
    print('Nome vazio, por favor digite um nome válido.')
