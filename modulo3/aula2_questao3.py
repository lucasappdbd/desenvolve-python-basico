# Entrada de dados
idade = int(input("Digite sua idade: "))
qtd_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
vitorias = int(input("Quantos jogos já venceu? "))
# Processamento
## Verifica se a idade está entre 16 e 18 anos
apto_idade = (idade >= 16) and (idade <= 18)
## Verifica se a pessoa já jogou pelo menos 3 jogos de tabuleiro
apto_jogos = qtd_jogos == "True"
## Verifica se a pessoa já venceu pelo menos 1 jogo
apto_vitorias = vitorias >= 1
## Verifica se os 3 requisitos acima foram cumpridos
apto_clube = apto_idade and apto_jogos and apto_vitorias
#Saída
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_clube}")