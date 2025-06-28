# 88. Escreva um programa que implemente a regressão linear simples com base em duas listas.

def regressao_linear_simples(x_vals, y_vals):
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        return "Erro: As listas devem ter o mesmo tamanho e pelo menos 2 elementos."

    n = len(x_vals)
    
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(x_vals[i] * y_vals[i] for i in range(n))
    sum_x2 = sum(x_vals[i] ** 2 for i in range(n))

    # Calcula o coeficiente angular (slope)
    try:
        b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    except ZeroDivisionError:
        return "Erro: Não é possível calcular o coeficiente angular (divisão por zero)."

    # Calcula o intercepto (intercept)
    b0 = (sum_y / n) - b1 * (sum_x / n)
    
    return f"Equação da regressão linear: y = {b0:.2f} + {b1:.2f}x"

entrada_x = input("Digite os valores de X separados por espaços: ")
x_valores = [float(x) for x in entrada_x.split()]

entrada_y = input("Digite os valores de Y separados por espaços: ")
y_valores = [float(y) for y in entrada_y.split()]

resultado_regressao = regressao_linear_simples(x_valores, y_valores)
print(resultado_regressao)