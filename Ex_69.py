# 69. Escreva um programa que leia um CSV e calcule estatísticas básicas (média, soma, etc.).

import csv

nome_arquivo = input("Digite o nome do arquivo CSV: ")
coluna_para_calcular = input("Digite o nome da coluna numérica para calcular estatísticas: ")

try:
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        valores = []
        for linha in leitor:
            if coluna_para_calcular in linha and linha[coluna_para_calcular].strip():
                try:
                    valores.append(float(linha[coluna_para_calcular]))
                except ValueError:
                    continue # Ignora valores não numéricos

        if valores:
            soma = sum(valores)
            media = soma / len(valores)
            min_val = min(valores)
            max_val = max(valores)

            print(f"\nEstatísticas para a coluna '{coluna_para_calcular}':")
            print(f"Soma: {soma:.2f}")
            print(f"Média: {media:.2f}")
            print(f"Mínimo: {min_val:.2f}")
            print(f"Máximo: {max_val:.2f}")
        else:
            print(f"Nenhum dado numérico encontrado na coluna '{coluna_para_calcular}'.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")