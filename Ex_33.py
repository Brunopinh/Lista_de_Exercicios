# 33 Ler um número e dizer se ele é palíndromo

num_str = input("Digite um numero: ")
if num_str == num_str[::-1]:
    print(f"O numero {num_str} e palindromo.")
else:
    print(f"O numero {num_str} nao e palindromo.")