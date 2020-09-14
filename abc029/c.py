from itertools import product
n=int(input())
for p in product(('a','b','c'),repeat=n):
    print(''.join(p))
