s = input()
n = len(s)
if n%2:
    print(0)
    exit()
mod = 998244353

dist = [[0] * (n//2 + 1) for _ in range(n + 1)]
dist[0][0] = 1
for i in range(1, n + 1):
    c = s[i - 1]
    for j in range(n//2 + 1):
        if c == "(":
            if j != 0:
                dist[i][j] += dist[i - 1][j - 1]
        elif c == ")":
            if j != n//2:
                dist[i][j] += dist[i - 1][j + 1]
        elif c == "?":
            if j != 0:
                dist[i][j] += dist[i - 1][j - 1]
            if j != n//2:
                dist[i][j] += dist[i - 1][j + 1]
        dist[i][j] %= mod
print(dist[n][0])

"""
(: +1
): -1
途中で0未満になることはない
はじめとおわりは0
"""
