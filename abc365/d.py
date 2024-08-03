n = int(input())
s = input()
# dp[i][j]: i回目に高橋君が手jを出したときの最大勝利回数
dp = [[0] * 3 for _ in range(n + 1)]
# R:0, P:1, S:2
for i in range(1, n + 1):
    aoki_hand = s[i - 1]
    if aoki_hand == "R":
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + 1
    elif aoki_hand == "P":
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + 1
    elif aoki_hand == "S":
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + 1
ans = max(dp[n])
print(ans)


"""
1<=n<=2*10**5
"""
