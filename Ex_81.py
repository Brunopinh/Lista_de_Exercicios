# 81. Escreva um programa que utilize map, filter e reduce em uma lista de números.

from functools import reduce

# Exemplo de lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando map: dobrar cada número
dobrados = list(map(lambda x: x * 2, numeros))
print(f"Números dobrados (map): {dobrados}")

# Usando filter: obter apenas números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares (filter): {pares}")

# Usando reduce: somar todos os números
soma_total = reduce(lambda x, y: x + y, numeros)
print(f"Soma total (reduce): {soma_total}")