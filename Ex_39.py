# 39. Escreva um programa que leia uma lista de nomes e retorne apenas os que começam com vogal.

entrada = input("Digite uma lista de nomes separados por virgulas: ")
nomes = [nome.strip() for nome in entrada.split(',')]
vogais = "aeiouAEIOU"
nomes_com_vogal = []
for nome in nomes:
    if nome and nome[0] in vogais:
        nomes_com_vogal.append(nome)
print(f"Nomes que começam com vogal: {nomes_com_vogal}")