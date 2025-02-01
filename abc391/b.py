n, m = map(int, input().split())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        ok = True
        for p in range(m):
            for q in range(m):
                if sl[i + p][j + q] != tl[p][q]:
                    ok = False
        if ok:
            print(i + 1, j + 1)
            exit()
