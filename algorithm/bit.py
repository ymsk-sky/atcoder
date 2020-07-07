from itertools import product

N = 3  # ビット数
for p in product((0, 1), repeat=N):
    print(p)
