h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

ans = 0
def dfs(i, j, s):
    a = al[i][j]
    if not (a in s):
        s.add(a)
        if i == h - 1 and j == w - 1:
            global ans
            ans += 1
        else:
            if i + 1 < h:
                dfs(i + 1, j, s)
            if j + 1 < w:
                dfs(i, j + 1, s)
        s.remove(a)

dfs(0, 0, set())

print(ans)
