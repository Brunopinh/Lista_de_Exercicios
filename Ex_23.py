# 23. Gerar os 50 primeiros números pentagonais

for n in range(1, 51):
    pentagonal = n * (3 * n - 1) // 2
    print(pentagonal)