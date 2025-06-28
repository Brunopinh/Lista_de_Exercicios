# 53. Escreva um programa que calcule a moda de uma lista de números.

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]

if not numeros:
    print("Nenhum numero foi digitado.")
else:
    frequencia = {}
    for num in numeros:
        frequencia[num] = frequencia.get(num, 0) + 1

    max_frequencia = 0
    moda = []
    for num, freq in frequencia.items():
        if freq > max_frequencia:
            max_frequencia = freq
            moda = [num]
        elif freq == max_frequencia and num not in moda:
            moda.append(num)
    
    if len(moda) == len(numeros) and max_frequencia == 1:
        print("Nao ha moda clara (todos os numeros aparecem uma vez).")
    else:
        print(f"A(s) moda(s) da lista e(sao): {moda}")