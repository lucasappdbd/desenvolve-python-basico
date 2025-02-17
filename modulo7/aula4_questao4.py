import os, random

def imprime_enforcado(erros):
    f = open('gabarito_enforcado.txt', 'r')
    forca = f.read().split("\n")
    f.close()

    if erros == 0:
        for i in range(0,5):
            print(forca[i])
    elif erros == 1:
        for i in range(6,11):
            print(forca[i])
    elif erros == 2:
        for i in range(12,17):
            print(forca[i])
    elif erros == 3:
        for i in range(18,23):
            print(forca[i])
    elif erros == 4:
        for i in range(24,29):
            print(forca[i])
    elif erros == 5:
        for i in range(30,35):
            print(forca[i])
    elif erros == 6:
        for i in range(36,41):
            print(forca[i])
    if erros == 6:
        print("Você perdeu!!!")
        global palavra_secreta
        print(f"A palavra era {"".join(palavra_secreta)}.")

f1 = open('gabarito_forca.txt', 'r')
palavras = f1.read().split("\n")
f1.close()
n = random.randint(0,9)
palavra_secreta = palavras[n]
palavra = ("_" * len(palavra_secreta))
palavra = [palavra[i] for i in range(len(palavra_secreta))]
palavra_secreta = [palavra_secreta[i] for i in range(len(palavra_secreta))]

erros = 0

print("########## JOGO DA FORCA ##########")

print(f"Palavra: {" ".join(palavra)}\n")
imprime_enforcado(erros)

while erros < 6:

    if palavra == palavra_secreta:
        print("Parabéns! Você acertou.")
        break

    else:

        letra = input("Digite uma letra: ")
        letra = letra.upper()

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):    
                if palavra_secreta[i] == letra:
                    palavra[i] = letra
        else:
            erros += 1

        print(f"Palavra: {" ".join(palavra)}\n")
        imprime_enforcado(erros)