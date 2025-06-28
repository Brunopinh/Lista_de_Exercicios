# 79. Escreva um programa que implemente o algoritmo de ordenação quicksort.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    
    return quicksort(esquerda) + meio + quicksort(direita)

entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [float(x) for x in entrada.split()]

lista_ordenada = quicksort(numeros)
print(f"Lista ordenada por Quicksort: {lista_ordenada}")