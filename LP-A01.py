# Exemplo de variáveis
# Tipagem int
idade = 25

# Tipagem float
altura = 1.75

# Tipagem str
nome = "Alice"

# Tipagem bool
tem_gato = True

# Solicitação de dados ao usuário
usuario_nome = input("Digite seu nome: ")
usuario_idade = int(input("Digite sua idade: "))
usuario_altura = float(input("Digite sua altura em metros: "))
tem_animal_estimacao = input("Você tem algum animal de estimação? (Sim/Não): ").lower() == "sim"

# Imprimir solicitação na tela com mensagem personalizada
print("\nInformações do usuário:")
print(f"Nome: {usuario_nome}")
print(f"Idade: {usuario_idade} anos")
print(f"Altura: {usuario_altura} metros")
print(f"Possui animal de estimação? {tem_animal_estimacao}")
