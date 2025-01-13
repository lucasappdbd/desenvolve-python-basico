# Entrada de dados
ano = int(input("Digite o ano: "))

# Processamento e saída
ano_divisivel_4 = (ano % 4)
ano_divisivel_100 = (ano % 100)
ano_divisivel_400 = (ano % 400)
ano_bissexto = ((ano_divisivel_4 == 0) and (ano_divisivel_100 != 0)) or (ano_divisivel_400 == 0)

if ano_bissexto == True:
    print(f"O ano {ano} é Bissexto.")
else:
    print(f"O ano {ano} Não é Bissexto.")