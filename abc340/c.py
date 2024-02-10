import sys
sys.setrecursionlimit(10**6)

n = int(input())
d = {0: 0, 1: 0}
def f(x):
    if x in d:
        return d[x]
    s = x
    if x % 2 == 0:
        s += 2 * f(x // 2)
    else:
        s += f(-(-x // 2))
        s += f(x // 2)
    d[x] = s
    return s
ans = f(n)
print(ans)
