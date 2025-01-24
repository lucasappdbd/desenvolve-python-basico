lista = list()
cont = 0

print("Informe uma sequência de números inteiros: ")

while True:
    cont += 1
    if cont <= 4:
        n = int(input("Valor: "))
        lista.append(n)
    elif cont == 5:
        print("Para PARAR digite 0.")
        n = int(input("Valor: "))
        if n == 0:
            break
        lista.append(n)
    elif cont > 5:
        n = int(input("Valor: "))
        if n == 0:
            break
        lista.append(n)

print(f"Lista original: {lista}")
print(f"3 Primeiros elementos: {lista[0:3]}")
print(f"2 últimos elementos: {lista[((len(lista)) - 2):(len(lista) + 1)]}")
print(f"Lista invertida: {lista[::-1]}")
print(f"Elementos de índice PAR: {lista[::2]}")
print(f"Elementos de índice ÍMPAR: {lista[1:len(lista):2]}")