import random # importa biblioteca

def encrypt(lista):
    global chave_aleatoria
    chave_aleatoria = random.randint(1,10) # gera a chave aleatória (variável global)
    encrypted = [] # cria lista vazia
    palavra_encrypted = "" # estado inicial da variável local
    for palavra in lista:
        for letra in palavra:
            c = ord(letra) # verifica a ordem de cada caracter na tabela Unicode
            c += chave_aleatoria # soma a chave aleatória ao valor de c
            if (c >= 33) and (c <= 126): # verifica se o valor somado está dentro da faixa visível
                c = chr(c) # caso esteja, o valor do caracter é convertido de volta
            else:
                c = chr(33) # caso não esteja, sempre converterá o caracter 33
            palavra_encrypted += c # adiciona o caracter à palavra criptografada
        encrypted.append(palavra_encrypted) # adiciona a palavra criptografada à lista
        palavra_encrypted = "" # reinicia o estado da variável local
    return encrypted # retorna a lista criptografada

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

lista_criptografada = encrypt(nomes)

print(f"Lista original: {nomes}")
print(f"Chave aleatória: {chave_aleatoria}")
print(f"Lista criptografada: {lista_criptografada}")

# Exemplo de uso:
# nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
# chave_aleatoria = 5
# nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']