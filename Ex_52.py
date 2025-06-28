# 52. Escreva um programa que leia dados de uma lista de alunos (nome, nota) e calcule a média da turma.

alunos = []
print("Digite o nome e a nota do aluno (ex: Nome:Nota). Digite 'fim' para terminar.")
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    if ':' in entrada:
        nome, nota_str = entrada.split(':', 1)
        try:
            nota = float(nota_str.strip())
            alunos.append({'nome': nome.strip(), 'nota': nota})
        except ValueError:
            print("Nota invalida. Digite um numero.")
    else:
        print("Formato invalido. Use 'Nome:Nota'.")

if alunos:
    soma_notas = sum(aluno['nota'] for aluno in alunos)
    media_turma = soma_notas / len(alunos)
    print(f"A media da turma e: {media_turma:.2f}")
else:
    print("Nenhum aluno foi adicionado.")