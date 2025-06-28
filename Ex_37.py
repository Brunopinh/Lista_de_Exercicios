# 37. Escreva um programa que leia uma lista de números e remova os duplicados.

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]
lista_sem_duplicados = list(set(numeros))
print(f"Lista sem duplicados: {lista_sem_duplicados}")