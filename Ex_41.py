# 41. Escreva um programa que leia uma lista de números e conte quantos são pares e ímpares.

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]
pares = 0
impares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")