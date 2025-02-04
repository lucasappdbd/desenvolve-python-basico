celular = input("Digite o número: ")

if len(celular) == 9:
    numero_completo = (f"{celular[0:5]}-{celular[5:10]}")
if len(celular) == 8:
    numero_completo = (f"9{celular[0:4]}-{celular[4:9]}")

print(f"Número completo: {numero_completo}")