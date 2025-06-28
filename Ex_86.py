# 86. Escreva um programa que calcule correlação entre duas listas numéricas.

def calcular_correlacao(lista1, lista2):
    if len(lista1) != len(lista2) or len(lista1) < 2:
        return "Erro: Listas devem ter o mesmo tamanho e pelo menos 2 elementos."

    n = len(lista1)
    
    media1 = sum(lista1) / n
    media2 = sum(lista2) / n

    num = sum((lista1[i] - media1) * (lista2[i] - media2) for i in range(n))
    den1 = sum((lista1[i] - media1) ** 2 for i in range(n))
    den2 = sum((lista2[i] - media2) ** 2 for i in range(n))

    if den1 == 0 or den2 == 0:
        return "Não é possível calcular a correlação (desvio padrão zero em uma ou ambas as listas)."

    correlacao = num / ((den1 * den2) ** 0.5)
    return correlacao

entrada1 = input("Digite a primeira lista de números separados por espaços: ")
lista_numeros1 = [float(x) for x in entrada1.split()]

entrada2 = input("Digite a segunda lista de números separados por espaços: ")
lista_numeros2 = [float(x) for x in entrada2.split()]

correlacao = calcular_correlacao(lista_numeros1, lista_numeros2)
print(f"A correlação entre as duas listas é: {correlacao}")