import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())

d = dict()
def f(k):
    if k == 0:
        return 1
    if k in d:
        return d[k]
    else:
        k3 = f(k // 3)
        d[k // 3] = k3
        k2 = f(k // 2)
        d[k // 2] = k2
        return k2 + k3

print(f(n))