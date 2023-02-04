n, m = map(int, input().split())
al = list(map(int, input().split()))  # n
cl = list(map(int, input().split()))  # n
xl = list(map(int, input().split()))  # m
INF = float("inf")
# dp[i][j]: 残りi個のときに商品jを購入したときの最小値
dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        pass


"""
1<=m<=n<=5000
1<=a<=10**9
1<=c<=10**9
1<=x1<x2<...<xm<=n
"""
