# 90. Escreva um programa que calcule a precisão, revocação e f1-score a partir da matriz de confusão.

# Pede os valores da matriz de confusão diretamente ao usuário
tp = int(input("Digite o valor de True Positives (TP): "))
fp = int(input("Digite o valor de False Positives (FP): "))
fn = int(input("Digite o valor de False Negatives (FN): "))
tn = int(input("Digite o valor de True Negatives (TN): "))

# Calcula Precisão (Precision)
if (tp + fp) == 0:
    precisao = 0.0
else:
    precisao = tp / (tp + fp)

# Calcula Revocação (Recall ou Sensibilidade)
if (tp + fn) == 0:
    revocacao = 0.0
else:
    revocacao = tp / (tp + fn)

# Calcula F1-Score
if (precisao + revocacao) == 0:
    f1_score = 0.0
else:
    f1_score = 2 * (precisao * revocacao) / (precisao + revocacao)

print(f"\nPrecisão: {precisao:.2f}")
print(f"Revocação: {revocacao:.2f}")
print(f"F1-Score: {f1_score:.2f}")