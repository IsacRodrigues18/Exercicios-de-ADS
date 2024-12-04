import base64 # módulo para codificação e decodificação de strings

# Função para criptografar (codificar) uma mensagem
# 1. recebe um parâmetro
# 2. codifica em bytes (o módulo base64 precisa da string convertida em bytes para funcionar)
# 3. codifica a string em bytes para base64 (os valores em bytes são criptografados)
# 4. retorna a mensagem criptografada em base64, mas convertida em string usando o método decode()
def criptografar(mensagem):
    mensagem_bytes = mensagem.encode('utf-8')
    mensagem_base64 = base64.b64encode(mensagem_bytes)
    return mensagem_base64.decode('utf-8')

# Função para descriptografar (decodificar) uma mensagem
# 1. recebe um parâmetro
# 2. decodifica a mensagem no formato base64 para bytes
# 3. retorna a mensagem em bytes, mas convertendo ela em string
def descriptografar(mensagem_base64):
    mensagem_bytes = base64.b64decode(mensagem_base64)
    return mensagem_bytes.decode('utf-8')

# Exemplo
mensagem_original = input('Digite sua mensagem: ')
mensagem_criptografada = criptografar(mensagem_original)
print("Mensagem criptografada:", mensagem_criptografada)

mensagem_descriptografada = descriptografar(mensagem_criptografada)
print("Mensagem descriptografada:", mensagem_descriptografada)