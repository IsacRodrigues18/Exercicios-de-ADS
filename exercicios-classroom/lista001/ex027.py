# 27.Verifique se um ano fornecido é bissexto.

ano = int(input('Digite seu ano de nascimento: '))

if ano%4 == 0 and ano%100 != 0 or ano%4 == 0 and ano%400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')