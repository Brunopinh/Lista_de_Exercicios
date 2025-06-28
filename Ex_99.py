# 99. Escreva um programa que converta dados de um CSV para JSON.

import csv
import json

nome_arquivo_csv = input("Digite o nome do arquivo CSV de entrada: ")
nome_arquivo_json = input("Digite o nome do arquivo JSON de saída: ")

dados = []
try:
    with open(nome_arquivo_csv, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dados.append(row)

    with open(nome_arquivo_json, 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)
    
    print(f"Dados convertidos de '{nome_arquivo_csv}' para '{nome_arquivo_json}' com sucesso.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_csv}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")