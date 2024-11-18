# 68.Verifique se uma string é um URL válido.

# considerando que não irei usar nenhum método externo
# vou resolver isso apenas verificando se a url está escrita corretamente.
# a verificação vai ser para saber se a url do google
# foi digitada corretamente.

url = input('Digite o site: ')
site = ['google.com',
        'google.com.br',
        'www.google.com',
        'www.google.com.br',
        'https://google.com',
        'https://google.com.br']

if url in site:
    print('O site foi digitado corretamente.')
else:
    print('Site inválido.')