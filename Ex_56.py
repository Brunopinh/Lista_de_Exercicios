# 56. Escreva um programa com uma função que retorne True se um número for primo.

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero_digitado = int(input("Digite um numero para verificar se e primo: "))
if eh_primo(numero_digitado):
    print(f"O numero {numero_digitado} e primo.")
else:
    print(f"O numero {numero_digitado} nao e primo.")