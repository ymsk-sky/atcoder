"""
dp[i] = al[j] + "残り(i-al[j])個のときの後手の最適解(最大個数)"
= al[j] + (i - al[j] - "残り(i-al[j])個のときの先手の最適解(最大個数)")
= al[j] + i - al[j] - dp[i - al[j]]
= i - dp[i - al[j]]
よって
dp[i] = i - dp[i - a]  # a = al[j]
を 1 <= i <= nまで更新していく
"""

import sys

sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
al = list(map(int, input().split()))

# dp[i]: 残りi個のときの先手の最適解(最大個数)
dp = [-1] * (n + 1)

def f(i):
    if dp[i] != -1:
        return dp[i]
    tmp = 0
    for a in al:
        if a <= i:
            tmp = max(tmp, i - f(i - a))
    dp[i] = tmp
    return tmp

f(n)

print(dp[n])

"""
1<=n<=10**4
1<=k<=100
alは昇順

10000 10
1 2 4 8 16 32 64 128 256 512
5136
"""
