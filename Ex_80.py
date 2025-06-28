# 80. Escreva um programa que calcule o desvio padrão de uma lista de números.

def calcular_desvio_padrao(lista):
    if len(lista) < 2:
        return 0.0 # Desvio padrão não se aplica a listas com menos de 2 elementos
    
    media = sum(lista) / len(lista)
    variancia = sum([(x - media) ** 2 for x in lista]) / (len(lista) - 1) # Desvio padrão amostral
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [float(x) for x in entrada.split()]

if numeros:
    dp = calcular_desvio_padrao(numeros)
    print(f"O desvio padrão da lista é: {dp:.2f}")
else:
    print("Nenhum número foi digitado.")