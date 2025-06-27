# 34. Ler uma lista de números e informar o maior e o menor

entrada = input("Digite uma lista de numeros separados por espacos: ")
numeros = [int(x) for x in entrada.split()]
if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior numero e: {maior}")
    print(f"O menor numero e: {menor}")
else:
    print("Nenhum numero foi digitado.")