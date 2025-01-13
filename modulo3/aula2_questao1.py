# Entrada de dados
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))
# Processamento - verifica se Juliana e Cris são maiores de idade
podem_entrar = (idade_juliana > 17) and (idade_cris > 17)
# Saída
print("Ambas são maiores de idade e podem entrar no bar?")
print(f"{podem_entrar}")