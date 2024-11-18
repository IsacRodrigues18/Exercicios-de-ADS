# 55.Verifique se duas strings são anagramas.

palavra01 = 'amor'
palavra02 = 'roma'

anagrama = 0
for char in palavra01:
    if char in palavra02:
        anagrama += 1

if anagrama == len(palavra01):
    print('As duas palavras são uma anagrama da outra.')
else:
    print('As palavras não são um anagrama da outra.')