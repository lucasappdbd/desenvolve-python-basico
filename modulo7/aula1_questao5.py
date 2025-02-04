frase = input("Digite uma frase: ")

count_vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        count_vogais += 1
        indices.append(i)

print(count_vogais, " vogais")
print("Índices: ", indices)

# Exemplo de uso:
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# 19 vogais
# Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]