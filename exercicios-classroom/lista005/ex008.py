# 8. Importação e Uso de Biblioteca de Data e Hora
# Questão: Importe a biblioteca datetime e crie uma função chamada data_atual que exiba a
# data e a hora atual no formato "Dia/Mês/Ano Hora:Minuto:Segundo".
# Dica: Utilize datetime.datetime.now() para obter a data e hora atual.

import datetime

def data_atual():
    agora = datetime.datetime.now()

    data = ''.join(f'{agora.day}/{agora.month}/{agora.year}')
    hora = ''.join(f'{agora.hour}/{agora.minute}/{agora.second}')
    formatado = ''.join(f'{data} {hora}')

    return formatado

print(data_atual())