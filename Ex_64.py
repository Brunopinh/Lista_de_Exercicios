# 64. Escreva um programa que calcule a média móvel de uma lista de números.

entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [float(x) for x in entrada.split()]
janela = int(input("Digite o tamanho da janela para a média móvel: "))

media_movel = []
for i in range(len(numeros) - janela + 1):
    sub_lista = numeros[i:i + janela]
    media = sum(sub_lista) / janela
    media_movel.append(media)

print(f"Média móvel: {media_movel}")