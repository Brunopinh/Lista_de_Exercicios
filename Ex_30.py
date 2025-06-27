# 30. Ler uma string e retornar seu caractere do meio

texto = input("Digite uma string: ")
tamanho = len(texto)
if tamanho % 2 == 1:
    meio = texto[tamanho // 2]
    print(f"O caractere do meio e: {meio}")
else:
    meio1 = texto[tamanho // 2 - 1]
    meio2 = texto[tamanho // 2]
    print(f"Os caracteres do meio sao: {meio1}{meio2}")