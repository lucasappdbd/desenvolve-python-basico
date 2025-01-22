# entrada para lista 1
num_elementos = int(input("Digite a quantidade de elementos da Lista 1: "))
print(f"Digite os {num_elementos} elementos da Lista 1:")

lista1 = list() # cria lista vazia

# preenche a lista 1
for i in range(num_elementos):
    elemento = int(input())
    lista1.append(elemento)

lista2 = list() # cria lista vazia

# entrada para lista 2
num_elementos = int(input("Digite a quantidade de elementos da Lista 2: "))
print(f"Digite os {num_elementos} elementos da Lista 2:")

# preenche a lista 2
for i in range(num_elementos):
    elemento = int(input())
    lista2.append(elemento)

lista_intercalada = list() # cria lista vazia

diferenca = abs((len(lista1)) - (len(lista2))) # calcula diferença de tamanho das listas

# preenche a lista intercalada com um valor da lista 1 e valor da lista 2 alternadamente
if (len(lista1)) >= (len(lista2)):
    for i in range (len(lista1) - (diferenca)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
else:
    for i in range (len(lista2) - (diferenca)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

# termina de preencher a lista intercalada quando a lista menor já não possui mais nenhum elemento para alternar
if (len(lista1)) >= (len(lista2)):
    for i in range((len(lista2)), (len(lista2) + diferenca)):
        lista_intercalada.append(lista1[i])
else:
    for i in range((len(lista1)), (len(lista1) + diferenca)):
        lista_intercalada.append(lista2[i])

# exibe a lista intercalada
print(f"Lista intercalada: {lista_intercalada}")