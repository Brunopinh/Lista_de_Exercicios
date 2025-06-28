# 71. Escreva um programa que gere números aleatórios e os salve em um arquivo.

import random

nome_arquivo = input("Digite o nome do arquivo para salvar os números (ex: numeros.txt): ")
quantidade = int(input("Quantos números aleatórios deseja gerar? "))
limite_inferior = int(input("Limite inferior para os números: "))
limite_superior = int(input("Limite superior para os números: "))

try:
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(quantidade):
            numero = random.randint(limite_inferior, limite_superior)
            arquivo.write(str(numero) + '\n')
    print(f"{quantidade} números aleatórios foram salvos em '{nome_arquivo}'.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")