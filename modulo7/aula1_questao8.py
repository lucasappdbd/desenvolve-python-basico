### Verificador de CPF ###

def digito_verificador_1(cpf):
    numero_sem_digito = (cpf[0:3])+(cpf[4:7])+(cpf[8:11])   # separa os 9 primeiros dígitos do CPF
    multiplicacao = []  # cria lista vazia
    cont = 10   # define o primeiro valor a multiplicar por n (10)
    for n in numero_sem_digito:
        multiplicacao.append(int(n) * cont) # preenche a lista com valor de cada dígito multiplicado por "cont"
        cont -= 1
    soma = sum(multiplicacao)   # soma os valores dos elementos da lista
    divisao, resto = (soma // 11), (soma % 11)  # calcula a divisão exata e o resto da divisão por 11
    if resto < 2:   # verifica se o dígito será "zero"
        digito = 0
    else:           # calcula o dígito verificador
        digito = (11 - resto)
    return digito   # retorna o dígito verificador

def digito_verificador_2(cpf, digito_verificador_1):
    # separa os 9 primeiros dígitos do CPF + digito_verificador_1:
    numero_sem_digito = (cpf[0:3])+(cpf[4:7])+(cpf[8:11])+(str(digito_verificador_1))
    multiplicacao = []  # cria lista vazia
    cont = 11   # define o primeiro valor a multiplicar por n (11)
    for n in numero_sem_digito:
        multiplicacao.append(int(n) * cont) # preenche a lista com valor de cada dígito multiplicado por "cont"
        cont -= 1
    soma = sum(multiplicacao)   # soma os valores dos elementos da lista
    divisao, resto = (soma // 11), (soma % 11)  # calcula a divisão exata e o resto da divisão por 11
    if resto < 2:   # verifica se o dígito será "zero"
        digito = 0
    else:           # calcula o dígito verificador
        digito = (11 - resto)
    return digito   # retorna o dígito verificador

print("Digite o número do CPF a ser validado (com pontos e traço):")
cpf = input("CPF: ") # Entrada de dados

dv1 = digito_verificador_1(cpf)      # Processamento
dv2 = digito_verificador_2(cpf, dv1) # Processamento

cpf_valido = (cpf[0:3]) + "." + (cpf[4:7]) + "." + (cpf[8:11]) + "-" + str(dv1) + str(dv2) # Processamento

if cpf == cpf_valido:      # Processamento
    print("CPF válido!")   # Saída
else:
    print("CPF inválido!") # Saída