import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

n, x = map(int, input().split())
pl = list(map(int, input().split()))

# dp[i][j]: i番目まででj枚が当たる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 100
for i in range(1, n + 1):
    p = pl[i - 1]
    for j in range(i + 1):
        dp[i][j] = dp[i - 1][j]*(100 - p) + dp[i - 1][j - 1]*p
        dp[i][j] /= 100
P0 = dp[n][0]

@lru_cache(maxsize=None)
def f(x: int):
    """
    レアカードをあとx枚手に入れるのに必要なパックの個数の期待値
    """
    if x <= 0:
        return 0
    res = P0
    # 1パックで1~n枚
    for y in range(1, n + 1):
        res += dp[n][y]*(f(x - y) + 1)
    return res / (100 - P0)

ans = f(x)
print(ans)

"""
期待値とは, 確率の逆数
* 有効なカードを引く期待値は, 有効なカードを引く確率の逆数
-> 3/40でカードを引く期待値は, 40/3 = 13.3333333
"""