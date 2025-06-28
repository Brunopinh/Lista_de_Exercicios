# 83. Escreva um programa que conte a frequência de bigramas em um texto.

from collections import defaultdict

texto = input("Digite um texto: ")
palavras = texto.lower().split()

bigramas = defaultdict(int)
for i in range(len(palavras) - 1):
    bigrama = (palavras[i], palavras[i+1])
    bigramas[bigrama] += 1

print("Frequência de bigramas:")
for bigrama, contagem in bigramas.items():
    print(f"'{bigrama[0]} {bigrama[1]}': {contagem}")