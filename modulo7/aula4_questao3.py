import os

f = open('estomago.txt', 'r')
arquivo = os.path.abspath('estomago.txt')
print(f"Arquivo aberto:\n{arquivo}\n")
linhas = f.readlines()
f.close()

# Texto das primeiras 25 linhas:
print("As 25 primeiras linhas do arquivo são:\n")
for i in range(25):
    print(linhas[i], end="")
print()

# Número de linhas do arquivo:
numero_linhas = 1  # inicia a contagem na linha 1
for linha in range(len(linhas)):
    numero_linhas += 1
print(f"O arquivo possui {numero_linhas} linhas.")

# Linha com maior número de caracteres:
maior_linha = 1
comprimento = 0
for linha in range(len(linhas)):
    if len(linhas[linha]) > comprimento:
        maior_linha = linha + 1
        comprimento = len(linhas[linha])
print(f"A linha {maior_linha} é a maior, e possui {comprimento} caracteres.")

# Número de menções de "Nonato" e "Íria"
mencoes_nonato = 0
mencoes_iria = 0

for i in range(len(linhas)):
    mencoes_nonato += linhas[i].count("Nonato")
    mencoes_nonato += linhas[i].count("nonato")
    mencoes_nonato += linhas[i].count("NONATO")
    mencoes_iria += linhas[i].count("Íria")
    mencoes_iria += linhas[i].count(" Iria")
    mencoes_iria += linhas[i].count("íria")
    mencoes_iria += linhas[i].count(" iria")
    mencoes_iria += linhas[i].count("ÍRIA")
    mencoes_iria += linhas[i].count(" IRIA")

print(f"Número de menções:\nNonato: {mencoes_nonato}\nÍria: {mencoes_iria}")