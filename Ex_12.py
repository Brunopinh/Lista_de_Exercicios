# 12. Escreva um programa que peça um número e calcule o fatorial desse número.

num = int(input("Digite um número para calcular o fatorial: "))

for i in range(num - 1, 0, -1):
    num *= i
    print(f"Fatorial: {num}")
    
print(f"O fatorial do número é: {num}")