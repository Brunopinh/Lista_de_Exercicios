# 17. Escreva um programa que leia uma string e diga quantas consoantes ela tem.


palavra = str(input("Digite uma palavra: "))

vogais = []
for i in palavra:
    if i in "bcdfghjklmnpqrstvwxyz":
        vogais.append(i)
    
quantidade =  len(vogais)
print(quantidade)