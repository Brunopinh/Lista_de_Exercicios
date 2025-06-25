# 10. Escreva um programa que peça um número e imprima todos os números pares
# até ele.

num = int(input("me informa um numero: "))

for i in range(num):
    i += 1
    if i%2==0:
        print(f"Numeros pares: {i}")
    