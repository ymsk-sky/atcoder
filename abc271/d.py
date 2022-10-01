n, s = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i枚目までで総和がjである組み合わせリスト
dp = [[[] for _ in range(10001)] for _ in range(n + 1)]
a, b = abl[0]
dp[1][a] = [0]
dp[1][b] = [1]

for i in range(2, n + 1):
    a, b = abl[i - 1]
    for j in range(1, 10001):
        if 0 <= j - a < 10001:
            if len(dp[i - 1][j - a]) == i - 1:
                dp[i][j] = dp[i - 1][j - a] + [0]
                # dp[i][j].append(0)
        if 0<= j - b < 10001:
            if len(dp[i - 1][j - b]) == i - 1:
                dp[i][j] = dp[i - 1][j - b] + [1]
                #dp[i][j].append(1)

if len(dp[n][s]) == n:
    print("Yes")
    print("".join(["H" if d == 0 else "T" for d in dp[n][s]]))
else:
    print("No")

"""
1<=n<=100
1<=s<=10000
1<=a,b<=100

3 11
1 4
2 3
5 7

dp
[[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
[[], [0], [], [], [], [], [], [], [], [], [], [1], [], [], []]
[[], [], [], [0,0], [0,1], [], [], [], [], [], [], [], [1,0], [1,1], []]
[[], [], [], [], [], [], [], [], [], [0,0,0], [0,1,0], [0,0,1], [0,1,1], [], [], ....]

125 8
127 10
135 9
137 11
425 11
427 13
435 12
437 14
"""
