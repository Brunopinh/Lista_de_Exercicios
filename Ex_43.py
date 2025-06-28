# 43. Escreva um programa que leia uma lista e calcule a soma dos elementos na diagonal de uma matriz.

print("Digite a matriz (cada linha separada por Enter, elementos por espaço). Digite uma linha vazia para terminar:")
matriz = []
while True:
    linha_str = input()
    if not linha_str:
        break
    matriz.append([int(x) for x in linha_str.split()])

soma_diagonal = 0
for i in range(len(matriz)):
    if i < len(matriz[i]):
        soma_diagonal += matriz[i][i]
print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")