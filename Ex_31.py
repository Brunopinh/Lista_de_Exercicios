# 31. Contar quantas vezes cada vogal aparece em uma string

texto = input("Digite uma string: ").lower()
vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for char in texto:
    if char in vogais:
        vogais[char] += 1
print("Contagem de vogais:")
for vogal, count in vogais.items():
    print(f"{vogal}: {count}")