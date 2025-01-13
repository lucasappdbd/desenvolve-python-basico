# Entrada de dados
genero = input("Informe seu gênero (M ou F): ")
idade = int(input("Informe sua idade: "))
tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))
# Processamento
## Compara o gênero com a idade (feminino maior ou igual a 60 anos, masculino maior ou igual a 65 anos)
aposentar_por_idade = ((genero == "F") and (idade >= 60)) or ((genero =="M") and (idade >= 65))
## Verifica se o tempo de serviço é maior ou igual a 30 anos
aposentar_por_tempo = tempo_servico >= 30
## Verifica se a pessoa tem 60 anos e tempo de serviço maior ou igual a 25 anos
aposentar_por_idade_e_tempo = (idade >= 60) and (tempo_servico >= 25)
## Verifica se pelo menos uma das condições acima foi atendida
pode_aposentar = aposentar_por_idade or aposentar_por_tempo or aposentar_por_idade_e_tempo
# Saída
print(f"Você já pode se aposentar? {pode_aposentar}")