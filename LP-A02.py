# Solicita a velocidade do carro ao usuário
velocidade_carro = float(input("Digite a velocidade do carro em km/h: "))

# Limite de velocidade
limite_velocidade = 80

# Verifica se a velocidade ultrapassou o limite
if velocidade_carro > limite_velocidade:
    # Calcula a multa (R$20,00 por km excedido)
    km_excedido = velocidade_carro - limite_velocidade
    valor_multa = km_excedido * 20.0
    
    # Exibe a mensagem de multa e o valor
    print(f"Você foi multado! Velocidade excedida: {km_excedido:.2f} km/h")
    print(f"Valor da multa: R${valor_multa:.2f}")
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
