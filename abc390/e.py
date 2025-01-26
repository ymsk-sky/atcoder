n, x = map(int, input().split())

v1 = []
v2 = []
v3 = []
for _ in range(n):
    v, a, c = map(int, input().split())
    if v == 1:
        v1.append([a, c])
    elif v == 2:
        v2.append([a, c])
    else:
        v3.append([a, c])

def f(l: list) -> list:
    m = len(l)
    # dp[i][j]: i番目まででカロリーがjとなる時の最大ビタミン値
    dp = [[0] * (x + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        a, c = l[i - 1]
        for j in range(x + 1):
            dp[i][j] = dp[i - 1][j]
            if j - c >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - c] + a)
    return dp[m]

res1 = f(v1)
res2 = f(v2)
res3 = f(v3)

ans = 0
for x1 in range(x + 1):
    for x2 in range(x + 1):
        if x1 + x2 > x:
            break
        x3 = x - (x1 + x2)
        tmp = min(res1[x1], res2[x2], res3[x3])
        ans = max(ans, tmp)
print(ans)
