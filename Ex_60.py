# 60. Escreva um programa com uma função que ordene uma lista usando o método bolha.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [float(x) for x in entrada.split()]

lista_ordenada = bubble_sort(numeros)
print(f"Lista ordenada pelo metodo bolha: {lista_ordenada}")