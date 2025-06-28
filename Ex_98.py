# 98. Escreva um programa que leia um arquivo JSON e exiba seus dados.
# Python


import json

nome_arquivo = input("Digite o nome do arquivo JSON para ler (ex: dados.json): ")

try:
    with open(nome_arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)
    
    print(f"\nConteúdo de '{nome_arquivo}':")
    print(json.dumps(dados, indent=4)) # Exibe os dados formatados
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{nome_arquivo}' não é um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")