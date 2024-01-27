def calcular_media(notas):
    total_notas = len(notas)
    if total_notas > 0:
        soma = sum(notas)
        media = soma / total_notas
        return media
    else:
        return 0  # Retorna 0 se não houver notas para evitar divisão por zero

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Solicitar ao usuário digitar as notas
notas = []
while True:
    nota_str = input("Digite uma nota (ou 's' para sair): ")
    
    if nota_str.lower() == 's':
        break
    
    try:
        nota = float(nota_str)
        if nota < 0 or nota >10:
            print('Por favor, digite um número entre 0 e 10')
        else:    
            notas.append(nota)
    except ValueError:
        print("Por favor, digite um número válido.")

# Calcular a média
media_aluno = calcular_media(notas)

# Verificar situação e exibir resultado
situacao_aluno = verificar_situacao(media_aluno)
print(f"\nMédia do aluno: {media_aluno:.2f}")
print(f"Situação do aluno: {situacao_aluno}")
