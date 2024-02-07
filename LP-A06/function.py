# Função para adicionar uma tarefa
def adicionar_tarefa(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)

# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    for index, tarefa in enumerate(tarefas, 1):
        print(f"{index}. {tarefa['nome']} - {tarefa['descricao']}")

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice - 1]['concluida'] = True

# Função para exibir tarefas por prioridade
def exibir_tarefas_por_prioridade(tarefas, prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    listar_tarefas(tarefas_filtradas)

# Função para exibir tarefas por categoria
def exibir_tarefas_por_categoria(tarefas, categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    listar_tarefas(tarefas_filtradas)

# Função para exibir menu
def exibir_menu():
    print("")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("0. Sair")
