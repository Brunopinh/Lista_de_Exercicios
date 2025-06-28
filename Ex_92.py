# 92. Escreva um programa que calcule a média de notas de alunos usando dicionários.

alunos_notas = {}

print("Digite o nome do aluno e sua nota (ex: Nome:Nota). Digite 'fim' para terminar.")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if ':' in entrada:
        nome, nota_str = entrada.split(':', 1)
        try:
            nota = float(nota_str.strip())
            alunos_notas[nome.strip()] = nota
        except ValueError:
            print("Nota inválida. Digite um número.")
    else:
        print("Formato inválido. Use 'Nome:Nota'.")

if not alunos_notas:
    print("Nenhum aluno adicionado.")
else:
    soma_notas = sum(alunos_notas.values())
    media_turma = soma_notas / len(alunos_notas)
    print(f"A média de notas da turma é: {media_turma:.2f}")