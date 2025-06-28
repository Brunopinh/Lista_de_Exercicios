# 72. Escreva um programa que leia um arquivo texto e conte o número de linhas e palavras.

nome_arquivo = input("Digite o nome do arquivo de texto (ex: texto.txt): ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        num_linhas = 0
        num_palavras = 0
        for linha in arquivo:
            num_linhas += 1
            palavras = linha.split()
            num_palavras += len(palavras)
    
    print(f"Arquivo '{nome_arquivo}':")
    print(f"Número de linhas: {num_linhas}")
    print(f"Número de palavras: {num_palavras}")
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")