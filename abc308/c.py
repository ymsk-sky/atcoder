import numpy as np

n = int(input())
al = []
bl = []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
al = np.array(al).astype("float128")
bl = np.array(bl).astype("float128")
l = al / (al + bl)
l = [(-(i + 1), p) for i, p in enumerate(l)]
l.sort(key=lambda e: e[1], reverse=True)
print(*[-i for i, _ in l])
