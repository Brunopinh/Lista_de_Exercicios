# 77. Escreva um programa que simule uma calculadora com funções para as 4 operações.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

while True:
    print("\nCalculadora Simples:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    opcao = input("Escolha uma operação (1-5): ")

    if opcao == '5':
        print("Saindo da calculadora.")
        break
    
    if opcao in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = somar(num1, num2)
            elif opcao == '2':
                resultado = subtrair(num1, num2)
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
            elif opcao == '4':
                resultado = dividir(num1, num2)
            
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
    else:
        print("Opção inválida.")