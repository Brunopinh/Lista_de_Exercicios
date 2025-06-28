# 65. Escreva um programa que simule um sistema de cadastro de alunos com menu.

alunos = {}

while True:
    print("\nSistema de Cadastro de Alunos:")
    print("1. Adicionar Aluno")
    print("2. Ver Alunos")
    print("3. Atualizar Nota de Aluno")
    print("4. Remover Aluno")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        try:
            nota = float(input("Digite a nota do aluno: "))
            alunos[nome] = nota
            print(f"Aluno {nome} adicionado.")
        except ValueError:
            print("Nota inválida.")
    elif opcao == '2':
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("Lista de Alunos:")
            for nome, nota in alunos.items():
                print(f"Nome: {nome}, Nota: {nota}")
    elif opcao == '3':
        nome = input("Digite o nome do aluno para atualizar: ")
        if nome in alunos:
            try:
                nova_nota = float(input(f"Digite a nova nota para {nome}: "))
                alunos[nome] = nova_nota
                print(f"Nota de {nome} atualizada.")
            except ValueError:
                print("Nota inválida.")
        else:
            print("Aluno não encontrado.")
    elif opcao == '4':
        nome = input("Digite o nome do aluno para remover: ")
        if nome in alunos:
            del alunos[nome]
            print(f"Aluno {nome} removido.")
        else:
            print("Aluno não encontrado.")
    elif opcao == '5':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida.")