qtd_experimentos = int(input("Informe a quantidade de experimentos realizados: ")) # entrada
qtd_cobaia = 0
tipo_cobaia = ""
total_sapos = 0
total_ratos = 0
total_coelhos = 0
total_cobaias = 0
cont = 0 # variável de controle

while cont < qtd_experimentos:
    cont += 1 # atualiza a variável de controle
    qtd_cobaia = int(input(f"Informe a quantidade de cobaias do experimento {cont}: ")) # entrada relativa a cada experimento
    tipo_cobaia = str(input(f"Informe o tipo de cobaia do experimento {cont} (S:Sapo, R:Rato ou C:Coelho): ")) # entrada relativa a cada experimento
    if tipo_cobaia == "S":
        total_sapos += qtd_cobaia # soma a quantidade de cobaias do experimento à quantidade de sapos
    if tipo_cobaia == "R":
        total_ratos += qtd_cobaia # soma a quantidade de cobaias do experimento à quantidade de ratos
    if tipo_cobaia == "C":
        total_coelhos += qtd_cobaia # soma a quantidade de cobaias do experimento à quantidade de coelhos
    total_cobaias += qtd_cobaia # soma a quantidade de cobaias do experimento ao total de cobaias

percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")