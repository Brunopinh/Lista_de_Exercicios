# 74. Escreva um programa que simule um sistema de login e senha com verificação.

# Usuários e senhas pré-definidos (em um cenário real, isso viria de um banco de dados ou arquivo)
usuarios_cadastrados = {
    "user1": "pass123",
    "admin": "adminpass",
    "joao": "senha123"
}

print("Sistema de Login")
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

if username in usuarios_cadastrados and usuarios_cadastrados[username] == password:
    print("Login bem-sucedido! Bem-vindo(a).")
else:
    print("Nome de usuário ou senha incorretos.")