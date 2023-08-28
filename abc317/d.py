n = int(input())
xyzl = [list(map(int, input().split())) for _ in range(n)]
zm = sum([z for _, _, z in xyzl])
# dp[i][j]: i番目までで価値がjになる最小の重さ
dp = [[0] * (zm + 1) for _ in range(n + 1)]
