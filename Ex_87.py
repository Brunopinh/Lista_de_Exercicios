# 87. Escreva um programa que normalize uma lista de dados numéricos.

def normalizar_min_max(lista):
    if not lista:
        return []
    
    min_val = min(lista)
    max_val = max(lista)

    if max_val == min_val: # Evita divisão por zero se todos os valores forem iguais
        return [0.0 for _ in lista]

    lista_normalizada = [(x - min_val) / (max_val - min_val) for x in lista]
    return lista_normalizada

entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [float(x) for x in entrada.split()]

lista_normalizada = normalizar_min_max(numeros)
print(f"Lista normalizada (Min-Max): {lista_normalizada}")