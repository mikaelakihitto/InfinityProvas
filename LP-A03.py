# Inicialização de variáveis
soma = 0
quantidade_numeros = 0

# Loop para ler números até que o usuário digite 0
while True:
    try:
        numero = int(input("Digite um número (digite 0 para encerrar): "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue
    
    # Verifica se o usuário digitou 0 para encerrar
    if numero == 0:
        break
    
    soma += numero
    quantidade_numeros += 1

# Calcula a média aritmética (evita divisão por zero)
media = soma / quantidade_numeros if quantidade_numeros != 0 else 0

# Exibe resultados
print("\nResultados:")
print(f"Quantidade de números digitados: {quantidade_numeros}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")
