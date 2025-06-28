# 46. Escreva um programa que leia uma lista de nomes e retorne os que terminam com uma vogal.

entrada = input("Digite uma lista de nomes separados por virgulas: ")
nomes = [nome.strip() for nome in entrada.split(',')]
vogais = "aeiouAEIOU"
nomes_terminam_vogal = []
for nome in nomes:
    if nome and nome[-1] in vogais:
        nomes_terminam_vogal.append(nome)
print(f"Nomes que terminam com vogal: {nomes_terminam_vogal}")