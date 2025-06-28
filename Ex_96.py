# 96. Escreva um programa que simule uma pilha (LIFO) com listas.

pilha = []

while True:
    print("\nSimulação de Pilha (LIFO):")
    print("1. Adicionar elemento (Push)")
    print("2. Remover elemento (Pop)")
    print("3. Ver Pilha")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        elemento = input("Digite o elemento para adicionar à pilha: ")
        pilha.append(elemento)
        print(f"'{elemento}' adicionado à pilha.")
    elif opcao == '2':
        if pilha:
            elemento_removido = pilha.pop() # Remove o último elemento (LIFO)
            print(f"'{elemento_removido}' removido da pilha.")
        else:
            print("A pilha está vazia.")
    elif opcao == '3':
        if not pilha:
            print("A pilha está vazia.")
        else:
            print(f"Pilha atual: {pilha}")
    elif opcao == '4':
        print("Saindo da simulação de pilha.")
        break
    else:
        print("Opção inválida.")