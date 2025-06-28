# 54. Escreva um programa que gere um histograma com uma lista de números.

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]

if not numeros:
    print("Nenhum numero foi digitado.")
else:
    frequencia = {}
    for num in numeros:
        frequencia[num] = frequencia.get(num, 0) + 1

    print("Histograma:")
    for num in sorted(frequencia.keys()):
        print(f"{num}: {'*' * frequencia[num]}")