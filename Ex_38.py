# 38. Escreva um programa que leia uma lista de nomes e retorne os nomes em ordem alfabética.

entrada = input("Digite uma lista de nomes separados por virgulas: ")
nomes = [nome.strip() for nome in entrada.split(',')]
nomes.sort()
print(f"Nomes em ordem alfabetica: {nomes}")