frase = input("Digite uma frase: ")
objetivo = sorted(input("Digite a palavra objetivo: "))

lista_palavras = frase.lower().split(" ")
anagramas = []

for palavra in lista_palavras:
    if sorted(palavra) == objetivo:
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")

# Exemplo de uso:
# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor
# Anagramas: ["amor", "mora", "ramo", "Roma"]