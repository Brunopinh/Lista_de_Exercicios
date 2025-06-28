# 49. Escreva um programa que leia dois dicionários e os mescle em um novo.

def criar_dicionario(nome_dic):
    dic = {}
    print(f"Crie o {nome_dic} (chave:valor, 'fim' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            break
        if ':' in entrada:
            chave, valor = entrada.split(':', 1)
            dic[chave.strip()] = valor.strip()
        else:
            print("Formato invalido. Use 'chave:valor'.")
    return dic

dic1 = criar_dicionario("primeiro dicionario")
dic2 = criar_dicionario("segundo dicionario")

dic_mesclado = dic1.copy()
dic_mesclado.update(dic2)
print(f"Dicionarios mesclados: {dic_mesclado}")