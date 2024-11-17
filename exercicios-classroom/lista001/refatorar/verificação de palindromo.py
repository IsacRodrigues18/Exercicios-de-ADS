# Verifique se uma string é um palíndromo.
palindromo = "subi no onibus"
palindromo_sem_espacos = palindromo.replace(" ", "")

if palindromo_sem_espacos == ''.join(reversed(palindromo_sem_espacos)):
    print(f"""
a frase '{palindromo}' ao contrário fica '{palindromo_sem_espacos}', portanto é um palíndromo.
    """)