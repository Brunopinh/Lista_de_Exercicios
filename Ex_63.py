# 3. Escreva um programa que receba um texto e crie um dicionário com a frequência de palavras.

texto = input("Digite um texto: ")
texto = texto.lower() # Converte para minúsculas para contar palavras sem distinção de caixa
palavras = texto.split() # Divide o texto em palavras
frequencia_palavras = {}

for palavra in palavras:
    palavra = palavra.strip('.,!?"\'()[]{}') # Remove pontuações
    if palavra: # Garante que a palavra não está vazia após remover pontuações
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1

print("Frequencia de palavras:")
for palavra, contagem in frequencia_palavras.items():
    print(f"'{palavra}': {contagem}")