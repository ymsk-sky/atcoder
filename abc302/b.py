h, w = map(int, input().split())
s = [input() for _ in range(h)]
snuke = "snuke"
ans = []
def f(i, j, p, q, k):
    u, v = i + p, j + q
    if u < 0 or u >= h or v < 0 or v >= w:
        return
    if s[u][v] == snuke[k + 1]:
        ans.append((u, v))
        if k + 1 == 4:
            for an in ans:
                print(*[a + 1 for a in an])
            exit()
        f(u, v, p, q, k + 1)

for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            for p in (-1, 0, 1):
                for q in (-1, 0, 1):
                    if p == 0 and q == 0:
                        continue
                    ans = []
                    ans.append((i, j))
                    f(i, j, p, q, 0)
