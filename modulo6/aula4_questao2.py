lista_vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

frase = input("Digite uma frase: ")

vogais = sorted([frase[i] for i in range(len(frase)) if frase[i] in lista_vogais])
consoantes = [frase[i] for i in range(len(frase)) if not(frase[i] in lista_vogais) and (frase[i] != " ")]

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")