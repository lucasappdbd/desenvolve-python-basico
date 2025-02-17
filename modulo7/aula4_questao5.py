import os

cabecalho = ["Título", "Autor", "Ano de publicação", "Número de páginas"]

livros = [
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Harry Potter e a Pedra Filosofal",
    "As Crônicas de Nárnia: O Leão a Feiticeira e o Guarda-Roupa",
    "A Terra das Sombras",
    "A Guerra dos Tronos",
    "O Hobbit",
    "O Nome do Vento",
    "O Ciclo da Herança: Eragon",
    "O Mago",
    "Percy Jackson e os Olimpianos: O Ladrão de Raios"
]

autores = [
    "J.R.R. Tolkien",
    "J.K. Rowling",
    "C.S. Lewis",
    "Terry Goodkind",
    "George R.R. Martin",
    "J.R.R. Tolkien",
    "Patrick Rothfuss",
    "Christopher Paolini",
    "Raymond E. Feist",
    "Rick Riordan"
]

anos = [1954, 1997, 1950, 1994, 1996, 1937, 2007, 2002, 1982, 2005]

paginas = [423, 223, 208, 464, 694, 310, 662, 503, 416, 377]

f = open('livros.csv', 'w')
f.write(",".join(cabecalho))
f.write("\n")
for i in range(len(livros)):
    f.write(livros[i])
    f.write(",")
    f.write(autores[i])
    f.write(",")
    f.write(str(anos[i]))
    f.write(",")
    f.write(str(paginas[i]))
    f.write("\n")
f.close()

print(f"Arquivo salvo em {os.path.abspath('livros.csv')}")