# 14. Escreva um programa que peça um número e verifique se ele é primo.

num = int(input("Digite um número: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")