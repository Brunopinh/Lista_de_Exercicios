# 51. Escreva um programa que leia uma lista de dicionários e some um valor de uma chave específica.

lista_de_dicionarios = []
print("Crie uma lista de dicionarios (ex: nome:texto, idade:numero). Digite 'novo' para um novo dicionario, 'fim' para terminar.")
temp_dic = {}
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if entrada.lower() == 'novo':
        if temp_dic:
            lista_de_dicionarios.append(temp_dic)
            temp_dic = {}
        continue
    
    if ':' in entrada:
        chave, valor = entrada.split(':', 1)
        try:
            temp_dic[chave.strip()] = int(valor.strip())
        except ValueError:
            temp_dic[chave.strip()] = valor.strip()
    else:
        print("Formato invalido. Use 'chave:valor' ou 'novo'.")
if temp_dic:
    lista_de_dicionarios.append(temp_dic)

chave_para_somar = input("Digite a chave para somar os valores: ")
soma_total = 0
for dic in lista_de_dicionarios:
    if chave_para_somar in dic and isinstance(dic[chave_para_somar], (int, float)):
        soma_total += dic[chave_para_somar]
print(f"Soma dos valores da chave '{chave_para_somar}': {soma_total}")