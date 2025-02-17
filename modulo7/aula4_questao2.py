import os, re

frase = open('frase.txt', 'r')
frase_sem_pontuacao = frase.read().strip()
palavras = re.findall(r'\b[a-zA-ZáãâàéèêóôõÁÃÂÀÉÊÓÔÕ]+\b', frase_sem_pontuacao)
frase.close()

pal = open('palavras.txt', 'w')
for i in range(len(palavras)):
    pal.write(palavras[i]+"\n")
pal.close()

linha = open('palavras.txt', 'r')
linhas = linha.readlines()
linha.close()

for i in range(len(linhas)):
    print((linhas[i]), end="")