n = int(input())
dl = [[0] * n for _ in range(n)]

for i in range(n - 1):
    d = list(map(int, input().split()))
    for k in range(n - i - 1):
        j = k + i + 1
        dl[i][j] = dl[j][i] = d[k]

# dp[S]: 集合Sが使用済みの場合の最大値
dp = [0 for _ in range((1 << n) + 1)]

for S in range((1 << n) + 1):
    for v in range(n):
        if (S >> v) & 1 == 0:
            # vが使われていない場合はスルー
            continue
        for u in range(v + 1, n):
            if (S >> u) & 1 == 0:
                continue
            d = dl[u][v]
            dp[S] = max(dp[S], dp[S - (1 << v) - (1 << u)] + d)
print(dp[(1 << n) - 1])


"""
2<=n<=16
1<=d<=10**9
"""
