pares = [i for i in range(20,51) if i%2 == 0]
print(f"Números pares entre 20 e 50: {pares}")

quadrados = [i**2 for i in range(1,(len([1,2,3,4,5,6,7,8,9])+1))]
print(f"Quadrados de 1 a 9: {quadrados}")

divisiveis_7 = [i for i in range(0,101) if i%7 == 0]
print(f"Números divisíveis por 7 entre 0 e 100: {divisiveis_7}")

paridade = ["par" if i%2 == 0 else "ímpar" for i in range(0,30,3)]
print(f"Paridade entre 0 e 30 com pulo 3: {paridade}")