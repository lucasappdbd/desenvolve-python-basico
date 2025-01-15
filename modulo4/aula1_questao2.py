n = int(input("Digite o valor de N: "))
cont = 0
while n < cont: # Se (n < 0), o loop será infinito. Se (n >= 0), o loop não será executado.
    cont = cont + 1
    print(cont)
print("Fim")


# OBS: Provavelmente a instrução do exercício inverteu o sinal da condição do 'while'.
# Se a condição pedida fosse 'while n > cont:' o código executaria sem loop infinito.


# O código 'corrigido' está comentado abaixo:

# n = int(input("Digite o valor de N: "))
# cont = 0
# while n > cont:
#    cont = cont + 1
#    print(cont)
# print("Fim")