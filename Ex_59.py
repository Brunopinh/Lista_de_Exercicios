# 59. Escreva um programa com uma função que retorne o maior valor em uma lista.

def encontrar_maior(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [float(x) for x in entrada.split()]

maior_valor = encontrar_maior(numeros)
if maior_valor is not None:
    print(f"O maior valor na lista e: {maior_valor}")
else:
    print("Nenhum numero foi digitado.")