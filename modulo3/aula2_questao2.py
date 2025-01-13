# Entrada de dados
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))
# Processamento - verifica se Juliana ou Cris são maiores de idade
podem_entrar = (idade_juliana > 17) or (idade_cris > 17)
# Saída
print("Pelo menos uma das duas é maior de idade e podem entrar no bar?")
print(f"{podem_entrar}")