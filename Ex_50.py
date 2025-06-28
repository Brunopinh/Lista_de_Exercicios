# 50. Escreva um programa que inverta as chaves e valores de um dicionário.

dicionario_original = {}
print("Crie o dicionario para inverter (chave:valor, 'fim' para terminar):")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if ':' in entrada:
        chave, valor = entrada.split(':', 1)
        dicionario_original[chave.strip()] = valor.strip()
    else:
        print("Formato invalido. Use 'chave:valor'.")

dicionario_invertido = {valor: chave for chave, valor in dicionario_original.items()}
print(f"Dicionario invertido: {dicionario_invertido}")