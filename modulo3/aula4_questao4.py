# Entrada de dados
distancia = float(input("Informe a distância (km): "))
peso_pacote = float(input("Informe o peso do pacote (kg): "))

# Processamento
## Distância até 100 km: R$ 1.00 por kg
if (distancia <= 100):
    valor_frete = peso_pacote * 1.00
## Distância entre 101 e 300 km: R$1.50 por kg
if (distancia >= 101 and distancia <= 300):
    valor_frete = peso_pacote * 1.50
## Distância acima de 300 km: R$ 2.00 por kg.
if (distancia > 300):
    valor_frete = peso_pacote * 2.00
## Taxa para pacotes com peso superior a 10 kg: R$ 10.00
if (peso_pacote > 10):
    valor_frete = valor_frete + 10.00

# Saída
print(f"O valor do frete é R$ {valor_frete:.2f}.")