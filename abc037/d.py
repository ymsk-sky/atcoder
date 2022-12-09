import sys
sys.setrecursionlimit(10 ** 8)

h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
mod = 10**9 + 7

l = ((-1, 0), (1, 0), (0, -1), (0, 1))

# メモ化再帰
dp = [[0] * w for _ in range(h)]
def f(i, j):
    if dp[i][j] > 0:
        return dp[i][j]
    for p, q in l:
        u, v = i + p, j + q
        if u < 0 or h <= u or v < 0 or w <= v:
            continue
        if al[i][j] >= al[u][v]:
            continue
        dp[i][j] += f(u, v) % mod
    dp[i][j] += 1
    dp[i][j] %= mod
    return dp[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        ans += f(i, j)
        ans %= mod
print(ans % mod)
