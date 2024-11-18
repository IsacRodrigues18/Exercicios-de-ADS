# 60.Crie uma string e remova todos os números.

string = 'abc 123'
sem_numeros = ""

for char in string:
    if not char.isnumeric():
        sem_numeros += char

print(string)
print(sem_numeros)