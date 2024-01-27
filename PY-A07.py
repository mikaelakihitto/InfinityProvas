def AdicionarAluno(alunos_dict):
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o número de matrícula do aluno: ')
    if not (matricula in alunos_dict):
        alunos_dict[matricula] = nome
        print(f'Aluno {nome} adicionado com sucesso!')
    else :
        print(f'Matricula:{matricula} ja esta sendo usada') 

def RemoverAluno(alunos_dict):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos_dict:
        nome = alunos_dict.pop(matricula)
        print(f'Aluno {nome} removido com sucesso!')
    else:
        print('Número de matrícula não encontrado.')

def AtualizarAluno(alunos_dict):
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos_dict:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos_dict[matricula] = novo_nome
        print(f'Nome do aluno atualizado com sucesso!')
    else:
        print('Número de matrícula não encontrado.')

def VerAlunos(alunos_dict):
    print('\nLista de alunos:')
    for matricula, nome in alunos_dict.items():
        print(f'Matricula: {matricula} - Nome: {nome}')

def main():
    alunos = {}  # Dicionário para armazenar os alunos
    while True:
        print('\nEscolha uma opção:')
        print('1. Adicionar aluno')
        print('2. Remover aluno')
        print('3. Atualizar aluno')
        print('4. Ver alunos')
        print('5. Sair')

        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            AdicionarAluno(alunos)
        elif opcao == '2':
            RemoverAluno(alunos)
        elif opcao == '3':
            AtualizarAluno(alunos)
        elif opcao == '4':
            VerAlunos(alunos)
        elif opcao == '5':
            print('Saindo do programa. Até logo!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
