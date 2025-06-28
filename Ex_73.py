# 73. Escreva um programa que leia um arquivo texto e exiba as linhas que contêm uma palavra-chave.

nome_arquivo = input("Digite o nome do arquivo de texto: ")
palavra_chave = input("Digite a palavra-chave para buscar: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        print(f"\nLinhas em '{nome_arquivo}' que contêm '{palavra_chave}':")
        for num_linha, linha in enumerate(arquivo, 1):
            if palavra_chave.lower() in linha.lower():
                print(f"Linha {num_linha}: {linha.strip()}")
except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")