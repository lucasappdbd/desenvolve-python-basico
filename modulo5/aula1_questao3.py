import random # importa biblioteca

aleatorio = random.randint(1,10) # gera número aleatório

while True: # processamento e saída
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == aleatorio:
        print(f"Correto! O número é {aleatorio}.")
        break
    elif palpite < aleatorio:
        print("Muito baixo, tente novamente!")
    elif palpite > aleatorio:
        print("Muito alto, tente novamente!")