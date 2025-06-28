# 89. Escreva um programa que calcule a matriz de confusão a partir de previsões e rótulos.

# Rótulos verdadeiros e previsões de exemplo (entrada do usuário seria similar)
# Exemplo: labels = [0, 1, 0, 1], predictions = [0, 0, 0, 1]
# 0 = Negativo, 1 = Positivo

print("Digite os rótulos verdadeiros (0 ou 1, separados por espaço):")
rotulos_verdadeiros = [int(x) for x in input().split()]

print("Digite as previsões do modelo (0 ou 1, separados por espaço):")
previsoes = [int(x) for x in input().split()]

if len(rotulos_verdadeiros) != len(previsoes):
    print("Erro: O número de rótulos e previsões deve ser o mesmo.")
else:
    # Matriz de Confusão:
    # TN (True Negative) | FP (False Positive)
    # ----------------------------------------
    # FN (False Negative) | TP (True Positive)
    
    tn = 0
    fp = 0
    fn = 0
    tp = 0

    for i in range(len(rotulos_verdadeiros)):
        if rotulos_verdadeiros[i] == 0 and previsoes[i] == 0:
            tn += 1
        elif rotulos_verdadeiros[i] == 0 and previsoes[i] == 1:
            fp += 1
        elif rotulos_verdadeiros[i] == 1 and previsoes[i] == 0:
            fn += 1
        elif rotulos_verdadeiros[i] == 1 and previsoes[i] == 1:
            tp += 1
            
    print("\nMatriz de Confusão:")
    print(f"TN: {tn} | FP: {fp}")
    print(f"FN: {fn} | TP: {tp}")