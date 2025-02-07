def verifica_palindromo(frase):
    global letras_frase
    letras_frase = frase.lower().split(" ")
    letras_frase = "".join(letras_frase)
    palavras = []
    for letra in range(len(letras_frase)):
        if letras_frase[letra] in "abcdefghijklmnopqrstuvwxyzç0123456789":
            palavras.append(letras_frase[letra])
    palavras = "".join(palavras)
    letras_frase = palavras    
    frase_invertida = []
    for letra in range(len(letras_frase) + 1):
        if letra > 0:
            frase_invertida.append(letras_frase[-letra])
    frase_invertida = "".join(frase_invertida)
    return frase_invertida

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase == "fim":
        print("Execução finalizada!")
        break
    frase_invertida = verifica_palindromo(frase)
    if letras_frase == frase_invertida:
        print(f'"{frase}" é palíndromo.')
    else:
        print(f'"{frase}" não é palíndromo.')