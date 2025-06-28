# 47. Escreva um programa que leia um dicionário e exiba suas chaves e valores.

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

print("Chaves e valores do dicionario:")
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")