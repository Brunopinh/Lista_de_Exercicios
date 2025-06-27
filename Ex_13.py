# 13. Escreva um programa que exiba os 10 primeiros números da sequência de
# Fibonacci.

fib_prev = []
for i in range(10):
    
    if i == 0:
        fib_prev.append(i)
    elif i == 1:
        fib_prev.append(i)
    else:
        num = fib_prev[i-1] + fib_prev[i-2] 
        fib_prev.append(num)
    
print(fib_prev)

