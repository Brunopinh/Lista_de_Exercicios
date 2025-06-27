# 18. Escreva um programa que leia uma string e diga quantas palavras ela tem.

palavra = str(input("Digite uma frase: "))  

palavra = palavra.split()  # Divide a string em palavras
quantidade = len(palavra)  # Conta o número de palavras
print(f"A frase tem {quantidade} palavras.")  # Exibe o resultado