# 57. Escreva um programa com uma função que retorne a média de uma lista de números.

def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [float(x) for x in entrada.split()]

media_calculada = calcular_media(numeros)
print(f"A media dos numeros e: {media_calculada:.2f}")