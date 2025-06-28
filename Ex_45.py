# 45. Escreva um programa que leia uma lista de nomes e conte quantos nomes têm mais de 5 letras.

entrada = input("Digite uma lista de nomes separados por virgulas: ")
nomes = [nome.strip() for nome in entrada.split(',')]
contagem = 0
for nome in nomes:
    if len(nome) > 5:
        contagem += 1
print(f"Numero de nomes com mais de 5 letras: {contagem}")