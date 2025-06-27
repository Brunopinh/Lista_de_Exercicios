# 29. Ler uma senha e verificar se ela é válida segundo regras específicas

senha = input("Digite a senha: ")
valida = True
if len(senha) < 8:
    valida = False
elif not any(char.isdigit() for char in senha):
    valida = False
elif not any(char.isupper() for char in senha):
    valida = False
elif not any(char.islower() for char in senha):
    valida = False
if valida:
    print("Senha valida.")
else:
    print("Senha invalida. A senha deve ter no minimo 8 caracteres, incluindo numeros, letras maiusculas e minusculas.")