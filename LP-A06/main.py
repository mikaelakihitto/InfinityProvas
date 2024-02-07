import data
import function




tarefas = []

while True:
    function.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        break
    elif opcao == '1':
        nova_tarefa = data.task.copy()
        nova_tarefa['nome'] = input("Nome da tarefa: ")
        nova_tarefa['descricao'] = input("Descrição da tarefa: ")
        nova_tarefa['prioridade'] = input("Prioridade da tarefa: ")
        nova_tarefa['categoria'] = input("Categoria da tarefa: ")
        function.adicionar_tarefa(tarefas, nova_tarefa)
    elif opcao == '2':
        function.listar_tarefas(tarefas)
    elif opcao == '3':
        function.listar_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa concluída: "))
        function.marcar_tarefa_concluida(tarefas, indice)
    elif opcao == '4':
        prioridade = input("Digite a prioridade desejada: ")
        function.exibir_tarefas_por_prioridade(tarefas, prioridade)
    elif opcao == '5':
        categoria = input("Digite a categoria desejada: ")
        function.exibir_tarefas_por_categoria(tarefas, categoria)
    else:
        print("Opção inválida. Tente novamente.")
