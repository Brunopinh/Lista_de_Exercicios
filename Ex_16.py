# 16. Escreva um programa que leia uma string e diga quantas vogais ela tem.

palavra = str(input("Digite uma palavra: "))

vogais = []
for i in palavra:
    if i in "aeiou":
        vogais.append(i)
    
quantidade =  len(vogais)
print(quantidade)