nome = input("Digite seu nome: ")

for i in range(len(nome) + 1):
    if i != 0:
        print(nome[0:i])