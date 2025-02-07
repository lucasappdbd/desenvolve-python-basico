import random

def embaralhar_palavras(frase):
    frase_embaralhada = []
    for i in range(len(palavras)):
        palavra = palavras[i]
        palavra_embaralhada = []
        if len(palavra) > 1:        
            for letra in range(len(palavra)):
                palavra_embaralhada.append(palavra[letra])
            palavra = palavra_embaralhada
            primeira_letra = [palavra_embaralhada[0]]
            ultima_letra = [palavra_embaralhada[-1]]
            meio_da_palavra = palavra_embaralhada[1:-1]
            random.shuffle(meio_da_palavra)
            palavra_embaralhada = []
            palavra_embaralhada += primeira_letra
            palavra_embaralhada += meio_da_palavra
            palavra_embaralhada += ultima_letra
            palavra_embaralhada = "".join(palavra_embaralhada)
            frase_embaralhada.append(palavra_embaralhada)
        else:
            for letra in range(len(palavra)):
                palavra_embaralhada.append(palavra[letra])
            palavra_embaralhada = "".join(palavra_embaralhada)
            frase_embaralhada.append(palavra_embaralhada)
    frase_embaralhada = " ".join(frase_embaralhada)
    return(frase_embaralhada)

frase = input("Digite uma frase: ")

palavras = frase.split(" ")

frase_embaralhada = embaralhar_palavras(frase)

print(f"Frase embaralhada: {frase_embaralhada}")