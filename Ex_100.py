# 100. Escreva um programa que simule um mini projeto de análise de dados: leia um CSV com dados de vendas e gere um relatório com total por vendedor, produto mais vendido, média de vendas por dia e gráfico simples (texto ou ASCII).

import csv
from collections import defaultdict

nome_arquivo_vendas = input("Digite o nome do arquivo CSV de vendas (ex: vendas.csv): ")

# Estruturas para armazenar os dados e resultados
vendas_por_vendedor = defaultdict(float)
contagem_produtos = defaultdict(int)
vendas_por_dia = defaultdict(float)
contagem_dias = defaultdict(int)

try:
    with open(nome_arquivo_vendas, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Assume que o CSV tem colunas como 'Vendedor', 'Produto', 'Valor', 'Data'
        # Adapte os nomes das colunas conforme seu CSV
        for i, row in enumerate(csv_reader):
            # Ignora o cabeçalho se o DictReader não for usado ou houver linhas extras
            if i == 0 and 'Vendedor' not in row: # Verifica se é o cabeçalho
                 continue # Pula o cabeçalho se DictReader falhar

            try:
                vendedor = row['Vendedor']
                produto = row['Produto']
                valor = float(row['Valor'])
                data = row['Data'] # Assume formato YYYY-MM-DD ou similar para agrupamento

                vendas_por_vendedor[vendedor] += valor
                contagem_produtos[produto] += 1
                vendas_por_dia[data] += valor
                contagem_dias[data] += 1

            except KeyError as e:
                print(f"Erro: Coluna '{e}' não encontrada no CSV. Verifique o cabeçalho do arquivo.")
                print(f"Linha problematica: {row}")
                exit() # Sai do programa se uma coluna essencial estiver faltando
            except ValueError as e:
                print(f"Erro de valor em uma linha: {e}. Linha: {row}")
                continue # Pula a linha com erro de valor

    print("\n--- Relatório de Vendas ---")

    # 1. Total por vendedor
    print("\nTotal de Vendas por Vendedor:")
    for vendedor, total in sorted(vendas_por_vendedor.items()):
        print(f"- {vendedor}: R$ {total:.2f}")

    # 2. Produto mais vendido (por quantidade)
    if contagem_produtos:
        produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
        print(f"\nProduto Mais Vendido (por quantidade): {produto_mais_vendido} ({contagem_produtos[produto_mais_vendido]} unidades)")
    else:
        print("\nNenhum produto foi registrado.")

    # 3. Média de vendas por dia
    print("\nMédia de Vendas por Dia:")
    media_total_vendas_por_dia = {}
    for data, total_vendas_dia in vendas_por_dia.items():
        media_total_vendas_por_dia[data] = total_vendas_dia / contagem_dias[data]
        print(f"- {data}: R$ {media_total_vendas_por_dia[data]:.2f}")
    
    # 4. Gráfico simples (ASCII) das vendas por dia
    if media_total_vendas_por_dia:
        print("\nGráfico de Vendas por Dia (ASCII):")
        # Encontra a venda máxima para escalonar o gráfico
        max_venda_dia = max(media_total_vendas_por_dia.values())
        
        for data in sorted(media_total_vendas_por_dia.keys()):
            valor = media_total_vendas_por_dia[data]
            # Escala a barra para um tamanho razoável (ex: max de 50 caracteres)
            num_asteriscos = int((valor / max_venda_dia) * 50)
            print(f"{data}: {'*' * num_asteriscos} R$ {valor:.2f}")
    else:
        print("\nNão há dados suficientes para gerar o gráfico de vendas por dia.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_vendas}' não foi encontrado. Certifique-se de que o arquivo está no mesmo diretório do script ou forneça o caminho completo.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")