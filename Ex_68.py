# 68. Escreva um programa que leia um CSV simples e exiba os dados.

import csv

nome_arquivo = input("Digite o nome do arquivo CSV (ex: dados.csv): ")

try:
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        print(f"Conteúdo de '{nome_arquivo}':")
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")