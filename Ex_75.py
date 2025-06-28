# 75. Escreva um programa que simule o lançamento de dois dados e conte quantas vezes a soma deu 7.

import random

num_lancamentos = int(input("Quantos lançamentos de dados deseja simular? "))
soma_sete = 0

for _ in range(num_lancamentos):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    
    # print(f"Dados: {dado1} + {dado2} = {soma}") # Opcional: para ver cada lançamento

    if soma == 7:
        soma_sete += 1

print(f"Em {num_lancamentos} lançamentos, a soma deu 7 por {soma_sete} vezes.")