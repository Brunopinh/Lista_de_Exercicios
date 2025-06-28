# 84. Escreva um programa que gere uma matriz identidade de dimensão n.

n = int(input("Digite a dimensão (n) da matriz identidade: "))

matriz_identidade = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)

print("Matriz Identidade:")
for linha in matriz_identidade:
    print(linha)