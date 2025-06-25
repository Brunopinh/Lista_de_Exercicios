# 7. Escreva um programa que peça três números e informe o maior entre eles.

numeros = []

for i in range(3): 
    i += 1
    num = int(input(f"informe o {i} numero: "))
    numeros.append(num)

maior = numeros[0]

for num in numeros:
    if maior < num:
        maior = num
      

print(f"\nO maior numero é: {maior}")

