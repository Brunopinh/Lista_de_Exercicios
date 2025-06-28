# 61. Escreva um programa que calcule a matriz transposta.

print("Digite a matriz (cada linha separada por Enter, elementos por espaço). Digite uma linha vazia para terminar:")
matriz_original = []
while True:
    linha_str = input()
    if not linha_str:
        break
    matriz_original.append([int(x) for x in linha_str.split()])

if not matriz_original:
    print("Matriz vazia.")
else:
    num_linhas = len(matriz_original)
    num_colunas = len(matriz_original[0])

    matriz_transposta = []
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(matriz_original[i][j])
        matriz_transposta.append(nova_linha)

    print("Matriz Transposta:")
    for linha in matriz_transposta:
        print(linha)