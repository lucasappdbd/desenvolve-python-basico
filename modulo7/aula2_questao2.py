frase = input("Digite uma frase: ")

frase_lista = frase.split(" ")
palavra_modificada = ""
frase_modificada =[]

for palavra in frase_lista:
    for letra in range(len(palavra)):
        if palavra[letra] not in "AEIOUaeiou":
            palavra_modificada += palavra[letra]
        else:
            palavra_modificada += "*"
    frase_modificada.append(palavra_modificada)
    palavra_modificada = ""

frase_modificada = " ".join(frase_modificada)

print(f"Frase modificada: {frase_modificada}")

# Exemplo de uso:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**