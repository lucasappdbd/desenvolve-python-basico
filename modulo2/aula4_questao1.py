comprimento = int(input("Informe o comprimento do terreno em metros: "))
largura = int(input("Informe a largura do terreno em metros: "))
preco_m2 = float(input("Informe o valor do metro quadrado em R$: "))
# Calcular a área do terreno:
area_m2 = comprimento * largura
# Calcular o preço do terreno:
preco_total = preco_m2 * area_m2
# Exibir a área e preço do terreno:
print(f"O terreno possui {area_m2} m2 e custa R$ {preco_total:,.2f}.")