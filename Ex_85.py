# 85. Escreva um programa que implemente o método de busca linear.

def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i # Retorna o índice do item se encontrado
    return -1 # Retorna -1 se o item não for encontrado

entrada_lista = input("Digite uma lista de números separados por espaços: ")
numeros = [int(x) for x in entrada_lista.split()]
item_buscar = int(input("Digite o número que deseja buscar: "))

indice = busca_linear(numeros, item_buscar)
if indice != -1:
    print(f"O número {item_buscar} foi encontrado no índice {indice}.")
else:
    print(f"O número {item_buscar} não foi encontrado na lista.")