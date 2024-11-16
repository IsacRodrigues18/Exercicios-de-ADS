# 7. Escreva um programa que leia a senha do usuário
# até que ele digite a senha correta usando um loop while.

senha = ""
senha_correta = "senha123"

while senha != senha_correta:
    senha = input("Digite sua senha: ")

print("Senha correta. Fim do programa.")