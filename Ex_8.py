# 8. Escreva um programa que peça três números e informe o menor entre eles.

numeros = []

for i in range(3): 
    i += 1
    num = int(input(f"informe o {i} numero: "))
    numeros.append(num)

menor = numeros[0]

for num in numeros:
    if menor > num:
        menor = num
   
print(f"\nO menor numero é: {menor}")