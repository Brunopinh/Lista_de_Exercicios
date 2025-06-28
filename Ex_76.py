# 76. Escreva um programa que gere uma senha aleatória com letras e números.

import random
import string

tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))

caracteres = string.ascii_letters + string.digits # Letras maiúsculas, minúsculas e dígitos
senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))

print(f"Senha gerada: {senha}")