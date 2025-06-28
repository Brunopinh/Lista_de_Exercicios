# 78. Escreva um programa que implemente o algoritmo de busca binária.

def busca_binaria(lista, item):
    lista_ordenada = sorted(lista) # A busca binária exige lista ordenada
    baixo = 0
    alto = len(lista_ordenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista_ordenada[meio]
        
        if chute == item:
            return True
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return False

entrada_lista = input("Digite uma lista de números separados por espaços: ")
numeros = [int(x) for x in entrada_lista.split()]
item_buscar = int(input("Digite o número que deseja buscar: "))

if busca_binaria(numeros, item_buscar):
    print(f"O número {item_buscar} foi encontrado na lista.")
else:
    print(f"O número {item_buscar} não foi encontrado na lista.")