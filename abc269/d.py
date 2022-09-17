import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]
xyl = [[x + 1000, y + 1000] for x, y in xyl]

# l[x][y]: (x, y)は黒く塗られているか
l = [[False] * 2001 for _ in range(2001)]
for x, y in xyl:
    l[x][y] = True

# すでに数えたか
g = [[False] * 2001 for _ in range(2001)]

def fs(x, y):
    if l[x][y] and not g[x][y]:
        g[x][y] = True
        for i, j in [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]:
            if (0 <= x + i <= 2000) and (0 <= y + j <= 2000):
                g[x][y] = True
                if l[x][y]:
                    fs(x + i, y + j)

ans = 0
for i in range(n):
    x, y = xyl[i]
    if not g[x][y]:
        fs(x, y)
        ans += 1
print(ans)

"""
1<=n<=1000
|x|,|y|<=1000

6
-1 -1
0 1
0 2
1 0
1 2
2 0

"""
