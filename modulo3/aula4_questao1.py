# Entrada de dados
x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))

# Processamento e saída
soma = x + y
resto = soma % 2

print(f"{x} + {y} = {soma}.")
if resto == 0:
    print(f"{soma} é um número PAR.")
else:
    print(f"{soma} é um número ÍMPAR.")