# 44. Escreva um programa que crie uma matriz n x n com valores aleatórios de 0 a 1.

import random

n = int(input("Digite o tamanho da matriz (n): "))
matriz = []
for _ in range(n):
    linha = []
    for _ in range(n):
        linha.append(random.random())
    matriz.append(linha)

print("Matriz gerada:")
for linha in matriz:
    print([f"{x:.2f}" for x in linha])