n = int(input("Informe a quantidade de respondentes: ")) # entrada
idade = 0 # valor inicial da soma das idades
cont = 0 # variável de controle

while cont < n:
    cont += 1
    idade += int(input(f"Digite a idade da pessoa {cont}: ")) # entrada e soma das idades informadas

media = idade / n # calcula a média das idades

print(f"Média entre as {n} idades informadas: {media:.2f} anos. ")