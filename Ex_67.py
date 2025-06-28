# 67. Escreva um programa que simule uma lista de tarefas com status (pendente/concluído).

tarefas = []
id_tarefa = 1

while True:
    print("\nLista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        descricao = input("Digite a descrição da tarefa: ")
        tarefas.append({'id': id_tarefa, 'descricao': descricao, 'status': 'pendente'})
        print(f"Tarefa '{descricao}' adicionada com ID {id_tarefa}.")
        id_tarefa += 1
    elif opcao == '2':
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("Tarefas:")
            for tarefa in tarefas:
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}")
    elif opcao == '3':
        try:
            id_concluir = int(input("Digite o ID da tarefa para marcar como concluída: "))
            encontrada = False
            for tarefa in tarefas:
                if tarefa['id'] == id_concluir:
                    tarefa['status'] = 'concluído'
                    print(f"Tarefa ID {id_concluir} marcada como concluída.")
                    encontrada = True
                    break
            if not encontrada:
                print("Tarefa não encontrada.")
        except ValueError:
            print("ID inválido.")
    elif opcao == '4':
        print("Saindo da lista de tarefas.")
        break
    else:
        print("Opção inválida.")