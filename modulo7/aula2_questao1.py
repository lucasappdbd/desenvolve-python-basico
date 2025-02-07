data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(data[3:5])
dia = data[0:2]
mes = meses[mes-1]
ano = data[6:10]
data_por_extenso = (f"{dia} de {mes} de {ano}")

print(f"Você nasceu em {data_por_extenso}.")