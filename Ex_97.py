# 97. Escreva um programa que salve dados estruturados em JSON.

import json

dados = {}
print("Digite pares de chave e valor para salvar em JSON (ex: nome:João, idade:30). Digite 'fim' para terminar.")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if ':' in entrada:
        chave, valor = entrada.split(':', 1)
        # Tenta converter para número se possível, senão guarda como string
        try:
            dados[chave.strip()] = int(valor.strip())
        except ValueError:
            try:
                dados[chave.strip()] = float(valor.strip())
            except ValueError:
                dados[chave.strip()] = valor.strip()
    else:
        print("Formato inválido. Use 'chave:valor'.")

nome_arquivo = input("Digite o nome do arquivo JSON para salvar (ex: dados.json): ")

try:
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4) # Salva com indentação para legibilidade
    print(f"Dados salvos em '{nome_arquivo}'.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo JSON: {e}")