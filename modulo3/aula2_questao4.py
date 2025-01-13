# Entrada de dados
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))
# Processamento
## Verifica a consistência de pontos para cada classe
consist_guerreiro = (classe == "guerreiro") and (forca >= 15) and (magia <= 10)
consist_mago = (classe == "mago") and (forca <= 10) and (magia >= 15)
consist_arqueiro = (classe == "arqueiro") and ((forca > 5) and (forca <= 15)) and ((magia > 5) and (magia <= 15))
## Verifica se alguma das condições acima foi atendida
consistente = consist_guerreiro or consist_mago or consist_arqueiro
# Saída
print(f"Pontos de atributo consistentes com a classe escolhida: {consistente}")