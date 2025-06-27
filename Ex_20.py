# 20. Escreva um programa que leia uma palavra e verifique se ela é um palíndromo.

palavra = str(input("Digite uma palavra: "))

palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print(f"Essa palavra {palavra} é um palindromo")
else:
    print(f"essa palavra: {palavra} não é um palindromo")