n, m = map(int, input().split())

ans = [[False] * n for _ in range(n)]

for _ in range(m):
    k, *xl = list(map(int, input().split()))
    for i in range(k):
        x = xl[i]
        for j in range(i + 1, k):
            y = xl[j]
            ans[x - 1][y - 1] = True
            ans[y - 1][x - 1] = True

for i in range(n):
    for j in range(n):
        if i != j:
            if ans[i][j]:
                continue
            else:
                print("No")
                exit()

print("Yes")