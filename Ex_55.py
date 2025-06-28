# 55. Escreva um programa que crie um menu interativo com opções de cálculo simples.

while True:
    print("\nMenu de Calculos:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    opcao = input("Escolha uma opcao (1-5): ")

    if opcao == '5':
        print("Saindo do programa.")
        break
    elif opcao in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))

            if opcao == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisao por zero nao e permitida.")
        except ValueError:
            print("Entrada invalida. Por favor, digite numeros.")
    else:
        print("Opcao invalida. Tente novamente.")