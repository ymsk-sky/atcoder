import sys
sys.setrecursionlimit(10**7)

a, b, c = map(int, input().split())

memo = [[[-1] * 101 for _ in range(101)] for _ in range(101)]
def f(x, y, z):
    if memo[x][y][z] != -1:
        return memo[x][y][z]

    if x == 100 or y == 100 or z == 100:
        return 0

    res = 0
    res += (f(x + 1, y, z) + 1)*x/(x + y + z)
    res += (f(x, y + 1, z) + 1)*y/(x + y + z)
    res += (f(x, y, z + 1) + 1)*z/(x + y + z)
    memo[x][y][z] = res
    return res

print(f(a, b, c))