# 35. Ler uma lista de números e calcular a média

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [float(x) for x in entrada.split()]
if numeros:
    media = sum(numeros) / len(numeros)
    print(f"A media dos numeros e: {media:.2f}")
else:
    print("Nenhum numero foi digitado.")