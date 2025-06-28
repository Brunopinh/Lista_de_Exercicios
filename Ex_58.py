# 58. Escreva um programa com uma função que retorne a mediana de uma lista de números.

def calcular_mediana(lista):
    if not lista:
        return None
    
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    
    if n % 2 == 1:
        mediana = lista_ordenada[n // 2]
    else:
        meio1 = lista_ordenada[n // 2 - 1]
        meio2 = lista_ordenada[n // 2]
        mediana = (meio1 + meio2) / 2
    return mediana

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [float(x) for x in entrada.split()]

mediana_calculada = calcular_mediana(numeros)
if mediana_calculada is not None:
    print(f"A mediana dos numeros e: {mediana_calculada:.2f}")
else:
    print("Nenhum numero foi digitado.")