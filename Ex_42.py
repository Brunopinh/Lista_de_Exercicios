# 42. Escreva um programa que leia uma lista de números e retorne apenas os múltiplos de 3.

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]
multiplos_de_3 = []
for num in numeros:
    if num % 3 == 0:
        multiplos_de_3.append(num)
print(f"Numeros multiplos de 3: {multiplos_de_3}")