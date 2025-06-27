# 19. Escreva um programa que leia uma palavra e a exiba de trás para frente.

palavra = str(input("Digite uma palavra: "))
palavra_invertida = palavra[::-1]  
print(f"A palavra invertida é: {palavra_invertida}")  