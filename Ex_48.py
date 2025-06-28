# 48. Escreva um programa que leia pares de chave e valor e monte um dicionário.

dicionario = {}
print("Digite pares de chave e valor (ex: chave:valor). Digite 'fim' para terminar.")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if ':' in entrada:
        chave, valor = entrada.split(':', 1)
        dicionario[chave.strip()] = valor.strip()
    else:
        print("Formato invalido. Use 'chave:valor'.")
print(f"Dicionario montado: {dicionario}")