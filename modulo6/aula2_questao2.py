import random # importa biblioteca

num_elementos = random.randint(5,20) # gera um número aletório de elementos

elementos = list() # cria lista vazia

for i in range(num_elementos):
    elementos.append(random.randint(1,10)) # preenche a lista

soma = sum(elementos) # soma os elementos
media = (sum(elementos)) / (len(elementos)) # calcula a média dos elementos

# saída
print(f"Lista: {elementos}")
print(f"Quantidade de elementos: {len(elementos)}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
