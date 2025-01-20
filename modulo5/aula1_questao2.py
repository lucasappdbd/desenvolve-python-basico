import math # importa biblioteca
import random # importa biblioteca

n = int(input("Informe a quantidade de valores: ")) # entrada
cont = 0 # variável de controle
aleatorio = 0 # variável processamento
soma = 0 # variável processamento

while cont < n: # processamento
    cont += 1
    aleatorio = random.randint(0, 100)
    print(aleatorio)
    soma += aleatorio

print(f"Soma: {soma}")

raiz_quadrada = math.sqrt(soma) # processamento

print(f"Raiz quadrada: {raiz_quadrada}") # saída