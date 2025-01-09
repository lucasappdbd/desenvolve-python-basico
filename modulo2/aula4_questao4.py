valor = int(input("Digite o valor desejado em R$: "))
# Calcular quantidade de notas de 100 reais e valor restante:
notas_100 = valor // 100
resto_100 = valor % 100
# Calcular quantidade de notas de 50 reais e valor restante:
notas_50 = resto_100 // 50
resto_50 = resto_100 % 50
# Calcular quantidade de notas de 20 reais e valor restante:
notas_20 = resto_50 // 20
resto_20 = resto_50 % 20
# Calcular quantidade de notas de 10 reais e valor restante:
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10
# Calcular quantidade de notas de 5 reais e valor restante:
notas_5 = resto_10 // 5
resto_5 = resto_10 % 5
# Calcular quantidade de notas de 2 reais e valor restante:
notas_2 = resto_5 // 2
resto_2 = resto_5 % 2
# Calcular quantidade de notas de 1 real:
notas_1 = resto_2
# Exibir a quantidade de notas:
print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")