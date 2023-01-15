n = int(input())
al = list(map(int, input().split()))

# dp[i][j]: 休日数がi日のとき
dp = [[]]

"""
1<=n<=5000
1<=a<=10**9
"""
