# 36. Ler uma lista de números e ordenar em ordem crescente

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]
numeros.sort()
print(f"Numeros em ordem crescente: {numeros}")
