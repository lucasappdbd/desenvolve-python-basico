frase = input("Digite a frase: ")

espacos = 0

for i in range(len(frase)):
    if frase[i] == " ":
        espacos += 1

print(f"Espaços em branco: {espacos}")

# Exemplo de uso:
# Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
# Espaços em branco: 11