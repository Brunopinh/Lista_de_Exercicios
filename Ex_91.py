# 91. Escreva um programa que aplique tokenização simples a um texto.

import re

texto = input("Digite um texto para tokenizar: ")

# Remove pontuações e converte para minúsculas
texto_limpo = re.sub(r'[^\w\s]', '', texto).lower()
tokens = texto_limpo.split() # Divide o texto em palavras (tokens)

print(f"Tokens: {tokens}")