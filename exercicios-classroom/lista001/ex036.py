# 36.Verifique se uma string é um palíndromo.

string_original = 'Morram após a sopa marrom'

string_comparativa = string_original.replace("ó", "o").lower()
string_inversa = string_original[::-1].replace("ó", "o").lower()

print(string_comparativa)
print(string_inversa)

if string_comparativa == string_inversa:
    print('A string é um palíndromo.')
else:
    print('A string não é um palíndromo.')