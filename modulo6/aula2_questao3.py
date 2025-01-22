import random # importa biblioteca

# cria listas vazia
lista1 = []
lista2 = []
interseccao = []

# preenche 20 elementos de cada lista
for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

# verifica os elementos em comum entre as listas 1 e 2; preenche a lista intersecção sem repetir os valores
for i in range(20):
    if (lista1[i] in lista2) and (not(lista1[i] in interseccao)):
        interseccao.append(lista1[i])

# ordena os elementos da lista intersecção
interseccao.sort()

# exibe as listas
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Intersecção: {interseccao}")

# exibe a quantidade de vezes que cada elemento em comum se repete nas 2 listas
for i in range(len(interseccao)):
    print(f"{interseccao[i]}: Lista 1 = {lista1.count(interseccao[i])} , ", end = "")
    print(f"Lista 2 = {lista2.count(interseccao[i])}")