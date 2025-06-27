# 24. Calcular a área de um triângulo a partir dos lados

a = float(input("Digite o primeiro lado do triangulo: "))
b = float(input("Digite o segundo lado do triangulo: "))
c = float(input("Digite o terceiro lado do triangulo: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"A area do triangulo e: {area:.2f}")