def validador_senha(senha):
    comprimento = (len(senha) >= 8) # verifica se a senha possui pelo menos 8 caracteres
    lower_case = "" # define estado inicial da variável local
    upper_case = "" # define estado inicial da variável local
    number = ""     # define estado inicial da variável local
    special = ""    # define estado inicial da variável local
    for i in range(len(senha)):
        if senha[i] in "abcdefghijklmnopqrstuvwxyzç": # verifica se a senha possui pelo menos 1 letra minúscula
            lower_case = True # atualiza a variável local
            break
        else:
            lower_case = False
    for i in range(len(senha)):
        if senha[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ": # verifica se a senha possui pelo menos 1 letra maiúscula
            upper_case = True # atualiza a variável local
            break
        else:
            upper_case = False # atualiza a variável local
    for i in range(len(senha)):
        if senha[i] in "0123456789": # verifica se a senha possui pelo menos 1 número
            number = True # atualiza a variável local
            break
        else:
            number = False # atualiza a variável local
    for i in range(len(senha)):
        if senha[i] in "!@#$%¨&*(){[]}": # verifica se a senha possui pelo menos 1 caractere especial
            special = True # atualiza a variável local
            break
        else:
            special = False # atualiza a variável local   
    senha_forte = comprimento and lower_case and upper_case and number and special # verifica se todos os requisitos foram atendidos
    return senha_forte # retorna o resultado (True/False)
    
senha = input("Digite uma senha: ") # Entrada de dados

senha_forte = validador_senha(senha) # Processamento

if senha_forte == True: # Processamento
    print(f"{senha_forte} - A senha atende a todos critérios.") # Saída
else:
    print(f"{senha_forte} - A senha é fraca.") # Saída