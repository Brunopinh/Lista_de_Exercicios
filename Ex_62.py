# 62. Escreva um programa que receba uma lista de listas e flatenize (achate) a estrutura.

print("Digite as sublistas (ex: 1 2 3). Digite uma linha vazia para terminar a lista de listas.")
lista_de_listas = []
while True:
    sublista_str = input()
    if not sublista_str:
        break
    lista_de_listas.append([int(x) for x in sublista_str.split()])

lista_achatada = []
for sublista in lista_de_listas:
    for item in sublista:
        lista_achatada.append(item)

print(f"Lista achatada: {lista_achatada}")