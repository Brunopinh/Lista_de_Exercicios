# 32. Ler uma string e contar a frequência de cada caractere

texto = input("Digite uma string: ")
frequencia = {}
for char in texto:
    frequencia[char] = frequencia.get(char, 0) + 1
print("Frequencia de cada caractere:")
for char, count in frequencia.items():
    print(f"'{char}': {count}")