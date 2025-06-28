# 40. Escreva um programa que leia uma frase e retorne as palavras em ordem reversa.

frase = input("Digite uma frase: ")
palavras = frase.split()
palavras.reverse()
frase_reversa = ' '.join(palavras)
print(f"Frase com palavras em ordem reversa: {frase_reversa}")