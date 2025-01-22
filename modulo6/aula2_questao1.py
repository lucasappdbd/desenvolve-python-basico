import random # importa biblioteca

lista = [] # cria lista vazia

for i in range(20):
    lista.append(random.randint(-100,100)) # preenche a lista

lista_ordenada = sorted(lista) # cria uma lista ordenada com base nos elementos da lista

maior = max(lista) # verifica maior valor da lista
menor = min(lista) # verifica menor valor da lista

# saída
print(f"Lista ordenada: {lista_ordenada}")
print(f"Lista original: {lista}")
print(f"Maior valor: {maior}, índice: {lista.index(maior)}")
print(f"Menor valor: {menor}, índice: {lista.index(menor)}")