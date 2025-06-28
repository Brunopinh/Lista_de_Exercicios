# 66. Escreva um programa que simule uma agenda de contatos utilizando dicionários.

agenda = {}

while True:
    print("\nAgenda de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        agenda[nome] = {'telefone': telefone, 'email': email}
        print(f"Contato {nome} adicionado.")
    elif opcao == '2':
        if not agenda:
            print("Nenhum contato na agenda.")
        else:
            print("Lista de Contatos:")
            for nome, dados in agenda.items():
                print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")
    elif opcao == '3':
        nome = input("Digite o nome do contato para buscar: ")
        if nome in agenda:
            dados = agenda[nome]
            print(f"Contato encontrado - Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")
        else:
            print("Contato não encontrado.")
    elif opcao == '4':
        nome = input("Digite o nome do contato para remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido.")
        else:
            print("Contato não encontrado.")
    elif opcao == '5':
        print("Saindo da agenda.")
        break
    else:
        print("Opção inválida.")