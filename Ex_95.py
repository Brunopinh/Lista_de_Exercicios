# 95. Escreva um programa que simule uma fila (FIFO) com listas.

fila = []

while True:
    print("\nSimulação de Fila (FIFO):")
    print("1. Adicionar elemento (Enqueue)")
    print("2. Remover elemento (Dequeue)")
    print("3. Ver Fila")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        elemento = input("Digite o elemento para adicionar à fila: ")
        fila.append(elemento)
        print(f"'{elemento}' adicionado à fila.")
    elif opcao == '2':
        if fila:
            elemento_removido = fila.pop(0) # Remove o primeiro elemento (FIFO)
            print(f"'{elemento_removido}' removido da fila.")
        else:
            print("A fila está vazia.")
    elif opcao == '3':
        if not fila:
            print("A fila está vazia.")
        else:
            print(f"Fila atual: {fila}")
    elif opcao == '4':
        print("Saindo da simulação de fila.")
        break
    else:
        print("Opção inválida.")