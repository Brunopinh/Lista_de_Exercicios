# 70. Escreva um programa que filtre dados de um CSV por critério específico.

import csv

nome_arquivo = input("Digite o nome do arquivo CSV: ")
coluna_filtro = input("Digite o nome da coluna para filtrar: ")
valor_filtro = input(f"Digite o valor pelo qual filtrar na coluna '{coluna_filtro}': ")

try:
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        
        cabeçalho = leitor.fieldnames
        dados_filtrados = []
        
        for linha in leitor:
            if coluna_filtro in linha and linha[coluna_filtro] == valor_filtro:
                dados_filtrados.append(linha)

        if dados_filtrados:
            print(f"\nDados filtrados por '{coluna_filtro}' = '{valor_filtro}':")
            print(cabeçalho) # Exibe o cabeçalho
            for linha in dados_filtrados:
                print([linha[campo] for campo in cabeçalho])
        else:
            print(f"Nenhum dado encontrado para o critério de filtro.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")