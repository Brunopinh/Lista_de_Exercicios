# 93. Escreva um programa que conte quantas vezes um valor aparece em uma tupla.

entrada_tupla = input("Digite elementos da tupla separados por espaços: ")
tupla_original = tuple(entrada_tupla.split()) # Cria uma tupla de strings
# Se precisar de números, use: tupla_original = tuple(int(x) for x in entrada_tupla.split())

valor_buscar = input("Digite o valor que deseja contar na tupla: ")

contagem = tupla_original.count(valor_buscar)
print(f"O valor '{valor_buscar}' aparece {contagem} vezes na tupla.")