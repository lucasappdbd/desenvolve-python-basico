f = open('spotify-2023.csv', 'r', encoding='latin-1')

conteudo = f.read()
conteudo = conteudo.split("\n")
f.close()

linhas = [conteudo[i] for i in range(len(conteudo))]

cabecalho = []
cabecalho.append(linhas[0])
cabecalho = "".join(cabecalho)
cabecalho = cabecalho.split(",")

linhas_filtradas = []

for i in range(1, len(linhas)):
    linha = linhas[i]
    linha = linha.split(",")
    if len(linha) == len(cabecalho):
        linhas_filtradas.append([linha])

streams_ano = 0

mais_tocadas = []

tocadas = []
maior = 0

for ano in range(2012, 2023):
    streams_ano = 0
    tocadas_ano = []

    for i in range(len(linhas_filtradas)):

        if int(linhas_filtradas[i][0][3]) == ano:
            valor = int(linhas_filtradas[i][0][8])
            if valor > streams_ano:
                streams_ano = valor
                tocadas_ano = [(valor, linhas_filtradas[i][0])]
            elif valor == streams_ano:
                tocadas_ano.append((valor, linhas_filtradas[i][0]))

    tocadas.extend(tocadas_ano)

indices_filtrar = [0, 1, 3, 8]

lista_formatada = [[item[1][pos] for pos in indices_filtrar] for item in tocadas]

print("[", end="")
for item in lista_formatada:
    if lista_formatada.index(item) < (len(lista_formatada) - 1):
        print(f"{item},")
    elif lista_formatada.index(item) == (len(lista_formatada) - 1):
        print(f"{item}", end="")
print("]")