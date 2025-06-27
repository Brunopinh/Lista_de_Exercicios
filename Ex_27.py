# 27. Calcular o valor de um investimento com juros compostos

capital_inicial = float(input("Digite o capital inicial: "))
taxa_juros = float(input("Digite a taxa de juros (em decimal, ex: 0.05 para 5%): "))
tempo = int(input("Digite o tempo em anos: "))
montante_final = capital_inicial * (1 + taxa_juros) ** tempo
print(f"O valor final do investimento e: {montante_final:.2f}")