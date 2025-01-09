descricao_p1 = input("Digite o nome do produto 1: ")
preco_unitario_p1 = float(input("Digite o preço unitário do produto 1: "))
qtd_p1 = int(input("Digite a quantidade do produto 1: "))
descricao_p2 = input("Digite o nome do produto 2: ")
preco_unitario_p2 = float(input("Digite o preço unitário do produto 2: "))
qtd_p2 = int(input("Digite a quantidade do produto 2: "))
descricao_p3 = input("Digite o nome do produto 3: ")
preco_unitario_p3 = float(input("Digite o preço unitário do produto 3: "))
qtd_p3 = int(input("Digite a quantidade do produto 3: "))
# Calcular preço total do item 1:
preco_p1 = preco_unitario_p1 * qtd_p1
# Calcular preço total do item 2:
preco_p2 = preco_unitario_p2 * qtd_p2
# Calcular preço total do item 3:
preco_p3 = preco_unitario_p3 * qtd_p3
# Calcular a soma total dos preços:
preco_total = preco_p1 + preco_p2 + preco_p3
# Exibir o valor total:
print(f"Total: R$ {preco_total:,.2f}.")