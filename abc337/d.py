h, w, k = map(int, input().split())
sl = [input() for _ in range(h)]
INF = float("inf")
ans = INF
# 横方向確認
if k <= w:
    for i in range(h):
        d = {"o": 0, "x": 0, ".": 0}
        for j in range(k):
            d[sl[i][j]] += 1
        if d["x"] == 0:
            ans = min(ans, d["."])
        for j in range(k, w):
            d[sl[i][j - k]] -= 1
            d[sl[i][j]] += 1
            if d["x"] == 0:
                ans = min(ans, d["."])
# 縦方向確認
if k <= h:
    for j in range(w):
        d = {"o": 0, "x": 0, ".": 0}
        for i in range(k):
            d[sl[i][j]] += 1
        if d["x"] == 0:
            ans = min(ans, d["."])
        for i in range(k, h):
            d[sl[i - k][j]] -= 1
            d[sl[i][j]] += 1
            if d["x"] == 0:
                ans = min(ans, d["."])
print(-1 if ans == INF else ans)

"""
h*w <= 2*10**5
"""
