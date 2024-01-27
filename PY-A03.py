alunos = {}
while True:
    print('\nEscolha uma opção:')
    print('1. Adicionar aluno')
    print('2. Remover aluno')
    print('3. Visualizar alunos')
    print('4. Sair')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':

        nome = input('Digite o nome do aluno: ')
        matricula = input('Digite o número de matrícula do aluno: ')
        if not (matricula in alunos):
            alunos[matricula] = nome
            print(f'Aluno {nome} adicionado com sucesso!')
        else :
            print(f'Matricula:{matricula} ja esta sendo usada')    

    elif opcao == '2':

        matricula = input('Digite o número de matrícula do aluno que deseja remover: ')
        if matricula in alunos:
            nome = alunos.pop(matricula)
            print(f'Aluno {nome} removido com sucesso!')
        else:
            print('Número de matrícula não encontrado.')

    elif opcao == '3':
        print('Lista de alunos:')
        for matricula, nome in alunos.items():
            print(f'Matricula: {matricula} - Nome: {nome}')

    elif opcao == '4':
        print('Saindo do programa. Até logo!')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')