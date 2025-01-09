temperatura_F = int(input("Informe a temperatura em graus Fahrenheit: "))
# Converter a temperatura para graus Celsius:
temperatura_C = (temperatura_F - 32) * (5/9)
# Exibir a temperatura convertida em graus Celsius:
print(f"{temperatura_F} graus Fahrenheit são {temperatura_C:.0f} graus Celsius.")