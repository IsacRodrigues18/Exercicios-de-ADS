# 44.Verifique se uma string é vazia.

nome = input('Digite seu nome: ')
string_preenchida = bool(nome)

if string_preenchida:
    print(f'O seu nome é {nome}.')
else:
    print('Nome inválido. Tente novamente.')