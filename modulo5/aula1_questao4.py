import datetime # importa biblioteca

data_atual = datetime.datetime.now() # armazena a data atual

data_formatada = data_atual.strftime('%d/%m/%Y') # formata a data
hora_formatada = data_atual.strftime('%H:%M') # formata o horário

print(f"Data: {data_formatada}") # saída
print(f"Hora: {hora_formatada}") # saída

