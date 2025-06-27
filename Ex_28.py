# 28. Ler um ano e dizer se é bissexto

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} e bissexto.")
else:
    print(f"O ano {ano} nao e bissexto.")