x, y, z = map(int, input().split())
s = input()
n = len(s)
INF = float("inf")
# dp[i][j]: sのi文字目までが入力完了しcapsがjのときの最短時間
dp = [[INF]*2 for _ in range(n + 1)]
dp[0] = [0, z]
for i in range(1, n + 1):
    c = s[i - 1]
    if c == "a":
        dp[i][0] = min(dp[i - 1][0] + x, dp[i - 1][1] + y + z)
        dp[i][1] = min(dp[i - 1][0] + x + z, dp[i - 1][1] + y)
    elif c == "A":
        dp[i][0] = min(dp[i - 1][0] + y, dp[i - 1][1] + x + z)
        dp[i][1] = min(dp[i - 1][0] + y + z, dp[i - 1][1] + x)
print(min(dp[n]))

"""
1<=x,y,z<=10**9
1<=|s|<=3*10**5
"""
