# Configurações
senha_cadastrada = "1234"
tentativas_maximas = 3

# Inicialização do celular
print("Bem-vindo! Por favor, inicialize seu celular.")

# Loop para solicitar senha
for tentativa in range(tentativas_maximas):
    senha_digitada = input("Digite sua senha: ")

    # Verifica se a senha está correta
    if senha_digitada == senha_cadastrada:
        print("Senha correta. Bem-vindo!")
        break  # Sai do loop se a senha estiver correta
    else:
        tentativas_restantes = tentativas_maximas - (tentativa + 1)
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")
        else:
            print("Senha incorreta. Seu celular foi bloqueado.")
            break  # Sai do loop se atingir o número máximo de tentativas

# Código a ser executado após a inicialização bem-sucedida
if tentativas_restantes > 0:
    print("Inicialização bem-sucedida. Bem-vindo ao seu celular!")
