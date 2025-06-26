# 13. Escreva um programa que exiba os 10 primeiros números da sequência de
# Fibonacci.

for i in range(10):
    if i == 0:
        fib = 0
    elif i == 1:
        fib = 1
    else:
        fib = fib_prev + fib
    fib_prev = fib if i > 0 else 0
    print(fib)